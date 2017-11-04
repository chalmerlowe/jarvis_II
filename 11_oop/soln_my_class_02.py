# * Create a class called `Car`
# * Define an `__init__()` method that takes a two parameters and assigns them to `color` and `mpg` (miles per gallon) attributes respectively
# * Define a method called `set_color` that takes in a parameter and assigns that to `color`
# * Define a method called `print_specs` that prints the values associatd with `color` and `mpg`
# * Create an object based on your class.

class Car:
    def __init__(self, color, mpg):
        self.color = color
        self.mpg = mpg
        
    def set_color(self, color):
        self.color = color
    
    def print_specs(self):
        print('Your ca is {} and has a mpg of: {}'.format(self.color, self.mpg))

c = Car('red', 42)        
        
print('script loaded')