import os, requests
from slackclient import SlackClient

SLACK_TOKEN = os.environ.get('SLACK_TOKEN', None)

slack_client = SlackClient(SLACK_TOKEN)


def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call['ok']:
        return channels_call['channels']
    return None


def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None


def user_info(user_id):
    user_info = slack_client.api_call("users.info", user=user_id)
    if user_info['ok']:
        return user_info['user']
    return None

def get_latest_message(channel_id):
    channel_history = slack_client.api_call("channels.history", count = 1, channel=channel_id)
    if channel_history:
        if 'messages' in channel_history:
            return channel_history['messages'][0]
    return None


def get_channel_id_from_name(name):
    channels_ = list_channels()
    if channels_:
        for channel_ in channels_:
            if channel_['name'] == name:
                return channel_['id']
        return "Chanel Not found"
    else:
        print("Unable to authenticate.")


def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='botsco',
        icon_emoji=':bosco:'
    )
    print('message sent')


def trump_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='rage',
        icon_emoji=':trump_rage:'
    )


def paste_bot_message(channel_id, message, username = "Paste Bot", icon_url = None):
    if icon_url is None:
        slack_client.api_call(
            "chat.postMessage",
            channel=channel_id,
            text=message,
            username=username,
            icon_emoji=':clippy:'
        )
    else:
        slack_client.api_call(
            "chat.postMessage",
            channel=channel_id,
            text=message,
            username=username,
            icon_url=icon_url
        )

        
if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for channel in channels:
            print(channel['name'] + " (" + channel['id'] + ")")
            detailed_info = channel_info(channel['id'])
            if detailed_info:
                print('Latest text from ' + channel['name'] + ":")
                # print(detailed_info['latest']['text'])
            if channel['name'] == 'bottest':
                send_message(channel['id'], 'Hello123')
    else:
        print("Unable to authenticate.")
