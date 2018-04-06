class myclass:
    def __init__(self, mystr):
        self.mystr = mystr

    def set_string(self, mystr):
        self.mystr = mystr

    def print_str(self):
        str1 = self.mystr.upper()
        print(str1)

myclass_obj = myclass("Satish Pandey")
myclass_obj.print_str()