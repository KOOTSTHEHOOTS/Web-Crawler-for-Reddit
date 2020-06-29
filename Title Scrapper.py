import praw

#subreddits to crawl
subreddits=[]

with open("Subreddits.txt", "r") as f:
    # add all subreddits from text file to filter
    for subreddit in f:
        subreddits.append(subreddit.strip())
        
print(subreddits)
# Create read only instance of Reddit
# Bot1 settings is selected from praw.ini
reddit = praw.Reddit("Bot1", config_interpolation="basic")

