# -*- coding: utf-8 -*-

#Section 3.1 

#7. Describe an algorithm that takes as input a list of n integers and finds the location of the last even integer in the list or returns 0 if there are no even integers in the list.  
import random

def fill_list_of_intergers():
    list_of_intergers = []
    for number in range(0, number_of_intergers):
        new_number = random.randint(0,22)
        list_of_intergers.append(new_number)
    return list_of_intergers

def find_last_even_integer(list_of_intergers):
    last_location = 0
    #reverse list as we are only looking for last even number_of_intergers
    list_of_intergers.reverse()
    print(f'The reversed list of intergers is: {list_of_intergers}')
    #Check if even
    location = 0
    check_location = 0
    for check_number in list_of_intergers:
        if 0 == check_number % 2:
            print('You found an even!')
            print(f'Check location was {check_location}')
            location = len(list_of_intergers) - check_location - 1
            print(f'Our actual location was {location}')
        else:
            check_location += 1

        return location

if __name__ == '__main__':
    number_of_intergers = 5
    list_of_intergers = []

    list_of_intergers = fill_list_of_intergers()
    print(f'Your list of intergers was {list_of_intergers}')

    location= find_last_even_integer(list_of_intergers)
    print(f'The location of the last even was {location}.')