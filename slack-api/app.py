import logging
import os
import re

# Use the package we installed
from chalice import Chalice, Response
from dotenv import find_dotenv, load_dotenv
from slack_bolt import App
from slack_bolt.adapter.aws_lambda.chalice_handler import \
    ChaliceSlackRequestHandler

load_dotenv(find_dotenv())

# Initializes your app with your bot token and signing secret
bolt_app = App(
    process_before_response=True,
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)


@bolt_app.command("/start")
def respond_to_slack_within_3_seconds(ack):
    ack("one sec!")


@bolt_app.message(re.compile("."))
def say_some(message, say):
    user = message["user"]
    content = message["text"]
    print(message, flush=True)
    say(f"This *{content}* message is a little harsh, <@{user}>!")


ChaliceSlackRequestHandler.clear_all_log_handlers()
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)


app = Chalice(app_name="philia-slack")
slack_handler = ChaliceSlackRequestHandler(app=bolt_app, chalice=app)


@app.route(
    "/slack/events",
    methods=["POST"],
    content_types=["application/x-www-form-urlencoded", "application/json"],
)
def events() -> Response:
    return slack_handler.handle(app.current_request)


@app.route("/slack/install", methods=["GET"])
def install() -> Response:
    return slack_handler.handle(app.current_request)


@app.route("/slack/oauth_redirect", methods=["GET"])
def oauth_redirect() -> Response:
    return slack_handler.handle(app.current_request)
