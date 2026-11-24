class Avtomobil:
    def __init__(self, model):
        self.model = model
        self.__eshikOchiq = False

    def eshikni_och(self):
        if not self.__eshikOchiq:
            self.__eshikOchiq = True
            print("Eshik ochildi")
        else:
            print("Eshik ochiq!")

    def eshikni_yop(self):
        if self.__eshikOchiq:
            self.__eshikOchiq = False
            print("Eshik yopildi")
        else:
            print("Eshik yopiq!")

    def holat(self):
        if self.__eshikOchiq:
            print("Eshik ochiq")
        else:
            print("Eshik yopiq")


m = Avtomobil("Chevrolet Cobalt")

m.eshikni_och()
m.holat()
m.eshikni_yop()