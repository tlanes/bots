import praw
import os
import time 
import requests
import config

def authenticate():
	print "Authenticating ..."
	reddit = praw.Reddit(username= config.username,
						password = config.password,
						client_id = config.client_id,
						client_secret = config.client_secret,
					user_agent = "____ joke comment responder v0.1")
	print "Authenticated as {}".format(reddit.user.me())
	
	return reddit


def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

def main():
	reddit = authenticate()
	comments_replied_to = get_saved_comments()
	print comments_replied_to

	while(True):
		run_bot(reddit, comments_replied_to)

def run_bot(r, comments_replied_to):
	print "Obtaining 10 comments ... "
	for comment in r.subreddit('test').comments(limit=10):
		if "!joke" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
			print "String with \"joke\" found in comment " + comment.id
			
			comment_reply = "You requested a Chuck Norris joke! Here it is:\n\n"

			joke = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']

			comment_reply += ">" + joke

			comment_reply += "\n\nThis joke came from [ICNDb.com](http://api.icndb.com)"
			#comment.reply("woof.")
			comment.reply(comment_reply)
			print "Replied to comment " + comment.id
	
			comments_replied_to.append(comment.id)

			with open("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	print " Sleeping for 10 sec..."
	time.sleep(10)


if __name__ == '__main__':
	main()



