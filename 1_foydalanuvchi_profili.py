class Foydalanuvchi:
    def __init__(self, ism, username, parol):
        self.ism = ism
        self.username = username
        self.__parol = parol

    def parolni_ozgartir(self, eski_parol, yangi_parol):
        if self.__parol == eski_parol:
            self.__parol = yangi_parol
            print("Parol muvaffaqiyatli ozgartirildi")
        else:
            print("Eski parol notogri!")

    def tekshir(self, parol):
        if self.__parol == parol:
            print("Parol togri")
        else:
            print("Parol notogri!")


user = Foydalanuvchi("Ali", "ali_01", "abc123")
user2 = Foydalanuvchi("Vali", "vali_02", "123456")

user.tekshir("abc123")
user.parolni_ozgartir("abc123", "new456")
user.tekshir("new456")

user2.tekshir("123456")
user2.parolni_ozgartir("123456", "654321")
user2.tekshir("654321")