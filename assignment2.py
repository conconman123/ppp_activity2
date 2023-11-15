#Write a Python function called max_num()to find the maximum of three numbers.
def max_mun(a, b, c):
    maximun = max(a, b, c)
    print(maximun)
    return maximun

max_mun(3, 8, 5)

#Write a Python function called mult_list() to multiply all the numbers in a list.

def multi_list(num):
    value = 1
    for i in num:
        value *= i
    print(value)
    return value

multi_list([3, 7, 4])

#Write a Python function called rev_string() to reverse a string.

def rev_string(string):
    reversed = string[::-1]
    print(reversed)
    return reversed

rev_string("Hello World")

#Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(a, x, y):
    if a > x & a < y:
        return True
    else:
        return False
    
num_within(3 , 1, 6)
num_within(6, 2, 4)

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    def next_row(row):
        result = [1]
        for i in range(1, len(row)):
            result.append(row[i-1] + row[i])
        result.append(1)
        return result
    row = [1]
    for x in range(n):
        print(row)
        row = next_row(row)

pascal(12)