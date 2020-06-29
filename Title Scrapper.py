import praw

# Create read only instance of Reddit
# Bot1 settings is selected from praw.ini
reddit = praw.Reddit("Bot1", config_interpolation="basic")
