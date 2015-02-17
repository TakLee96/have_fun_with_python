class Acount:
    num_of_accounts = 0
    def __init__(self, id):
        self.id = id
        Acount.num_of_accounts += 1
    def register(self, student):
        self.student = student
        print("Register" + student)
    @property
    def type(self):
        return type(self)
