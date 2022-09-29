"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
"""Websites used for syntax:
https://www.w3schools.com/python/python_for_loops.asp  
https://www.w3schools.com/python/python_lists_methods.asp  
https://www.w3schools.com/python/python_conditions.asp
https://www.w3schools.com/python/python_while_loops.asp
"""

   
def primes(number_of_primes):
    list=[]
    count=2
    while number_of_primes!=0:
        for i in range(2,count):
            if(count%i==0):
                break
        else:
            list.append(count)
            number_of_primes-=1
        count+=1
    return list


print(primes(10))