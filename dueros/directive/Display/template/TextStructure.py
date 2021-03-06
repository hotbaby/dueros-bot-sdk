# encoding: utf8


class TextStructure:

    def __init__(self):
        super(TextStructure, self).__init__()
        self.data = {}
        self.set_type('PlainText')

    def set_type(self, structure_type):

        if type:
            self.data['type'] = structure_type

    def set_text(self, text):

        if text:
            self.data['text'] = text

    def get_data(self):

        return self.data
