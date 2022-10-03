# -*- coding: utf-8 -*-

#9. A palindrome is a string that reads the same forward and backward. Describe an algorithm for determining whether a string of n characters is a palindrome.

user_string = input()
reverse_string = user_string[::-1]

if user_string == reverse_string:
    print('That is a palindrome!')
    print('{user_string} = {reverse_string}')
else:
    print('That is not a palindrome.')
    print('{user_string} is not the same as {reverse_string}')