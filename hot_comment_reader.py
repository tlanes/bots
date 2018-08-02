import praw
import config

def authenticate():
	print "Authenticating ..."
	r = praw.Reddit(username = config.username,
					password = config.password,
					client_id = config.client_id,
					client_secret = config.client_secret,
					user_agent = "ttjj1995 joke comment responder v0.1")
	print "Authenticated as {}".format(r.user.me())
	return r

def main():
	reddit = authenticate()

	subreddit = reddit.subreddit('test')

	hot_news = subreddit.hot(limit=3)

	for item in hot_news:
		print item.url


'''
	for submission in hot_news:
		if not submission.stickied:
			print 'Title: {}, ups: {}, downs: {}'.format(submission.title,
													submission.ups,
													submission.downs)
			
			submission.comments.replace_more(limit=0)

			for comment in submission.comments.list():
				print "------------------"
				print "Parent ID: " + str(comment.parent())
				print "Comment ID: " + str(comment.id)
				print comment.body

'''

if __name__ == '__main__':
	main()