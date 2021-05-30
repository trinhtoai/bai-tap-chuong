class Nguoi:
    def __init__(self):
        pass
    def getGender(self):
        pass
class Nam(Nguoi):
    def getGender(self):
        print('Nam')
class Nu(Nguoi):
    def getGender(self):
        print('Nu')
a=Nam()
a.getGender()
b=Nu()
b.getGender()
