# encoding: utf8

import unittest
from dueros.directive.Display.template.BodyTemplate3 import BodyTemplate3


class BodyTemplate3Test(unittest.TestCase):

    '''
    bodyTemplate测试
    '''

    def setUp(self):
        self.template = BodyTemplate3()
        self.template.set_plain_content('test')
        self.template.set_image('http://www.baidu.com')
        self.template.set_background_image('http://www.baidu.com')
        self.template.set_token('0c71de96-15d2-4e79-b97e-e52cec25c254')

    def testGetData(self):
        '''
        测试getData
        :return:
        '''

        data = self.template.get_data()
        ret = {
            'type': 'BodyTemplate3',
            'token': '0c71de96-15d2-4e79-b97e-e52cec25c254',
            'content': {
                'type': 'PlainText',
                'text': 'test'

            },
            'image': {
                'url': 'http://www.baidu.com'
            },
            'backgroundImage': {
                'url': 'http://www.baidu.com'
            }
        }

        self.assertEqual(data, ret)
    pass
