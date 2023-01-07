class Polynomial:
    def __init__(self, polynom = None):
        if polynom is not None:
            self.__dict__.update(polynom)
            return
        power = int(input('Введіть ступінь багаточлену: '))
        for each in range(power, -1, -1):
            try:
                self.__dict__.update({str('power' + str(each)): float(input(f'Введіть коефіцієнт при одночлені зі ступенем {each}: '))})
            except:
                self.__dict__.update({str('power' + str(each)): 0})
    
    def count(self, x):
        value = 0
        for each in self.__dict__.keys():
            value += self.__dict__[each] * (x ** int(each[5:]))
        return value
    
    def form(self):
        form = ''
        keys = list(self.__dict__.keys())
        keys.sort()
        keys.reverse()
        for each in keys:
            if self.__dict__[each] == 0:
                continue
            if form != '':
                form += ' + '
            form += '(' + str(self.__dict__[each]) + ')' + ('*x**(' + each[5:] + ')') * int(bool(int(each[5:])))
        return form
    
    def __add__(self1, self2):
        coefficients = {}
        for obj in [self1, self2]:
            for key in obj.__dict__.keys():
                if key not in coefficients.keys():
                    coefficients[key] = obj.__dict__[key]
                else:
                    coefficients[key] += obj.__dict__[key]
        return Polynomial(coefficients)
    
    def __sub__(self1, self2):
        coefficients = self1.__dict__.copy()
        for key in self2.__dict__.keys():
            if key not in coefficients.keys():
                coefficients[key] = 0 - (self2.__dict__[key])
            else:
                coefficients[key] -= self2.__dict__[key]
        return Polynomial(coefficients)
    
    def __mul__(self1, self2):
        coefficients = {}
        for key1 in self1.__dict__.keys():
            for key2 in self2.__dict__.keys():
                new_key = 'power' + str(int(key1[5:]) * int(key2[5]))
                if new_key not in coefficients.keys():
                    coefficients[new_key] = self1.__dict__[key1] * self2.__dict__[key2]
                else:
                    coefficients[new_key] += self1.__dict__[key1] * self2.__dict__[key2]
        return Polynomial(coefficients)

parabole = Polynomial()
print('Значення функції:', parabole.count(float(input('Введіть значення аргументу: '))))
polynom1 = Polynomial()
print(polynom1.form())
polynom2 = Polynomial()
print(polynom2.form())
print((polynom1 + polynom2).form())
print('Значення суми функцій у точці дорівнює:', (polynom1 + polynom2).count(float(input('Введіть значення аргументу: '))))
print('Значення різниці функцій у точці дорівнює:', (polynom2 - polynom1).count(float(input('Введіть значення аргументу: '))))
print('Форма добутку функцій представляється у вигляді y =', (polynom1 * polynom2).form())
print('Значення множення функцій у точці дорівнює:',(polynom1 * polynom2).count(12))