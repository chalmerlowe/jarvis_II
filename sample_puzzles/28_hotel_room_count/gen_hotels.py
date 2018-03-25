from random import randint

with open('hotels.txt', 'w') as fout:
    num_hotels = 20
    fout.write('{}\n'.format(num_hotels))
    
    for hotel in range(num_hotels):
        num_floors = randint(3, 9)
        num_rooms = randint(4, 88)
        divisor_x = randint(3, 6)
        divisor_y = divisor_x + randint(1, 3)
       
        fout.write('''
{}
{}
{} {}
'''.format(num_floors, num_rooms, divisor_x, divisor_y))
        