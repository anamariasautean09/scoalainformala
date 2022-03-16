import datetime


class Validator:
    def __init__(self, cnp):
        self.CNP = cnp

    def Lungime(self):
        if len(self.CNP) != 13:
            return False
        return True

    def Sex(self):
        s = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if self.Sex in s:
            return False
        return True

    def Date(self):
        try:
            date = self.CNP[1:7]
            if datetime.datetime.strptime(date, "%y%m%d"):
                return True
        except ValueError:
            return False

    def Judet(self):
        jud = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
               '17','18','19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
               '33', '34', '35','36','37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '51', '52']
        if self.CNP[7:9] in jud:
            return True
        return False

    def NNN(self):
        n1 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        n2 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        n3 = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        if self.CNP[9] in n1 and self.CNP[10] in n2 and self.CNP[11] in n3:
            return True
        return False

    def cifcontrol(self):
        intcnp = int(self.CNP[-1])
        val = '279146358279'
        cnpc = 0
        for i, v in enumerate(val):
            cnpc += int(v) * int(self.CNP[i])
        rest = cnpc % 11
        if rest == 10:
            rest = 1
        else:
            rest = rest
        if intcnp == rest:
            return True
        return False

    def format(self):
        if self.CNP.isdigit():
            return True
        return False

    def __str__(self):
        if self.Lungime() and self.Sex() and self.Date() and self.Judet() and self.NNN() and self.cifcontrol() and self.format() is True:
            return f'CNP: {self.CNP} este valid.'
        return f'CNP: {self.CNP} nu este valid.'

cnp_input = input('Introdu CNP: ')
obiect_1 = Validator(cnp_input)
print(obiect_1)