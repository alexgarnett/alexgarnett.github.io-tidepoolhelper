# TidepoolHelper
This is a personal project that I created in order to gain more exposure to front-end web technologies, back-end 
technologies like Python's Flask framework, containerization, and CI/CD pipelines.
This project started as a simple CLI webscraper. I then decided to turn it into a web app using Flask. I also thought this would be a good
opportunity to learn about DevOps and CI/CD tools, so I containerized it and created a GitLab pipeline for automated 
testing, building, and deployment. The GitLab repo can be found at https://gitlab.com/garnett.alexander.l/TidepoolHelper,
but it is no longer connected to the Digital Oecan deployment server. 

The app uses www.tide-forecast.com to help find the best times to go tidepooling.

It returns the time and tide height of all daylight low tides occuring for the next 30 days for either Half Moon Bay, Huntington Beach, Providence, Wrightsville Beach, or San Diego, depending on the user's choice.

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
Location: San Diego California

Date	                    Low Tide Times	    Tide Heights
Thursday 30 November 2023	  None	              ---
Friday 01 December 2023	    None	              ---
Saturday 02 December 2023	  None	              ---
Sunday 03 December 2023	    6:36 AM	            3.46 ft
Monday 04 December 2023	    8:46 AM	            3.36 ft
Tuesday 05 December 2023	  0:05 PM	            1.03 ft
Wednesday 06 December 2023	0:47 PM	            1.24 ft
Thursday 07 December 2023	  2:14 PM, 1:24 PM	  1.48 ft, 1.45 ft
Friday 08 December 2023	    2:52 PM, 1:58 PM	  0.78 ft, 1.64 ft
Saturday 09 December 2023	  1:28 PM	            0.13 ft
Sunday 10 December 2023	    2:04 PM	            -0.44 ft
Monday 11 December 2023	    2:41 PM	            -0.89 ft
Tuesday 12 December 2023	  3:20 PM	            -1.21 ft
Wednesday 13 December 2023	4:02 PM	            -1.36 ft
Thursday 14 December 2023	  None	              ---
Friday 15 December 2023	    None	              ---
Saturday 16 December 2023  	None	              ---
Sunday 17 December 2023	    None	              ---
Monday 18 December 2023	    7:17 AM	            2.68 ft
Tuesday 19 December 2023	  9:00 AM	            2.3 ft
Wednesday 20 December 2023	0:04 PM	            0.93 ft
Thursday 21 December 2023  	0:57 PM	            1.34 ft
Friday 22 December 2023	    2:40 PM, 1:46 PM	  -0.11 ft, 1.67 ft
Saturday 23 December 2023	  1:28 PM	            -0.74 ft
Sunday 24 December 2023	    2:12 PM	            -1.15 ft
Monday 25 December 2023	    2:52 PM	            -1.34 ft
Tuesday 26 December 2023	  3:30 PM	            -1.35 ft
Wednesday 27 December 2023	4:07 PM	            -1.22 ft

```

# Testing
In the root directory, run pytest
```
pytest
```
