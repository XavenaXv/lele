from instabot import Bot
import time

# Initialize the bot
bot = Bot()
bot.login(username="nyxora", password="878127evanrevan")

# Search for a user whose stories you want to view
user_to_interact_with = "mpklw"
user_id = bot.get_user_id_from_username(user_to_interact_with)

# Get user's story reel ID
story_reel_id = bot.get_user_stories(user_id)
if not story_reel_id:
    print(f"No stories found for user {user_to_interact_with}")
else:
    # View stories
    bot.view_user_stories(user_id, story_reel_id)

    # Interact with stories (like and reply)
    for story in bot.get_user_stories(user_id, story_reel_id):
        story_id = story["id"]
        bot.like_story(story_id)  # Like the story
    # Wait for a while to simulate a user's interaction
    time.sleep(10)

# Logout
bot.logout()
