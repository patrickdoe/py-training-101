'''
some_text = 'Testing python'

print(some_text.upper())            # Prints text in UPPERCASE.
print(some_text.lower())            # Prints text in lowercase.

print(some_text.find('y'))          # Finds index location of 'y' (9).

print(some_text.replace('Testing', "Learning")) # Replace text stored in a variable.

print(some_text.find('python'))     # Prints first index of where 'python' appears.
print('python' in some_text)        # Returns "True". Another way of finding if a certain text exists within a string.

---

print(10 / 3)                       # Prints decimal numbers.
print(10 // 3)                      # Prints whole integers.

print(10 % 3)                       # Prints remainder of the divivsion.
print(10 ** 3)                      # 10^3.

x = 10
x += 3                              # Adding 3 to the x value of 10 and store it in the same variable.
print(x)

total1 = 10 + 3 * 2                 # Prints 16.
print(total1)

total2 = (10 + 3) * 2               # Prints 26. Control the order of what gets calculated first with parenthesis.
print(total2)

---

x = 3 > 2
print(x)                            # Prints 'True' because 3 is greater than 2.

x = 3 == 2
print(x)                            # Prints 'False', 3 isn't equal to 3.

x = 3 != 2
print(x)                            # Prints 'True', 3 isn't equal to 3.

---

price = 25
print(price > 10 and price < 30)    # Prints 'True' because the price is between 10 and 30.

price = 5
print(price > 10 or price < 30)     # Prints 'True' because the price is lower than 30, 'or' only needs one statement to be true.

print(not price > 10)               # Prints 'True', flips the statement to check if the price isn't greater than 10, which is true, it's not.

---

temperature = 25

if temperature > 30:
    print("It's a hot day")
elif temperature > 20:
    print("It's a nice day. Not too hot.") # Will print this message based on temperature. The > 10 is also true but it won't be printed because this option is listed first. 
elif temperature > 10:
    print("It's a bit cold.")
else:
    print("It's a cold day.")

    
if temperature > 30:
    print("It's a hot day")
elif temperature > 10:
    print("It's a bit cold.")       # In this scenario it will only print this one because it enters this option first.
elif temperature > 20:
    print("It's a nice day. Not too hot.")
else:
    print("It's a cold day.")

---

print('Simple weight converter')
print('-----------------------')
weight = float(input('Enter weight: '))

unit = input('(K)g or (L)bs: ')

if unit.lower() == 'l':
    weight = weight * 0.45359237
    print('That equals to around', int(weight), 'kg.')
elif unit.lower() == 'k':
    weight = weight * 2.2
    print('That equals to around', int(weight), 'lbs.')
else:
    print('Input error.')

---

i = 1

while i <= 5:           # Loop throught while i is less or equal to 5.
    print(i * '*')      # Prints 1 to 5 asterix.
    i = i + 1           # Add +1 to 'i' variable.

---

names = ['John', 'Bob', 'Sam', 'Mary', 'Lewis']
print(names)            # Prints all the name with brackets.
print(names[0])         # Prints John.
print(names[-1])        # Prints the last name; Lewis. Starts from the end of the list.

names[0] = 'Eva'
print(names[0])         # Prints 'Eva'. John has been changed to Eva. 

print(names[0:3])       # Prints index 0-2 with brackets.

---

numbers = [1, 2, 3, 4, 5]

numbers.append(6)
print(numbers)          # Prints the list with the appended addition of '6'.

numbers.insert(0, -1)   # Inserts a new number ('-1') on index 0.
print(numbers)

numbers.remove(6)
print(numbers)          # Removes the '6' from the list.

numbers.clear()         # Clears the enire list.
print(numbers)

numbers = [1, 2, 3, 4, 5]

print(1 in numbers)     # Prints 'True'. Checking if '1' is in the list which is true.
print(10 in numbers)    # Prints 'False' since 10 doesn't exist in the list.

print (len(numbers))    # Prints the number of elements in the list.

---

numbers = [1, 2, 3, 4, 5]
print(numbers)          # Prints the list with brackets.

print('\nPrinting with a for-loop:')
for i in numbers:       # A for-loop that prints all elements on a new line (less code than the while loop below).
    print(i)


print('\nPrinting with a while-loop:')
i = 0 

while i < len(numbers): # A while-loop that prints all elements on a new line.
    print(numbers[i])
    i = i + 1

---

numbers = range(5)              # Note: Starts with 0, ends with 4.
print(numbers)                  # Prints the range 0 - 4.

for number in numbers:
    print(number)               # Prints the range 0 1 2 3 4.

print('---')

numbers = range(5, 10)          # Range: 5 - 9.
for number in numbers:
    print(number)               # Prints the range 5 6 7 8 9.

print('---')

numbers = range(5, 10, 2)       # Range: 5 - 9, skipping every other number.
for number in numbers:
    print(number)               # Prints the range 5 7 9.

print('---')

for i in range(5):
    print(i)                    # Also prints the range 0-4. Variables aren't necessary.

---

numbers = (1, 2, 3, 3)          # A tuple, cannot be changed.
print(numbers.count(3))         # Prints 2 since there are two '3' in the tuple.
'''
