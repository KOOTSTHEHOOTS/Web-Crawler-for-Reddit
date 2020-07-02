import praw
import time
import re

#subreddits to crawl
subreddits=[]
keywords_list=[]
with open("Subreddits.txt", "r") as f:
    # add all subreddits from text file to filter
    for subreddit in f:
        subreddits.append(subreddit.strip().lower())

with open("Keyword.txt", "r") as f:
    # add all subreddits from text file to filter
    for keyword in f:
        keywords_list.append(keyword.strip().lower())
print(subreddits)
print(keywords_list)

# Create read only instance of Reddit
# Bot1 settings is selected from praw.ini
reddit = praw.Reddit("Bot1", config_interpolation="basic")
subreddit_name="+".join(subreddits)
print(subreddit_name)

subreddit=reddit.subreddit(subreddit_name)
keywords=re.compile(rf"\b{'|'.join(keywords_list)}\b", re.IGNORECASE)

counter=0
for submission in subreddit.stream.submissions():
    if submission==None:
        # print(None)
        # time.sleep(1)
        break
    
    found=keywords.search(submission.title)
    
    if found!=None:
        print(found.expand(fr"Matched on {found.group(0)} \n{submission.title}"))
        time.sleep(1)
   
    else:
        pass
        # # print("Keyword Not Found")
        # time.sleep(1)

    counter+=1
    print(counter)

# for comment in subreddit.stream.comments():
#         if comment==None:
#             print(None)
#             time.sleep(1)
#             break
            
#         elif keyword in comment.body:
#             print(f"{keyword}\n\n{comment.body}")
#             time.sleep(1)
#             break
       
#         else:
#             print("Keyword Not Found")
#             time.sleep(1)
#             break