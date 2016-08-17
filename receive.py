from flask import Flask, request, Response, jsonify
from flask_slack import Slack
from url_parser import *
from app import *

app = Flask(__name__)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')
SLACK_RAGE_BOT = os.environ.get('SLACK_RAGE_BOT')
SLACK_BOSCO_BOT = os.environ.get('SLACK_BOSCO_BOT')


@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        channel_id = get_channel_id_from_name(channel)
        message = request.form.get('text')[5:]
        send_message(channel_id=channel_id, message=message)
        return Response(), 200


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
