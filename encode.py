class Encoder:
    def __init__(self, password):
        self.password = password

    def encode(self):
        new_password = ""
        for char in self.password:
            new_password += str(int(char) + 3)
        return new_password
