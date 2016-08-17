from flask import Flask, request, Response, jsonify
from flask_slack import Slack
from url_parser import *
from app import *

app = Flask(__name__)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')
SLACK_RAGE_BOT = os.environ.get('SLACK_RAGE_BOT')
SLACK_BOSCO_BOT = os.environ.get('SLACK_BOSCO_BOT')
SLACK_COPY_BOT = os.environ.get('SLACK_COPY_BOT')

@app.route('/paste', methods=['POST'])
def PASTE():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        channel_id = get_channel_id_from_name(channel)
        message = request.form.get('text')[5:]
        username = "paste bot"
        paste_bot_message(channel_id=channel_id, message=message, username=username)
        return Response(), 200


@app.route('/copy', methods=['POST'])
def COPY():
    if request.form.get('token') == SLACK_COPY_BOT:
        username = request.form.get('user_name')
        message = request.form.get('text').encode('utf-8')
        channel = request.form.get('channel_name')
        channel_id = get_channel_id_from_name(channel)
        previous_message_data = get_latest_message(channel_id)
        message = previous_message_data['text']
        user = previous_message_data['user']
        return 'Message Copied!'


@app.route('/rage', methods=['POST'])
def RAGE():
    if request.form.get('token') == SLACK_RAGE_BOT:
        user = request.form.get('user_name')
        channel = request.form.get('channel_name')
        channel_id = get_channel_id_from_name(channel)
        message = "@{}: {}".format(user, message_to_upper(request.form.get('text').encode('utf-8')))
        trump_message(channel_id=channel_id, message=message)
    return Response(), 200


@app.route('/botsco', methods=['POST'])
def BOTSCO():
    if request.form.get('token') == SLACK_BOSCO_BOT:
        channel = request.form.get('channel_name')
        channel_id = get_channel_id_from_name(channel)
        send_message(channel_id=channel_id, message=request.form.get('text'))
        print("{} took over Botsco and said: {}".format(request.form.get('user_name'), request.form.get('text')))
        return Response(), 200


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')


if __name__ == "__main__":
    app.run(debug=True)
