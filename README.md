# Time Delimiter Chunking
  
## Description

Delineates chunks of data captured by a time delimiter. Aka when >3ms passes print a new line to terminal. Pretty simple.

## Usage

1. Install this Extension
1. Add a new Analyzer by clicking the "+" arrow in the top right of the Analyzers tab
1. Analyze capture given the analyzer of your choice (Async Serial, SPI, etc.)
1. Add a new High Level Analyzer by clicking the "+" arrow in the top right of the Analyzers tab
1. Select "Time Delimiter Chunking"
1. In the edit/settings popup set "Input Analyzer" to your previous Analyzer
1. In the edit/settings popup set "Time Delimiter [mS]" a value between 1E-6 and 1E6
1. Click "Save"
1. Under the Analyzers tab select the "Data Table" icon under the "data" section
1. Note the time delineated data displayed

## Helpful Hints

Disable the Low Level Analyzer Data Table display by:
1. Selecting the three dot menu to the right of the "Type to search" box
1. Under the "Analyzers" section select "clear"
1. Click the "Time Delimeter Chunking" checkbox
This will allow you to easily see the Time Delimeter Chunking Analyzer data without seeing the Low Level Analyzer data.
