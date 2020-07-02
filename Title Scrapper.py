import praw
import time

#subreddits to crawl
subreddits=[]
keywords=[]
with open("Subreddits.txt", "r") as f:
    # add all subreddits from text file to filter
    for subreddit in f:
        subreddits.append(subreddit.strip().lower())

with open("Keyword.txt", "r") as f:
    # add all subreddits from text file to filter
    for keyword in f:
        keywords.append(keyword.strip().lower())
print(subreddits)
print(keywords)
# Create read only instance of Reddit
# Bot1 settings is selected from praw.ini
reddit = praw.Reddit("Bot1", config_interpolation="basic")

        
subreddit_name="+".join(subreddits)
print(subreddit_name)

subreddit=reddit.subreddit(subreddit_name)
counter=0
for submission in subreddit.stream.submissions():
    for keyword in keywords:
        if submission==None:
            # print(None)
            # time.sleep(1)
            break
            
        elif keyword in submission.title:
            print(f"{keyword}\n\n{submission.title}")
            time.sleep(1)
            break
       
        else:
            # # print("Keyword Not Found")
            # time.sleep(1)
            break
    counter+=1
    print(counter)

for comment in subreddit.stream.comments():
    for keyword in keywords:
        if comment==None:
            print(None)
            time.sleep(1)
            break
            
        elif keyword in comment.body:
            print(f"{keyword}\n\n{comment.body}")
            time.sleep(1)
            break
       
        else:
            print("Keyword Not Found")
            time.sleep(1)
            break