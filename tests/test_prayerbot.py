#-*- encoding: utf-8 -*-
import json
import unittest

from prayer import PrayerWebhook

class MessengerBotTestSuite(unittest.TestCase):

    def test_prayer_bot_recipent(self):
        sender_id = '10'
        message = {'text': 'helpppppp'}
        res = json.loads(PrayerWebhook.handle_message(sender_id, message))
        assert res['recipient']['id'] == '10'
        assert json.loads(res['message'])['text'] == u"Niestety Cię nie rozumiem.\nWpisz 'pomoc' żeby uzyskać dodatkowe informacje."
