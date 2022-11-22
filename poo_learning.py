# create class, atributes, constructor method, methods,
# creating objects, __dict___

class Cats:
    nr_of_cats = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.foods = []
        self.left_lives = 9
        Cats.nr_of_cats += 1

    def life_stage(self):
        if self.age > 3:
            print(self.name, 'is an adult cat')
        else:
            print(self.name, 'is a puppy cat')

    def is_fav_food(self, food):
        return food in self.foods

    def dies(self):
        self.left_lives -= 1
        print('{} dies, from now it has {} lives left'.format(self.name,self.left_lives))

p = Cats('Alastor', 1)
p.foods = ['fish','milk','tuna']
p.foods.append('cereals')
b = Cats('Gaspar', 4)

print(p.life_stage())
print(b.life_stage())

print(p.__dict__)

p.dies()
p.dies()
p.dies()

p.nr_of_cats = 5
#changing an atribute from just an object
print(Cats.nr_of_cats)
print(p.nr_of_cats)
print(b.nr_of_cats)

print(p.__dict__)