"""
#Operators
arithematic ( +, -, *, /, %, **->exp, //->floor division>whole number in return not decimal)
assignment
comparson
logical


"""
#exponential
#x = 2**3  # 2^3

#print(x)

#modulus ->  arithmetic operator
#even/dd
#cyclic rotation
#print(5 % 2)
# 5 - 2 = 3
# 3 - 2 = 1 ->ans

"""
#cyclic rotation
print("0 % 3 = ", (0 % 3))
print("1 % 3 = ", (1 % 3))
print("2 % 3 = ", (2 % 3))
print("3 % 3 = ", (3 % 3))
print("4 % 3 = ", (4 % 3))
print("5 % 3 = ", (5 % 3))
print("6 % 3 = ", (6 % 3))
print("7 % 3 = ", (7 % 3))
print("8 % 3 = ", (8 % 3))


#find the last digit
x = 123456432764983
print(x % 10)

"""

#assignment operator -> =
#x = 2000
#x = x + 1000  
#x += 1000 (can use -, *, /, % as well instead of +)
#print(x)
"""
x = 2000 
x %= 101 
print(x)


#comparison operator -> answer(true/false)
# ==     !=     >     <     >=
x = 100
y = 50
print(x==y)

x = "100"
y = 100
print(x==y)

x = "100"
y = "100"
print(x==y)

x = 100
y = 100
print(x!=y)  #false



#logical operator
x = 324
y = 45
z = 10000

#print(x > y and x > z)
#print(x > y and x < z)

#print(x > y or x > z)
#print(x < y or x > z)

print( x > y and x > z or y < x)  # T , F , T
print((x > y and x > z) or y < x) 

#class task
a = True
b = True
c = False
d = False

print(a and b)         #True
print(a or b)          #True
print(a or c)          #True
print(a and d)         #False
print(a and b or c)    #True
print((a and b) or c)  #True
print(a and (b or c))  #True
print(a or b and c)    #False 
print((a or b) and c)  #False
print(a or (b and c))  #True

#coditional statement
x = 184320
y = 313234
if x > y:
    print("x is greater than y")
    
print("end")


#class task
x = int(input("enter the number you want to check if it is positive or negative: "))

if x > 0:
    print("the number is positive")
else:
print("the number is negative")



#class task
age = int(input("ENTER YOUR AGE: "))
if age >= 18:
    print("YOU ARE ELIGIBLE TO VOTE!")
else: 
    print("YOU ARE NOT ELIGIBLE TO VOTE!")


#class task
x = int(input("ENTER ANY NUMBER: "))
if x % 2 == 0:
    print("THE NUMBER IS EVEN!")
else:
    print("THE NUMBER IS ODD!")

#class task
x = int(input("ENTER YOUR MATHS SCORE: "))
if x >= 80:
    print("A+")
elif x >= 70:
    print("A")
elif x >= 60:
    print("B")
elif x >= 50:
    print("C")
elif x < 50:
    print("F")

#class task
x = input("ENTER ANY ALPHABET: ")
if x == "a":
    print("vowel!")
elif x == "e": 
    print("vowel!")
elif x == "i": 
    print("vowel!")
elif x == "o": 
    print("vowel!")
elif x == "u": 
    print("vowel!")
else:
    print("consonant!")
"""
x = input("ENTER ANY ALPHABET: ")
if x == "a" or "e" or "i" or "o" or "u":
    print("vowel!")
else:
    print("consonant!")






































