import os
import re

from dotenv import find_dotenv, load_dotenv
# Use the package we installed
from slack_bolt import App

load_dotenv(find_dotenv())

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)

@app.message(re.compile("."))
def say_some(message, say):
    user = message['user']
    content = message["text"]
    print(message, flush=True)
    say(f"This *{content}* message is a little harsh, <@{user}>!")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
