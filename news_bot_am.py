import praw 
import time
import requests
import config
import smtplib
import datetime as dt
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "tjl236@nau.edu"
toaddr = "tlanes@asu.edu"
sub_dict = {"title":[], "url":[]}

def authenticate():
	print "Authenticating ..."
	reddit = praw.Reddit(username= config.username,
						password = config.password,
						client_id = config.client_id,
						client_secret = config.client_secret,
					user_agent = "ttjj1995 joke comment responder v0.1")
	print "Authenticated as {}".format(reddit.user.me())
	
	return reddit

def get_sub(r,sub,num):
	rsub = r.subreddit(sub).top('day',limit=num)
	for post in rsub:
		sub_dict.setdefault("title", []).append(post.title)
		sub_dict.setdefault("url", []).append(post.url)
	return sub_dict

def