'''
encapsulamiento, ocultamiento
abstracción (abc.py abstract base classes)
https://www.youtube.com/watch?v=aj4PEXq0zuc
polimorfismo y sobreescritura, (protocolo)
'''

class career:
    def __init__(self, name):
        self.name = name
        self.__subject = {}

    def add_subject(self, subject, code):
        self.__subject[code] = subject
    # se define un método que agrega materias
    # independiente de cómo se estén almancenando

class subject:
    def __init__(self, name, teacher, year):
        self.name = name
        self.teacher = teacher
        self.start_date = year

    @property #debe llamarse
    def start_date(self):
        print("Prueba")
        return self._start_date #(privado/público ?)

    @start_date.setter #método llamado a través de la creación de un atributo
    def start_date(self, year):
        if year < 2010:
            self._start_date = 2010
        else:
            self._start_date = year

ing = career('Ingeniería')
alg = subject('Álgebra', 'Ricardo Restrepo',2016)
fis = subject('Física', 'Martín Jiménez', 2017)
qui = subject('Química', 'Lorena Ríos', 2005)

ing.add_subject(alg,142)
copy = ing._career__subject
copy[510] = qui
print(copy)
# print(ing.__subject)
print(ing._career__subject)
# print(type(copy))

# print(qui.__dict__)
# print(qui.start_date)
# print(alg.__dict__)
