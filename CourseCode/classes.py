class PrivateClass:
    def __int__(self, p):
        self.public_data = p
        # self.__private_data = pri

    @property
    def getPub(self):
        return self.public_data