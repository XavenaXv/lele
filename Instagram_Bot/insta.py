from instapy import InstaPy
from instapy.util import smart_run

# Initialize InstaPy session
session = InstaPy(username="nyxora", password="878127evanrevan")

# Define the users whose stories you want to view
users_to_view_stories = ["mkplw"]

# Start a smart run to interact with stories
with smart_run(session):
    for user in users_to_view_stories:
        # View stories from the specified user
        session.story_by_users([user], amount=1, random_order=True, interact=False)

# End the session
session.end()