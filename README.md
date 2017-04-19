# FlaskImage (Python 3.6), Python 2.X is not tested
A Flask/Jinja2 driven webApp. that aims to provide images related to search term given.

# Quick Guide
## Installation/Setup
1.Install the dependencies:
 + requests
 + flask


2. Run the app on a webserver:
  FlaskImage(This App) can run a webserver to host itself. For Flask to run a webserver, simple run the pyImage.py:
   + Windows: open a Command Prompt and use 'cd' command to navigate CMD to FlaskImage folder
   + type: python pyimage.py
  + Example: 
    + 1:"cd C:\Users\%username%\Downloads\FlaskImage\"
    + 2:"python pyimage.py"

## Usage:
    Append "/" and your search term to the URL:
      + <Protocol><webserver(port)>/<searchTerm>
  Example:
   + http://localhost:5000/Flowers
# Screenshots
![alt tag](https://github.com/KHZ-INTL/FlaskImage/blob/master/1.png)
![alt tag](https://github.com/KHZ-INTL/FlaskImage/blob/master/2.png)


 # Additional Notes
 This tool was made and used for educational purposes (1: Analyse Androidesk behaviours and personal information leaks, 2: Understand http protical and reverse engineer http requests, 3: learn python and Flask and etc...).
 Outcome of research into Androidesk app:
  + information leaks: Analysing Androidesk https activity, important personal information about the user and mobile were leaked: 
    + device name,
    + Device IMEI,
    + brand and model,
    + device os and os version,
    + wifi SSID and MAC,
    + LinuxVersion and android Build revision,
    + Mobile Career,
    + SDK version,
 
Knowing these personal information can lead to identifiying specific exploits and potentially exploiting the system.

By using this script/application you are agreeing to the terms and agreements:
+ 1: The developer of FlaskImage/Pyimage (KHZ-INTL) is not responsible for the wrong doings of your actions and descions.
+ 2: This software should not be used for piracy of contents associated with Androidesk.

Credits:
+ All resources are from androidesk and the credits for each photo/image goes to its respective owner.
+ Thanks to Bootstrap framework, used for frontend.
+ Flask and Jinja 2
+ Requests

 
