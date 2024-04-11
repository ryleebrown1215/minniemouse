class Decode:

    def __init__(self, encoded_string):
        self.encoded_string = encoded_string


    def decode(self, encoded_string):
        original_string = ''

        for i in encoded_string:
            i -= 3
            original_string += i

        return original_string
