#!/usr/local/bin/python
import json
import matplotlib.pyplot as pl
import urllib2
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
with open('/Users/sankarshanmudkavi/bcheck/auth_tokens.json') as auth_file:
    json_auth_tokens = json.load(auth_file)
account_sid = json_auth_tokens['account_sid']
auth_token = json_auth_tokens['auth_token']
client = TwilioRestClient(account_sid, auth_token)


def send_sms():
    message = client.sms.messages.create(body="It's zero!",
                                         to=json_auth_tokens['to'],
                                         # Replace with your phone number
                                         from_=json_auth_tokens['from'])
                                         # Replace with your Twilio number


def bitcoin_price():
    json_obj_url = urllib2.urlopen(
        'http://blockchain.info/charts/market-price?format=json')
    json_obj = json.loads(json_obj_url.read())
    value_list = [[lists['x'], lists['y']]
                  for keys in json_obj for lists in json_obj[keys]]

    derivative_list = [(value_list[nums][0], (value_list[nums + 1][1] - value_list[nums][1]) / (value_list[nums + 1][0] - value_list[nums][0]) * 10 ** 5)
                       for nums in range(len(value_list) - 1)]

    if derivative_list[len(derivative_list) - 1][1] <= 0:
        send_sms()

    plot_list = zip(*derivative_list)
    plot_list_1 = zip(*value_list)
    pl.plot(plot_list_1[0], plot_list_1[1])
    pl.plot(plot_list[0], plot_list[1])
    pl.savefig('/Users/sankarshanmudkavi/bcheck/PriceGraph.png')

bitcoin_price()
