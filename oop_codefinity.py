# oop_codefinity.py


class Cat:
  # attribute
  name = 'Kitty'
  age = 2

  # method; Each method obligatory contains parameter self: this is a reference to the current object.
  def say_meow(self):
    print('Meow')
    
  def sleep(self): 
    print('Cat is sleeping')

# object creating
cat = Cat()
cat.sleep() 	# calling the method


print('\n _________')
class Cat:
  age = 1
  name = 'Kitty'
  weight = 0.5
  def __init__(self, name='Chicco', age='4'): 
    """ Constructor is a special method, which is automatically called during object creating. 
    #This method is not obligatory to define, the object can be created with the constructor that is generated automatically, 
    # as we did it before actually. For the default constructor, there is no need to write it. But sometimes you need to specify your 
    # constructor.""" 
    self.name = name
    self.age = age
  def say_meow(self):
    print(f'Cat named {self.name} is {self.age} yrs old. Meow!')
  def set_age(self, new_age):
    self.age = new_age
    print(self.name, 'is', self.age, 'yrs old now.')
  def run(self, kms):
    """Decreases the weight of the cat. """
    new_weight = self.weight - 0.1 * kms
    print(f'New weight is {new_weight}')
   

cat = Cat()
cat.say_meow()
cat.set_age(13)
cat.run(2)
littleCat = Cat('Bella', 2)
bigCat = Cat('Charlie', 12)
myCat = Cat()
print("Little cat's attributes:", littleCat.name, littleCat.age)
print("Big cat's attributes:", bigCat.name, bigCat.age)
print('My cats attributes:', myCat.name, myCat.age)



# 2) private and public concept: 
class Cat:
  def __init__(self, name='Kitty', age = 1):
    self.name = name
    self.__age = age
    self.__number_of_legs = 4 # this is private

cat = Cat('Maggie', 3)
# print(cat.__age) # AttributeError: 'Cat' object has no attribute '__age'
print(cat._Cat__age)    # way to access even the private value

# 2.1) private
class Dog:
  # set default values as: Puppy for name, 1 for weight, True for happy
  
  def __init__(self, happy=True):
    self.__weight = 1
    self.__name = 'Puppy'
    self.happy = happy


dog = Dog()
print('name:', dog._Dog__name)
print('weight:', dog._Dog__weight)
print('happy:', dog.happy)


# 2.2) Get and Set methods:
class Cat:
  def __init__(self, name='Kitty', age = 1):
    self.name = name
    self.__age = age
    self.__children = 0

  def get_children(self): 
    return self.__children
  
  def set_children(self, children): 
    if isinstance(children, int) and 0<=children<=20: 
      self.__children = children
    else: 
      print('Invalid value of attribute.')


cat = Cat('Penny', 23)
# setting wrong value of attribute
cat.set_children('eight')

# setting correct value of attribute
cat.set_children(3)
print(cat.get_children())

