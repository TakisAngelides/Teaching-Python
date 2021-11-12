# -------------------------------------------------------------------------------------------------------------------

# 1

# Define a class Disease and give it an attribute called name. Define a second class called Pandemic and make its
# constructor create 5 Disease objects that stores in a list.

# -------------------------------------------------------------------------------------------------------------------

# 2

# Define a class called Animal and give it your own attributes and functions. The create a class Bird that inherits
# the Animal class and give it your own attributes and functions. Make an example of polymorphism for one of the functions
# in the Animal class for which the Bird class overwrites.

# -------------------------------------------------------------------------------------------------------------------

# 3

# Make a class called Planet and give it an attribute called name and an attribute called mass. Then make a class called
# Solar_System and make its constructor create all the planets in our solar system which will be of class type Planet.
# Store these planets in a list when you create them in the constructor of the Solar_System class.

# Hint: Here is a list of the planet names and masses in Earth mass units:

# ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# [0.0553, 0.815, 1, 0.1075, 317.8, 95.2, 14.6, 17.2]

# -------------------------------------------------------------------------------------------------------------------










# Solutions:

# -------------------------------------------------------------------------------------------------------------------

# 1

class Disease():

    def __init__(self, name):

        self.name = name

class Pandemic():

    def __init__(self):

        self.spread_list = [] # In this list we will store the 5 Disease objects.

        for i in range(5):

            self.spread_list.append(Disease('Covid')) # I create a Disease object by calling Disease('...') and put it in the list using the append function attributed to lists


# Example

pandemic = Pandemic()

pandemic_list = pandemic.spread_list # this is the attribute of the Pandemic class which is a list

name_of_first_disease = pandemic_list[0].name # this is the attribute of the Disease class which is a string

# -------------------------------------------------------------------------------------------------------------------

# 2

class Animal():

    def __init__(self, name, number_of_legs, mass, colour):

        self.name = name
        self.legs = number_of_legs
        self.mass = mass
        self.colour = colour

    def fly(self):

        print(f'The {self.name} is flying.')

    def swim(self):

        print(f'The {self.name} is swimming.')

class Bird(Animal): # Bird class inherits Animal class

    def swim(self): # Polymorphism

        print('Some birds cannot swim.')

# -------------------------------------------------------------------------------------------------------------------

# 3

class Planet():

    def __init__(self, name, mass):

        self.name = name
        self.mass = mass

class Solar_System():

    def __init__(self):

        self.planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

        self.planet_masses = [0.0553, 0.815, 1, 0.1075, 317.8, 95.2, 14.6, 17.2]

        self.planets_list = []

        for i in range(len(self.planet_names)):

            self.planets_list.append(Planet(self.planet_names[i], self.planet_masses[i]))

# Example

ss = Solar_System()

planets_list = ss.planets_list

print(planets_list[0].name, planets_list[0].mass)

# -------------------------------------------------------------------------------------------------------------------