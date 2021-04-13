# DKSwingDataProcessing

This is a submission for the Diamond Kinetics codding challenge by Radu Lungu.

To use this script, press the green button in the gutter.

Available methods:

**_processData_** - Takes a .csv file and tranforms it into a multidimensional numpy array.

**_searchContinuityAboveValue_** - From indexBegin to indexEnd, search data for values that are higher than threshold. Returns the first index where data has values that meet this criteria for at least winLength samples in a row.

**_backSearchContinuityWithinRange_** - From indexBegin to indexEnd (where indexBegin is larger than indexEnd), search data for values that are higher than thresholdLo and lower than thresholdHi. Returns the first index where data has values that meet this criteria for at least winLength samples in a row.

**_searchContinuityAboveValueTwoSignals_** - From indexBegin to indexEnd, search data1 for values that are higher than threshold1 and also search data2 for values that are higher than threshold2. Returns the first index where both data1 and data2 have values that meet these criteria for at least winLength samples in a row.

**_searchMultiContinuityWithinRange_** - From indexBegin to indexEnd, search data for values that are higher than thresholdLo and lower than thresholdHi. Return the the starting index and ending index of all continuous samples that meet this criteria for at least winLength data points.

Thank you!

For  questions contact Radu Lungu at rlungu@macalester.edu
