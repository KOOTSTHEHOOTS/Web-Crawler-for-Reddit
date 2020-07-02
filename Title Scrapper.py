import praw
import time

#subreddits to crawl
subreddits=[]
keywords=[]
with open("Subreddits.txt", "r") as f:
    # add all subreddits from text file to filter
    for subreddit in f:
        subreddits.append(subreddit.strip())

with open("Keyword.txt", "r") as f:
    # add all subreddits from text file to filter
    for keyword in f:
        keywords.append(keyword.strip().lower())
print(subreddits)
print(keywords)
# Create read only instance of Reddit
# Bot1 settings is selected from praw.ini
reddit = praw.Reddit("Bot1", config_interpolation="basic")

    # for subreddit_name in subreddits:
    #     subreddit=reddit.subreddit(subreddit_name)
    #     for comment in subreddit.stream.comments(pause_after=1):
    #         for keyword in keywords:
    #              if keyword in comment.body:
    #                 print(f"{keyword}\n\n{comment.body}")
    #                 time.sleep(1)
    #                 break
            
for subreddit_name in subreddits:
    subreddit=reddit.subreddit(subreddit_name)
    for keyword in keywords:
        for submission in subreddit.stream.submissions(pause_after=1):
            if submission==None:
                break
                
            if keyword in submission.title:
               print(f"{keyword}\n\n{submission.title}")
               time.sleep(1)
               break
        
print(f"This is the subreddit title: {subreddit.title}")
    
