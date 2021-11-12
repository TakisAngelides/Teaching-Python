class Ball():

    def __init__(self, size, c): # self is the object we are creating with this blueprint when we call Ball() and the constructor runs

        self.size = size # on the left hand side are the object's attributes and on the right hand side the values of those attributes given as input
        self.colour = c

    def bounce(self): # self - which is any instance of the Ball class - is always given as an implicit input to the functions and the constructor defined within a class

        print(f'The ball has size {self.size} and colour {self.colour} and can bounce.')


ball_1 = Ball(size = 3, c = 'red')

ball_2 = Ball(2, 'yellow')

s = ball_1.size

print(s)

ball_1.bounce()

class Person():

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def get_name(self):

        print(self.name)

    def expertise_level(self, age_started_job):

        print('Teacher expertise level: ', self.age - age_started_job)
        # print(f'Teacher expertise level: {self.age - age_started_job}') # same as line above


class Student(Person): # Inheritance - Student class inherits all the attributes and functions of Person class

    def expertise_level(self, age_started_job = None):

        # Polymorphism - the same function name used in the subclass does something different to original function
        # in parent class because original function does not quite fit the student concept

        print('The student has not started a job yet.')


class Teacher(Person):

    pass


student_1 = Student('Luffy', 17)

a = student_1.age

print(a)

student_1.get_name()

teacher_1 = Teacher('Franky', 40)

teacher_1.expertise_level(25)

student_1.expertise_level()

