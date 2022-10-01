# -*- coding: utf-8 -*-

#Section 3.1

#8. Describe an algorithm that takes as input a list of n distinct integers and finds the location of the largest even integer in the list or returns 0 if there are no even integers in the list. 

import random

def fill_list_of_integers(number_of_integers):
    list_of_integers = []
    for number in range(0, number_of_integers):
        new_number = random.randint(0,22)
        list_of_integers.append(new_number)
    return list_of_integers

def find_largest_even_integer(list_of_integers):
    sorted_list_of_integers = list(sorted(list_of_integers))

    check_number = number_of_integers - 1
    while check_number >= 0:
        if 0 == sorted_list_of_integers[check_number] %2:
            largest_even_number = sorted_list_of_integers[check_number]
            largest_location = check_number - 1
            break
        else:
            check_number -= 1
    if check_number == -1:
        largest_even_number = -1
    return largest_even_number

if __name__ == "__main__":
    number_of_integers = 5
    
    list_of_integers = fill_list_of_integers(number_of_integers)
    print(f"The list of integers is: {list_of_integers}")
    
    largest_even_integer = find_largest_even_integer(list_of_integers)
    
    if largest_even_integer == -1:
        print("There are no even numbers.")

    location = 1
    for number in list_of_integers:
        if number == largest_even_integer:
            print(f"The largest even number is {largest_even_integer}, and its location is {location}.")
        else:
            location += 1