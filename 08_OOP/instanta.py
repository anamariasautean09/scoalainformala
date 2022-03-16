class Rata:

    ochi = 2

    def __init__(self, inaltime, greutate, gen):
        self.inaltime = inaltime
        self.greutate = greutate
        self.gen = gen

    def merge(self):
        pass

    def macane(self):
        return "MAC-MAC"

rata1 = Rata(inaltime=10, greutate=3.4, gen="femeiesc")
rata2 = Rata(inaltime=20, greutate=5, gen="barbatesc")

print(Rata.ochi)
print(rata1.macane())
