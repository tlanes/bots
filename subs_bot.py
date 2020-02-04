#! /usr/bin/python

import praw
import time
import requests
import config
import smtplib
import datetime as dt
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

SUBS = ['spaceporn',
		'woahdude',
		'onepiece',
		'me_irl',
		'interestingasfuck',
		'americandad']

fromaddr = "@nau.edu"
email_list = ["@asu.edu"]

topics_dict = { "title":[], "score":[]}

def authenticate():
	print "Authenticating ..."
	reddit = praw.Reddit(username= config.username,
						password = config.password,
						client_id = config.client_id,
						client_secret = config.client_secret,
					user_agent = "_______ joke comment responder v0.1")
	print "Authenticated as {}".format(reddit.user.me())
	
	return reddit


def get_top_post(r,sub_name, topics_dict):
	subreddit = r.subreddit(sub_name).top('day', limit=1)
	for submission in subreddit:
		topics_dict.setdefault("title", []).append(submission.title)
		topics_dict.setdefault("url", []).append(submission.url)
	return topics_dict


def main():
	r = authenticate()
	body = "Here it is ... Enjoy \n"
	n = 0
	for sub in SUBS:
		post = get_top_post(r,sub,topics_dict)
		body += "\n------------\n" + "Sub: " + str(sub)
		body += "\nTitle: " + post["title"][n].encode('ascii','ignore')
		body += "\nurl: " + post["url"][n].encode('ascii','ignore')
		n+=1
	
	for addr in email_list:
		send_email(body, addr)

	
def send_email(message, address):
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = address
	msg['Subject'] = "The Daily Slosh!!"
	msg.attach(MIMEText(message, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr,"foo(2)=U")
	text = msg.as_string()
	server.sendmail(fromaddr, address, text)
	server.quit()
	time.sleep(3)


if __name__ == '__main__':
	main()









