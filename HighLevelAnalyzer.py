# High Level Analyzer
# For more information and documentation, please go to https://support.saleae.com/extensions/high-level-analyzer-extensions
from saleae.data import GraphTimeDelta
from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, NumberSetting, ChoicesSetting

# High level analyzers must subclass the HighLevelAnalyzer class.
class Hla(HighLevelAnalyzer):

    # List of settings that a user can set for this High Level Analyzer
    time_delimiter = NumberSetting(label='Time Delimiter [mS]', min_value=1E-6, max_value=1E6)
    out_format = ChoicesSetting(choices=('HEX', 'DEC', 'ASCII'))

    # An optional list of types this analyzer produces, providing a way to customize the way frames are displayed in Logic 2.
    result_types = {
        'data': {
            'format': '{{data.data}}'
        },
        'error': {
            'format': 'Error!'
        },
    }

    # Previous frame and time trackers
    prev_frame = None
    start_chunk_time = None

    # Buffer of current chunk
    chunk = ''


    def __init__(self):
        '''
        Initialize HLA.

        Settings can be accessed using the same name used above.
        '''
        print("Time Delimiter [mS]: "+str(self.time_delimiter))


    def format_data(self, data):
        '''
        Format data given provided format setting
        '''
        if self.out_format == 'HEX':
            return "{0:02X}".format(data)
        return "{0}".format(chr(data) if self.out_format == 'ASCII' else data)


    def decode(self, frame: AnalyzerFrame):

        # support data frames from now
        if frame.type != "data" or "data" not in frame.data.keys():
            return None

        # special case if this is the first frame
        if self.prev_frame is None:
            self.prev_frame = frame
            self.chunk = self.format_data(frame.data['data'][0])
            self.start_chunk_time = frame.start_time
            return None

        # the AnalyzerFrame to return
        ret_frame = None

        # if time delimiter is passed create ret_frame, print chunk, and clear vars
        if frame.start_time > self.prev_frame.end_time + GraphTimeDelta(millisecond=self.time_delimiter):
            ret_frame = AnalyzerFrame('data', self.start_chunk_time, self.prev_frame.end_time, {
                'data': self.chunk
            })
            print(self.chunk)
            self.chunk = ''
            self.start_chunk_time = frame.start_time

        # add chunk data to buffer
        self.chunk += self.format_data(frame.data['data'][0])

        # set the previous frame end time for every frame
        self.prev_frame = frame

        # return a chunk if we hit a time delimeter otherwise None
        return ret_frame