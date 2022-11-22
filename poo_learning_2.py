# subclass, superclass, inheritance
# https://www.youtube.com/watch?v=iliKayKaGtc
class employee:
    def __init__(self, name, age, code, pay):
        self.name = name
        self.age = age
        self.code = code
        self.base_payment = pay

    def calculate_payment(self, discounts, bonus):
        return self.base_payment-discounts+bonus

class selling_agent(employee):
    def __init__(self, name, age, code, pay, show):
        self.show_number = show
        super().__init__(name, age, code, pay)

class crewman(employee):
    def renew_license(self):
        if self.age < 50:
            print('Renew license each year')
        else:
            print('Renew license each 6 months')

p = selling_agent('Juan Narváez',32,'A0OCF3',500,6)
print(p.calculate_payment(150,17))
print(p.show_number)
#clase selling_agent hereda el método calculate_payment
q = crewman('Lucas Betancur',56,'A0OCT4',300)
print(q.calculate_payment(150,17))
print(q.renew_license())
#clase crewman hereda el método constructor de employee
