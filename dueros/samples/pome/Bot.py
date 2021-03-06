# encoding: utf8

from dueros.Bot import Bot
from dueros.card.TextCard import TextCard
import json


class Bot(Bot):
    def launchRequest(self):
        return {
            'card': TextCard(r'欢迎使用家居控制!请告诉我您要查找什么智能设备，比如查找我的空调'),
            'outputSpeech': r'<speak>欢迎使用家居控制!请告诉我您要查找什么智能设备，比如查找我的空调</speak>'
        }

    def intentRequest(self):
        self.ask('deviceName')

        card = TextCard('您要查找什么智能设备呢? 比如"查找我的空调"')
        card.add_cue_words("百度")
        card.add_cue_words("百度")
        card.add_cue_words("百度")
        card.set_anchor("http://www.baidu.com", "百度")
        return {
            'card': card,
            'outputSpeech': '<speak>您要查找什么智能设备呢? 比如"查找我的空调"</speak>'
        }

    def controlRequest(self):
        self.ask('deviceName')
        # deviceName = self.getSlots('deviceName')
        # print('deviceName %s' % (deviceName))
        return {
            'card': TextCard('请告诉您的指令，比如调小空调风速、设置温度为30度'),
            'outputSpeech': '请告诉您的指令，比如调小空调风速、设置温度为30度'
        }

    def __init__(self, data):
        super(Bot, self).__init__(data)

        self.add_launch_handler(self.launchRequest)

        self.add_intent_handler('ai.dueros.common.default_intent', self.controlRequest)

        self.add_intent_handler('dueros.device_interface.smart_device.search', self.intentRequest)
    pass
