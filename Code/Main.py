import sys
import pandas as pd
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main():

	def printTweet(t):
		print("Username: %s" % t.username)
		print("Retweets: %d" % t.retweets)
		print("Text: %s" % t.text)
		print("date: %s" % t.date)
		print("Hashtags: %s\n" % t.hashtags)
		print("Hashtags: %s\n" % t.geo)
	data=[]

	tweetCriteria = got.manager.TweetCriteria().setQuerySearch('meningitis').setSince("2019-01-01").setUntil("2019-01-29").setMaxTweets(30000)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)

 	print(len(tweet))
	print(data)

	for tweet in tweet:
		temp=[]
		temp.append(tweet.date)
		temp.append(tweet.username)
		temp.append(''.join(tweet.text).encode('utf-8').strip())
		temp.append(tweet.retweets)
		temp.append(tweet.geo)
		data.append(temp)

	df=pd.DataFrame(data=data, columns=['date','username','text','retweets numbers','geo'])
	df.to_csv('meningitis/25.csv')


if __name__ == '__main__':
	main()
