class User:
    login = ""
    password = ""

    def __init__(self, myLogin, myPassword):
        self.login = myLogin
        self.password = myPassword

    def log(self):
        print("Input login: ")
        str1 = input()
        print("Input password: ")
        str2 = input()
        if str1 != self.login or str2 != self.password:
            print("try again")
            self.log()

        return True
