# TidepoolHelper

ssh -i C:\Users\Alexander/.ssh/id_rsa root@165.232.139.185
enter http://165.232.139.185/ in chrome
This script uses www.tide-forecast.com to help find the best times to go tidepooling.

In its current state, the script returns the time and tide height of all daylight low tides occuring today for Half Moon Bay, Huntington Beach, Providence, and Wrightsville Beach.

# Installation
Clone into the repo https://github.com/alexgarnett/TidepoolHelper

Install dependencies

```
pip install -r requirements.txt
```

# Running the App
```
flask --app tidepool_helper/tidepool_helper.py run
```

# Output
After selecting a location from the dropdown menu, you will be redirected to the "/location" URL. 
The exact output depends on the location selected and tides during that day, but will look similar to this.
```
Half-Moon-Bay-California
4:46PM, 0.27m

```

# Testing
In the root directory, run pytest
```
pytest
```
