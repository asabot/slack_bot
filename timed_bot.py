from flask import Flask, request, Response, jsonify
from flask_slack import Slack
from app import *
import schedule, time


def bosco_time(message):
    channel = 'random'
    channel_id = get_channel_id_from_name(channel)
    send_message(channel_id=channel_id, message=message)
    print("Botsco just said: {}".format(message))


def bosco_init():
    schedule.every().monday.at("13:13").do(bosco_time, "it's an interesting moment")
    schedule.every().tuesday.at("16:00").do(bosco_time, "cool dialogue - talk more soon.")
    schedule.every().wednesday.at("17:15").do(bosco_time, "galactic oportunity for Cisco right now")
    schedule.every().thursday.at("14:15").do(bosco_time, "it's an interesting moment")
    schedule.every().friday.at("21:00").do(bosco_time, "need to yak - buzz when free.")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    print("Timed bot initiated")
    bosco_init()
