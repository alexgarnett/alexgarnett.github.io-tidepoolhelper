# TidepoolHelper
This script uses www.tide-forecast.com to help find the best times to go tidepooling.

In its current state, the script returns the time and tide height of all daylight low tides occuring today for Half Moon Bay, Huntington Beach, Providence, and Wrightsville Beach.

# Installation
Clone into the repo https://github.com/alexgarnett/TidepoolHelper

Install dependencies

```
pip install requirements
pip install bs4
```

# Running the App
```
python .\tidepool-helper.py
```

# Output
The exact output depends on tides during that day, but will look similar to this
```
Half-Moon-Bay-California
4:46PM, 0.27m


Huntington-Beach
3:17PM, 0.55m


Providence-Rhode-Island
1:05PM, 0.13m


Wrightsville-Beach-North-Carolina
1:14PM, 0.17m
```
