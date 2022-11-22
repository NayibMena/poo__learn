'''
encapsulamiento, ocultamiento, abstracción
https://www.youtube.com/watch?v=iliKayKaGtc

(abc.py abstract base classes)
polimorfismo, (protocolo)
'''

class career:
    def __init__(self, name):
        self.name = name
        self.subject = {}

    def add_subject(self, subject, code):
        self.subject[code] = subject
        
class subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

ing = career('Ingeniería')
alg = subject('Álgebra', 'Ricardo Restrepo')
fis = subject('Física', 'Martín Jiménez')
qui = subject('Química', 'Ana María Cardona')

print(qui.teacher)