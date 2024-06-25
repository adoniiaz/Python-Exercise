import os
import numpy

'''
Question 1
Write a program that requests five names separated by commas and create a
list containing those names. Print your answer.
For example James,Alison,Fred,Sally,Matthew
should return ['James','Alison','Fred','Sally','Matthew']

names=input('Enter the names separated by comma. \n>>>')
names=names.split(',')
print(names)
'''

'''
Question 2
Can you write a short program that will print out the version of Python
that you are using?
'''
'''
Question 4
Write a program that takes a list of non-negative integers and prints each integer
to the screen the same number of times as the value of the integer, each new value
on a new line. For example
[2,3,4,1] would print:
22
333
4444
1

def print_em(number):
    for i in range(len(number)):
        print('')
        for j in range(number[i]):
            print(number[i], end='')

print_em([2,3,4,1])
'''
'''
Question 6
Write a program that will return the sum of the digits of an integer.

def adder(number):
    sum=0
    if isinstance(number, int):
        new_num=str(number)
        new_num=list(new_num)
        for i in range(len(new_num)):
            sum+=int(new_num[i])
    else:
        new_num=list(number)
        for i in range(len(new_num)):
            sum+=int(new_num[i])
    return sum
adding=adder(16532)
print(adding)
'''

'''
Question 7
Write a program that converts text into pig latin. Pig latin works as follows:
All letters before initial vowel are placed at the end of the word and then 'ay'
is added (explanation adapted from Wikipedia), so pig becomes igpay, cat becomes
atcay, potential becomes otentialpay etc.

def pig_latin(word):
    vowels=['a','e','i','o','u']
    if word[0] in vowels:
        return word + 'ay'
    for i in range(len(word)):
        if word[i] in vowels:
            return word[i:] + word[:i] + 'ay'
    return word + 'ay'

pigging=pig_latin('mcrdc')
print(pigging)

'''
'''
Question 8
Write a function that will check for the occurrence of double letters in
a string. If the string contains double letters next to each other it
will return True, otherwise it will return False.

def repiteition(word):
    for i in range(len(word)-1):
        if word[i]== word[i+1]:
            return word[i], word[i+1]
    return False

check=repiteition('darrik')
print(check)
'''
'''
Question 9
Write a function that will check if a string is a palindrome.

def palindrome(word):
    if word[::-1]==word:
        return 'Plaindrome'
    return 'not Palindrome'
checking=palindrome('Adoni')
print(checking)
    '''

'''
Question 10
Write a function def add_commas(numbers) that will add commas to an integer and return it as a string.
For example add_commas(1000000) will return 1,000,000 Do it first without using string fomratting
or f strings.

def addcomma(number):
    num=str(number)
    reversed=num[::-1]
    new_numb=[]
    for i in range (0,len(reversed),3):
        new_numb.append(reversed[i:i+3])

    commaed=','.join(new_numb[::-1])

    return commaed
check=addcomma(100000)
print(check)

def convert_to_binary(number):
    quotient=1
    remainder=[]
    while number!=0:
       
        remainder.append(str(number%2))
        number=number//2
    binary=''.join(remainder)
    binary=binary[::-1]
    return binary

checking=convert_to_binary(65)
print(checking)


def sum_of_integer(number):
    sum=0
    #for i in range(number+1):
        #sum+=i
    sum=number*(number+1)/2
    return sum

check=sum_of_integer(10)
print(check)
'''



