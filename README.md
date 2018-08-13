# Squakbot - the open source python / django twitterbot 

# Disclaimer
Squakbot is a tool I made to increase my twitter following, It is not intended for 
comercial use, nor is there any warranty if it goes wrong. Use this at your own 
risk

## Installation
To install squakbot you need to have python 3.x installed. 
For windows visit: https://www.python.org/
Install the 3.x version. Ensure that you tick the "add python to path box" during instalation. Otherwise you will have to add python to your path manually.
If you are running windows you will have to restart your pc and this point.

When your pc restarts check to see if python has be installed by running "python" in a cmd prompt.

Use cd to change your directory to where you installed squakbot. 

Create a virtual environment by running 
virtualenv env

Activate the virtual environment
Run \env\Scripts\activate.bat 
on windows

Install dependencies
pip install -r requirements.txt


If virtualenv is not installed run pip install virtualenv


To run the webserver run:
python manage.py runserver

To acccess the apt manually run 
python manage.py shell

To authenticate yourself run 
from bot_tasks.utils import TwitterAPI 
twitter_api = TwitterAPI("twitter_handle", "consumer_key", "consumer_secret", "access_token", access_private")


Once you have authenticated you can run 


# pass in a target users handle minus the @ symbol and a limit (the max  number of users you want to follow)
twitter_api.follow_all(target, limit)

# pass in a keword and a limit to follow users posting about a certain keyword (the max  number of users you want to follow)
twitter_api.follow_keyword(keyword, limit))

# unfollow users that do not follow you back
twitter_api.unfollow_back()

