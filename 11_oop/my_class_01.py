# * Create a class called `Animal`
# * Inside the class create an attribute of `fur_color` and assign it an empty string
# * Define two methods for your class:
#   * a method called `set_fur_color` that takes in a parameter and assigns that to `fur_color`
#   * a second method called `print_fur_color` that prints the value associatd with `fur_color`


class Animal:
    fur_color = ''
    
    def set_fur_color(self, color):
        self.fur_color = color
        
    def print_fur_color(self):
        print(self.fur_color)
        
print('script loaded')