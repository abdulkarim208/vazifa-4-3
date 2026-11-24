class Kitob:
    def __init__(self, nomi, muallif,):
        self.nomi = nomi
        self.muallif = muallif
        self.__ijarada = False

    def ijaraga_ber(self):
        if not self.__ijarada:
            self.__ijarada = True
            print("Kitob ijaraga berildi")
        else:
            print("Kitob ijarada!")

    def qaytarish(self):
        if self.__ijarada:
            self.__ijarada = False
            print("Kitob kutubxonaga qaytarildi")
        else:
            print("Kitob kutubxonada!")

    def holat(self):
        if self.__ijarada:
            print("Kitob ijarada.")
        else:
            print("Kitob kutubxonada.")


k = Kitob("Otkan kunlar", "Abdulla Qodiriy")

k.ijaraga_ber()
k.holat()
k.qaytarish()