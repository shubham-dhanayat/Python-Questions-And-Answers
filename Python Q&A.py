#Challenge: CLI Contact Book (CSV-Powered)
#Create a terminal-based contact book tool that stores and manages contacts using a CSV file.
#Your program should:
#1. Ask the user to choose one of the following options:
#   - Add a new contact
#   - View all contacts
#   - Search for a contact by name
#   - Exit
#2. Store contacts in a file called contacts.csv with columns:
#   - Name
#   - Phone
#   - Email
#3. If the file doesn't exist, create it automatically.
#4. Keep the interface clean and clear.
#Example:
#Add Contact
#View All Contacts
#Search Contact
#Exit
#Bonus:
#- Format the contact list in a table-like view
#- Allow partial match search
#- Prevent duplicate names from being added

import csv
import os

CSV_FILE = "contacts.csv"


class ContactBook:

    # Create CSV with headers if it does not exist
    def __init__(self):
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Name", "Phone", "Email"])

    # Add a new contact
    def add_contact(self):
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()

        # Check duplicates
        if self.contact_exists(name):
            print("\n❌ Contact with this name already exists!")
            return

        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, phone, email])

        print("\n✅ Contact added successfully!")

    # Check duplicate name
    def contact_exists(self, name):
        with open(CSV_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                if row[0].lower() == name.lower():
                    return True
        return False

    # View all contacts
    def view_contacts(self):
        print("\n📘 ALL CONTACTS")
        print("-" * 40)

        with open(CSV_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)

            found = False
            for row in reader:
                found = True
                print(f"{row[0]:15} | {row[1]:12} | {row[2]}")

        if not found:
            print("No contacts found.")

        print("-" * 40)

    # Search contact by partial name
    def search_contact(self):
        search_name = input("Search name: ").lower()

        print("\n🔍 SEARCH RESULTS")
        print("-" * 40)

        found = False
        with open(CSV_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for name, phone, email in reader:
                if search_name in name.lower():  # partial match
                    found = True
                    print(f"{name:15} | {phone:12} | {email}")

        if not found:
            print("❌ No matching contact found.")

        print("-" * 40)

    # Main menu
    def menu(self):
        while True:
            print("""
============= CONTACT BOOK =============
1. Add Contact
2. View All Contacts
3. Search Contact
4. Exit
========================================
""")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("❌ Invalid option. Try again.")


app = ContactBook()
app.menu()


""" Challenge: Student Marks Analyzer
Create a Python program that allows a user to input student names along with their marks
and then calculates useful statistics.
Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students
Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""
student = {}

def add_student():
    while True:
        name = input("Enter student name:  \n stop for exit" ).strip()
        if name.lower() == 'stop':
            break

        if name in student:
            print("Student name already taken. Please enter another one.")
            continue

        try:
            marks = float(input("Enter marks: "))
            student[name] = marks
        except ValueError:
            print("Please enter a valid number.")

def high_score():
    high = max(student.values())
    for name,marks in student.items():
        if marks == high:
            print('Highest scor is = ',marks,' Gotted to the = ',name)
def low_score():
    low = min(student.values())
    for name,marks in student.items():
        if marks == low:
            print('Lowest scor is = ',marks,' Gotted to the = ',name)
def std_report():
    if not student:
        print('student not available')
        return
    marks = list(student.values())
    total_std  = len(student)
    avg_marks = sum(marks)/len(marks)

    print('------------- Report -------------')
    print('Total Students = ',total_std)
    print('Average Marks = ',avg_marks)
    high_score()
    low_score()

def menu():
    add_student()
    std_report()

menu()


# 🔹 Q1. Write a function to find the maximum of two numbers.

def max_find(*args):
    print(max(args))

max_find(1,2,3,4,5,6)


# 🔹 Q2. Write a function that returns factorial of a number.

def factorial(num):
    factorial = 1
    for i in range(num):
        factorial *= i+1
    return factorial
print(factorial(5))

# 🔹 Q3. Write a recursive function to print Fibonacci series up to n terms.

def fib(n):
    if n <= 1:        # base condition
        return n
    return fib(n - 1) + fib(n - 2)

def print_fib_series(num):
    for i in range(num):
        print(fib(i), end=" ")

print_fib_series(7)
print('----------------------------------------------------------------------------------------')

# 🔹 Q4. Write a function that takes a list and returns a new list with only even numbers.

def return_even(num):
    result = []
    for i in (num):
        if i % 2 == 0:
            result.append(i)
    print(result)

return_even([1,2,3,4,5,6,7,8])

# 🔹 Q5. Write a function that counts vowels in a string.

def vowel_count(string):
    count = 0
    for i in string:
        if i in 'aeiouAEIOU':
            count += 1
    print(count)

vowel_count('Akash'.upper())
print('----------------------------------------------------------------------------------------')

# *🔹 Q6. Write a function that accepts variable number of arguments (args) and returns their sum.

def add_num(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
add_num(1,2,3,4,5)

# 🔹 Q7. Write a function that accepts keyword arguments (kwargs) and prints them.

def key_word(**kwargs):
    for key, value in kwargs.items():
        print(key,'=',value)
key_word(name='shubham',age=22,city='indore')

# 🔹 Q8. Write a function that returns both sum and average of a list.
#Hint: Use multiple return values (tuple).
# 1st way
def avg_sum(num):
    sum = 0
    avg = 0
    for i in num:
        sum += i
    avg = sum/len(num)
    print('sum of the list is : ',sum ,'\nAvg of the list is : ',avg)

avg_sum([0,1,2,3,4,5])

#2nd Way:
print('Way 2nd')

def avg_sum_2(num):
    total = sum(num)
    averages = total/len(num)
    return total,averages
a = avg_sum_2([0,1,2,3,4,5])
print(a)

# 🔹 Q9. Write a function inside another function (nested function) and call the inner function.

def first_fun():
    print('inside 1st function')
    def second_fun():
        print('inside 2nd function')

    second_fun()
first_fun()

# 🔹 Q10. Write a lambda function to square a number.

square = lambda x: x*x
print(square(3))

# 🔹 Q11. Write a function using map() to convert a list of strings to integers.
# Example: ['1','2','3'] → [1,2,3]

def convert_to_int(str_list):
    """
    Converts a list of strings into a list of integers using map().
    """
    return list(map(int, str_list))

# Example usage
string_list = ['1', '2', '3']
int_list = convert_to_int(string_list)
print(int_list)

# 🔹 Q12. Write a function using filter() to return numbers divisible by 3 from a list.

def divisible_by_3(num_list):
    """
    Returns a list of numbers divisible by 3 using filter().
    """
    return list(filter(lambda x: x % 3 == 0, num_list))

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
result = divisible_by_3(numbers)
print(result)

#🔹 Q13. Write a function using reduce() to find product of all list numbers.

from functools import reduce

def product_of_list(num_list):
    """
    Returns the product of all numbers in a list using reduce().
    """
    return reduce(lambda x, y: x * y, num_list)

# Example usage
numbers = [1, 2, 3, 4, 5]
result = product_of_list(numbers)
print(result)

# 🔹 Q14. Write a function that accepts another function as argument (Higher-Order Function).

def higher_order(func, value):
    """
    Accepts a function and a value, applies the function to the value.
    """
    return func(value)

# Example function to pass
def square(x):
    return x * x

# Example usage
result = higher_order(square, 5)
print(result)

# 🔹 Q15. Write a function using default arguments.

def def_argument(name='shubh'):
    print('Hi my name is :',name)
def_argument('Siddhesh')


## Some tricky one.
print('## Some tricky one.')
## 1.Default mutable argument
def append_item(item, lst=[]):
    lst.append(item)
    return lst

print(append_item(1))  # ?
print(append_item(2))  # ?
print('----------------------------------------------------------------------------------------')

## 2.function as a object
def square(x):
    return x*x

f = square
print(f(5))
print('----------------------------------------------------------------------------------------')

## 3.decorator simple example
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def hello():
    print("Hello World")

hello()
print('----------------------------------------------------------------------------------------')

## 4.Closures / Enclosed scope
def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(5)
print(f(10))
print('----------------------------------------------------------------------------------------')

## 5.Variable scope (LEGB rule)
x = 10
def test():
    x = 5
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()

print(test())
print('----------------------------------------------------------------------------------------')

# 1. Create a class Student with attributes name, roll_no, marks. Print the details.

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


# Creating object
s1 = Student("Shubh", 23, 99)
s1.display()
print('----------------------------------------------------------------------------------------')

# 2. Create a class Rectangle with length and width. Write methods to calculate area and perimeter.

class rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def display(self):
        area = self.width * self.length
        print("Area Of rectangale :",area)

        perimeter = 2 * (self.width + self.length)
        print("Perimeter of rectangale :",perimeter)

a = rectangle(100, 200)
a.display()

print('----------------------------------------------------------------------------------------')

# 3. Create a class Car with attributes model, color, price. Create objects and display values.

class car:
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price

    def display(self):
        print("Model:", self.model)
        print("Color:", self.color)
        print("Price:", self.price)

a = car('Ab001','blue',100000)
a.display()

# Print the largest of three numbers.
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#c = int(input("Enter third number: "))
a = 343
b = 213
c = 2442

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
print('----------------------------------------------------------------------------------------')

# Given a list of numbers, print the sum without using sum().
a = [1,2,3,4,5]
b = 0
for i in a:
    b += i
print(b)

#
a = int('11',2)
print(a)

print('''--------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------''')
# Day 2
print('day 2')


#Count number of words in a sentence
c = 'I am learning a python'
a = c.split(' ')
print(a)
print(len(a))

#Replace all spaces with _
c = 'I am learning a python'
print(c.replace(' ','_'))

#Extract first and last character of string
c = 'Shubham'
print(c[0],c[-1])

#Convert string to title case
c = 'I am learning a python'
print(c.title())

#Check if string contains only digits
a = '12345'
if a.isnumeric() == True:
    print(a,'Is a numeric')
else:
    print(a,'Is a not numeric')

#Remove all vowels from a string
c = 'shubham'
a = []
for i in c:
    if i not in 'aeiou':
        a.append(i)
b = ''.join(a)
print(b)

#Print every 2nd character
s = 'shubhamdhanayat'
print(s[::2])

#Reverse words in a sentence
c = 'I am learning a python'
print(' '.join(c.split()[::-1]))

#Count occurrences of a character
s = 'shubhamdhanayat'
print(s.count('a'))

#Find first and last index of a substring
s = 'shubhamdhanayat'
first = s.index('a')
print('first =',first)
last = s.rindex('a')
print('first =',last)

print('''--------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------''')
# Day 3
print('day ---> list')

#Reverse a list.
l = [1,2,3,4,5]
#print(l[::-1])
print(l.reverse())
print(l)

#Find max, min, sum in a list of numbers.
l = [1,2,3,4,5]
print(sum(l))
print(min(l))
print(max(l))

#Remove duplicates from a list.
l = [1,2,3,4,2,2,3,5,1]
b = set(l)
l = list(b)
print(l)

#Concatenate two lists.
l = [1,2,3,4,5]
s = [1,3,6,8]
print(l + s)

#Multiply elements in a list.
l = [1,2,3]
print(l * 5)

#Print all even numbers from a list.
l = [1,2,3,4,5,6,7,8,9,10]
print([x for i in l if i % 2 == 0])

#Merge two lists and sort.
a = [1,2,3.14]
b = [4,5,6,5.6]
c = a + b
c.sort()
print(c)

#Count occurrences of an element.
l = [1,2,3,4,2,2,3,5,1]
print(l.count(2))

#Extract sublist using slicing.
l = [1,2,3,4,2,2,3,5,1]
print(l[2:6])

#Flatten a list of lists.
l = [[1,2], [3,4], [5,6]]
flat = [item for sub in l for item in sub]
print(flat)


#Reverse a string (3 ways)
#Method 1: Slicing (Most Common Interview Answer)
s = "python"
rev = s[::-1] #Strings are immutable, so this creates a new string.
print(rev)
#Method 2: Using reversed() + join() (Cleaner & Explicit)
s = 'python'
rev = ''.join(reversed(s))
print(rev)
#Method 3: Loop (Most Conceptual / Low-Level)
s = 'python'
rev = ''
for ch in s:
    rev = ch + rev
print(rev)

print('----------------------------------------')

#Count length of string (without len())
s = 'python'
count = 0
for ch in s:
    count = count + 1
print(count)

count = 0
for _ in "hello":
    count += 1
print(count)

print('----------------------------------------')

#Count vowels in a string
s = 'education'
count = 0
for ch in s:
    if ch in 'aeiou':
        count += 1
print(count)

s = "education"
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count += 1
print(count)

print('----------------------------------------')

#Count uppercase & lowercase letters
s = "PyThOn"
upper = 0
lower = 0
for ch in s:
    if ch.isupper():
        upper = upper + 1
    if ch.islower():
        lower = lower + 1
print('uppercase in a string is {},and lowercase in a string is {}'.format(upper,lower))

s = "PyThOn"
upper = lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print(upper, lower)

print('----------------------------------------')

#Check palindrome
s = 'madam'
b = s[::-1]
if s == b :
    print('string is paindrome')
else:
    print('string is not paindrome')

s = "madam"
print(s == s[::-1])

print('----------------------------------------')

#Count frequency of each character
s = 'aabbc'
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

print('----------------------------------------')

#First non-repeating character
s = 'aabbcdde'
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

for ch in s:
    if freq[ch] == 1:   #this for first non-repeating character.
        print(ch)
        break

count = 0
for ch in s:
    if freq[ch] == 1: #forseconf non-repeating character.
        print(ch)
        count += 1
        if count == 2:
            break

print('----------------------------------------')

#Remove duplicate characters (keep order)
s = 'programming'
result = ''
seen = set()

for ch in s:
    if ch not in seen:
        result += ch
        seen.add(ch)
print(result)

print('----------------------------------------')

#Check if two strings are anagrams
s1 = "listen"
s2 = "silent"
print(sorted(s1) == sorted(s2))

freq1 = {}
freq2 = {}
for ch in s1:
    freq1[ch] = freq1.get(ch, 0) + 1
for ch in s2:
    freq2[ch] = freq2.get(ch, 0) + 1
if freq1 == freq2:
    print('string is anagrams')
else:
    print('string is not anagrams')

print('----------------------------------------')

#Reverse words in a sentence
s = "python is easy"
words = s.split()
print(" ".join(words[::-1]))

print('----------------------------------------')

#Reverse each word (not sentence)
s = "python is easy"
result = []
for word in s.split():
    result.append(word[::-1])
print(" ".join(result))

print('----------------------------------------')

#Find longest word in a sentence
s = "python string interview questions"
words = s.split()

longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)

print('----------------------------------------')

#Replace space with _
s = "python is powerful"
print(s.replace(' ','_'))

print('----------------------------------------')

#Remove special characters
s = "py@th!on#123"
result = ""
for i in s:
    if i.isalnum():
        result += i
print(result)

print('----------------------------------------')

#Extract only digits
s = "order123amount45"
digits = ""

for ch in s:
    if ch.isdigit():
        digits += ch

print(digits)

print('----------------------------------------')

#Check if string is rotation of another
s1 = "abcd"
s2 = "cdab"

print(len(s1) == len(s2) and s2 in s1 + s1)

print('----------------------------------------')

#Check pangram (contains all alphabets)
s = "the quick brown fox jumps over the lazy dog"
alphabets = set("abcdefghijklmnopqrstuvwxyz")

print(alphabets.issubset(set(s.lower())))


#-------------------------------------------------List-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
print('-----------------list-----------------------')

#Reverse a list
#Method 1: Slicing (Best interview answer)
lst = [1,2,3,4]
rev = lst[::-1]
print(rev)
#Method 2: In-place (memory efficient)
lst = [1,2,3,4]
lst.reverse()
print(lst)

print('----------------------------------------')

#Find length of list (without len())
lst = [10,20,30]
count = 0
for _ in lst:
    count += 1
print(count)

for i in lst:
    count = count + 1
print(count)

print('----------------------------------------')

#Find sum of elements in a list
lst = [1,2,3,4]
count = 0
for i in lst:
    count = count + i
print(count)

lst1 = [1,2,3,4]
count = 0
for i in lst1:
    count += i
print(count)

print('----------------------------------------')

#Find maximum element (without max())
lst = [3,7,2,9,4]
max_value = lst[0]
for i in lst:
    if i > max_value:
        max_value = i
print(max_value)
print(max(lst)) #With max()

print('----------------------------------------')

#Find minimum element (without min())
lst = [3,7,2,9,4]
min_value = lst[0]
for i in lst:
    if i < min_value:
        min_value = i
print(min_value)
print(min(lst)) #with min()

print('----------------------------------------')

#Count frequency of each element
lst = [1,2,2,3,1,4]
freq = {}
for i in lst:
    freq[i] = freq.get(i,0) + 1
print(freq)

print('----------------------------------------')

#Remove duplicates (keep original order)
lst = [1, 2, 2, 3, 1, 4]
result = []
seen = set()
for i in lst:
    if i not in seen:
        result.append(i)
        seen.add(i)
print(result)

print('----------------------------------------')

#Find duplicate elements
lst = [1, 2, 2, 3, 1, 4]
seen = set()
duplicates = set()
for i in lst:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
print(duplicates)

print('----------------------------------------')

#Find second largest element
#Method 1: Sort (simple)
lst = [10, 20, 5, 30, 25]
unique = list(set(lst))
unique.sort()
print(unique[-2])
#Method 2: Single pass (better)
lst = [10, 20, 5, 30, 25]
first = second = float('-inf')
for i in lst:
    if i > first:
        second = first
        first = i
    elif first > i > second:
        second = i
print(second)

print('----------------------------------------')

#Check if list is palindrome
lst = [1,2,3,2,1]
print(lst == lst[::-1])

print('----------------------------------------')

#Rotate a list by k positions (LEFT ROTATION)
#Input : [1,2,3,4,5], k = 2
#Output: [3,4,5,1,2]
lst = [1, 2, 3, 4, 5]
k = 2
k = k % len(lst)
result = lst[k:] + lst[:k]
print(result)

print('----------------------------------------')

#Rotate a list by k positions (RIGHT ROTATION)
lst = [1, 2, 3, 4, 5]
k = 2
k = k % len(lst)
result = lst[-k:] + lst[:-k]
print(result)

print('----------------------------------------')

#Split list into EVEN and ODD numbers
lst = [1,2,3,4,5,6]
even = []
odd = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

print('----------------------------------------')

#Move all zeros to the end (maintain order)
lst = [0, 1, 0, 3, 12]
result = []
zero_count = 0
for i in lst:
    if i == 0:
        zero_count += 1
    else:
        result.append(i)
result.extend([0] * zero_count)
print(result)

print('----------------------------------------')

#Merge two lists alternately
a = [1, 2, 3]
b = ['a', 'b', 'c']
result = []
for i in range(len(a)):
    result.append(a[i])
    result.append(b[i])
print(result)

print('----------------------------------------')

#Merge two sorted lists into one sorted list
a = [1, 3, 5]
b = [2, 4, 6]
result = []
i = j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1
result.extend(a[i:])
result.extend(b[j:])
print(result)

print('----------------------------------------')

#Chunk a list into fixed-size parts
lst = [1,2,3,4,5,6,7]
size = 3
chunks = []
for i in range(0, len(lst), size):
    chunks.append(lst[i:i+size])
print(chunks)

print('----------------------------------------')

#Flatten a nested list (1 level)
lst = [[1, 2], [3, 4], [5]]
flat = []
for sub in lst:
    for i in sub:
        flat.append(i)
print(flat)

print('----------------------------------------')

#Find common elements between two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = []
for i in a:
    if i in b and i not in common:
        common.append(i)
print(common)

print('----------------------------------------')

#Find missing number in a list (1 to n)
lst = [1, 2, 4, 5]
n = len(lst) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)
print(expected_sum - actual_sum)

print('----------------------------------------')

lst = [[0]] * 3
lst[0][0] = 1
print(lst)

#-------------------------------------------------Tuple-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
print('-----------------tuple-----------------------')


#Create a tuple and access elements
t = (10, 20, 30, 40)

print(t[0])    # first
print(t[-1])   # last

print('----------------------------------------')

#Create a single-element tuple
t = (5,)
print(type(t))

print('----------------------------------------')

#Iterate over a tuple
t = ('a', 'b', 'c')

for item in t:
    print(item)

print('----------------------------------------')

#Count elements in a tuple (without len())
t = (10, 20, 30)
count = 0
for _ in t:
    count += 1
print(count)

print('----------------------------------------')

#Find sum of numeric tuple elements
t = (10, 20, 30)
count = 0
for _ in t:
    count += _
print(count)

print('----------------------------------------')

#Find maximum and minimum in a tuple (without max/min)
t = (7, 2, 9, 4)
max_value = t[0]
min_value = t[0]
for i in t:
    if i > max_value:
        max_value = i
    elif i < min_value:
        min_value = i
print(max_value)
print(min_value)
#
max_value = min_value = t[0]
for i in t:
    if i > max_value:
        max_value = i
    elif i < min_value:
        min_value = i
print(max_value ,min_value)

print('----------------------------------------')

#Convert tuple to list and modify data
t = (1,2,3)
lst = list(t)
lst.append(4)
t = tuple(lst)
print(t)

print('----------------------------------------')

#Check if element exists in tuple
t = (10, 20, 30)
print(20 in t)   # True
print(50 in t)   # False
#
for i in t:
    if i == 20 and i in t:
        print('element',i,'exist')

print('----------------------------------------')

#Unpack tuple elements
t = (10, 20, 30)
a, *b= t
print(a, b)
#
t = (10, 20, 30)
a, b, c = t
print(a, b, c)

print('----------------------------------------')

#Swap two variables using tuple unpacking
a = 10
b = 20
a, b = b, a
print(a, b)

print('----------------------------------------')

#Find the length of a tuple using recursion
def tuple_len(t):
    if not t:
        return 0
    return 1 + tuple_len(t[1:])

t = (10, 20, 30, 40)
print(tuple_len(t))

print('----------------------------------------')

#Count frequency of elements in a tuple
t = (1, 2, 2, 3, 1, 4)
freq = {}
for i in t:
    freq[i] = freq.get(i, 0) + 1
print(freq)

print('----------------------------------------')

#Remove duplicates from tuple (keep order)
t = (1, 2, 2, 3, 1, 4)
result = []
seen = set()
for i in t:
    if i not in seen:
        result.append(i)
        seen.add(i)
result = tuple(result)
print(result)

print('----------------------------------------')

#Find duplicate elements in a tuple
t = (1, 2, 2, 3, 1, 4)
seen = set()
duplicates = set()
for i in t:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
print(tuple(duplicates))

print('----------------------------------------')

#Sort a tuple (ascending & descending)
t = (5,2,9,1)
asc = tuple(sorted(t))
des = tuple(sorted(t , reverse = True))
print(asc , des)

print('----------------------------------------')

#Find second largest element in a tuple
t = (2,12,4,7,2,9,2,6,9,13,13)
a = set(t)
second_large = tuple(sorted(a))
print(second_large[-2])
#
t = (10, 20, 5, 30, 25)
unique = tuple(set(t))
unique = tuple(sorted(unique))
print(unique[-2])

print('----------------------------------------')

#Reverse a tuple
t = (1, 2, 3, 4)
rev = t[::-1]
print(rev)

print('----------------------------------------')

#Flatten a tuple of tuples
t = ((1, 2), (3, 4), (5,))
flat = []
for i in t:
    for j in i:
        flat.append(j)
print(tuple(flat))

print('----------------------------------------')

#Find common elements between two tuples
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
common = []
for i in t1:
    if i in t2:
        common.append(i)
print(common)

print('----------------------------------------')

#Convert list of tuples to dictionary
pairs = [('a', 1), ('b', 2), ('c', 3)]
d = {}
for k, v in pairs:
    d[k] = v
print(d)

print('----------------------------------------')

#Tuple with mutable elements
t = (1, [2, 3], 4)
t[1].append(5)  #Why allowed?
print(t)        #Tuple is immutable, but it holds a reference to a mutable list.

print('----------------------------------------')

#Check if a tuple is hashable
t1 = (1, 2, 3)
print(hash(t1))   # ✅ hashable
t2 = (1, [2, 3])
# hash(t2) ❌ TypeError

print('----------------------------------------')

#Use tuple as dictionary key
locations = {}
locations[(12.97, 77.59)] = "Bangalore"
locations[(19.07, 72.87)] = "Mumbai"
print(locations)

print('----------------------------------------')

#Swap elements inside tuple (NOT DIRECTLY)
t = (10,20)
lst = list(t)
lst[0],lst[1] = lst[1],lst[0]
print(tuple(lst))

print('----------------------------------------')

#Find index of element in tuple
t = (10, 20, 30, 40)
print(t.index(30))

print('----------------------------------------')

#Count occurrences of an element in tuple
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))

print('----------------------------------------')

#Find maximum sum pair in tuple of pairs
t = ((1, 2), (3, 4), (5, 1))
max_pair = t[0]
max_sum = sum(t[0])
for pair in t:
    if sum(pair) > max_sum:
        max_sum = sum(pair)
        max_pair = pair
print(max_pair)

print('----------------------------------------')

#Sort tuple of tuples by second element
t = ((1, 3), (4, 1), (2, 2))
sorted_t = tuple(sorted(t, key=lambda x: x[1]))
print(sorted_t)

print('----------------------------------------')

#Convert nested tuple to flat tuple (RECURSIVE)
def flatten(t):
    result = []
    for i in t:
        if isinstance(i, tuple):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

t = (1, (2, (3, 4)), 5)
print(tuple(flatten(t)))

print('----------------------------------------')

#Replace value inside tuple (WITHOUT modifying original)
t = (1, 2, 3, 2, 4)
new_t = tuple(99 if i == 2 else i for i in t)
print(new_t)

#-------------------------------------------------Set-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
print('-----------------Set-----------------------')

#Remove duplicates from a list using set
lst = [1, 2, 2, 3, 1, 4]
result = list(set(lst))
print(result)

print('----------------------------------------')

#Remove duplicates while preserving order (IMPORTANT)
lst = [1, 2, 2, 3, 1, 4]
seen = set()
result = []
for i in lst:
    if i not in seen:
        seen.add(i)
        result.append(i)
print(result)

print('----------------------------------------')

#Check if two lists have common elements
a = [1, 2, 3]
b = [4, 5, 3]
print(bool(set(a) & set(b)))

print('----------------------------------------')

#Find intersection of two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B)

#Find union of two sets
print(A | B)

print('----------------------------------------')

#Find difference between two sets
print(A - B)   # elements in A not in B

print('----------------------------------------')

#Find symmetric difference
print(A ^ B)

print('----------------------------------------')

#Check if one set is subset of another
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))

print('----------------------------------------')

#Check if two sets are disjoint
A = {1, 2}
B = {3, 4}
print(A.isdisjoint(B))

print('----------------------------------------')


#Count unique elements in a list
lst = [1, 2, 2, 3, 1, 4]
print(len(set(lst)))

print('----------------------------------------')


#Find common elements in multiple lists
l1 = [1, 2, 3, 4]
l2 = [2, 3, 5]
l3 = [2, 3, 6]
common = set(l1) & set(l2) & set(l3)
print(list(common))

print('----------------------------------------')


#Find elements present in list A but not in list B
A = [1, 2, 3, 4]
B = [3, 4, 5]
result = list(set(A) - set(B))
print(result)

print('----------------------------------------')


#Check if two strings are anagrams (using set + count)
s1 = "listen"
s2 = "silent"
print(set(s1) == set(s2) and len(s1) == len(s2))

print('----------------------------------------')


#Remove all common elements from two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A -= B
B -= {3, 4}

print(A)
print(B)

print('----------------------------------------')


#Find missing numbers in a range
nums = [1, 2, 4, 6]
full = set(range(1, 7))

missing = full - set(nums)
print(missing)

print('----------------------------------------')


#Check if list contains duplicate elements
lst = [1, 2, 3, 4, 2]
print(len(lst) != len(set(lst)))

print('----------------------------------------')


#Find symmetric difference between two lists
A = [1, 2, 3]
B = [3, 4, 5]

result = set(A) ^ set(B)
print(list(result))

print('----------------------------------------')


#Convert list of lists into set of tuples
lst = [[1, 2], [3, 4], [1, 2]]

unique = set(tuple(x) for x in lst)
print(unique)

print('----------------------------------------')


#Track visited elements (classic use case)
nums = [1, 2, 3, 2, 4, 1]
visited = set()
for i in nums:
    if i in visited:
        print("First repeated:", i)
        break
    visited.add(i)

print('----------------------------------------')


#Remove elements safely from a set while iterating
s = {1, 2, 3, 4, 5}

for i in list(s):
    if i % 2 == 0:
        s.remove(i)
print(s)

print('----------------------------------------')


#Difference between remove() and discard() (PRACTICAL)
s = {1, 2, 3}
# s.remove(10)    # ❌ KeyError
s.discard(10)     # ✅ No error
print(s)

print('----------------------------------------')


#Demonstrate pop() behavior in set
s = {10, 20, 30}
print(s.pop())
print(s)

print('----------------------------------------')


#Use frozenset inside a set
s = {frozenset({1, 2}), frozenset({3, 4})}
print(s)

print('----------------------------------------')


#Find unique words in a sentence
sentence = "python is easy and python is powerful"
words = set(sentence.split())
print(words)

print('----------------------------------------')


#Check if two lists are equal ignoring order
a = [1, 2, 3]
b = [3, 2, 1]
print(set(a) == set(b))

print('----------------------------------------')


#Find elements occurring only once
nums = [1, 2, 2, 3, 3, 4]
unique = set(nums)
duplicates = set()
for i in nums:
    if nums.count(i) > 1:
        duplicates.add(i)
result = unique - duplicates
print(result)

print('----------------------------------------')


#Convert dictionary values to a set (remove duplicates)
d = {'a': 1, 'b': 2, 'c': 1}
values = set(d.values())
print(values)

print('----------------------------------------')


#Find common characters in two strings
s1 = "interview"
s2 = "review"
common = set(s1) & set(s2)
print(common)

print('----------------------------------------')


#Track visited nodes (graph-style problem)
edges = [(1,2), (2,3), (3,4), (2,3)]
visited = set()
for e in edges:
    if e in visited:
        print("Duplicate edge:", e)
        break
    visited.add(e)

print('----------------------------------------')


#Find all distinct pairs from two sets
A = {1, 2}
B = {3, 4}
pairs = set()
for i in A:
    for j in B:
        pairs.add((i, j))
print(pairs)

#-------------------------------------------------Dict-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
print('-----------------Dict-----------------------')

#Create a dictionary and access values
d = {'id':101, 'name':'shubham','role':'devloper'}
print(d['name'])
print(d.get('salary')) # safe because it doesnt show result

print('----------------------------------------')


#Add and update elements in a dictionary
d = {'a':1}

d['b'] =2   # add
d['a'] = 101#update
print(d)

print('----------------------------------------')


#Delete elements from dictionary (all ways)
d = {"a": 1, "b": 2, "c": 3}
del d["a"]
d.pop("b")
print(d)

print('----------------------------------------')


#Iterate over dictionary (keys, values, items)
d = {"a": 1, "b": 2}
for k in d:
    print(k)
for v in d.values():
    print(v)
for k, v in d.items():
    print(k, v)

print('----------------------------------------')

#Count frequency of elements (VERY IMPORTANT)
nums = [1, 2, 2, 3, 1, 4]
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1
print(freq)

print('----------------------------------------')

#Find character frequency in a string
s = "interview"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


print('----------------------------------------')


#Find element with maximum frequency
freq = {'a': 2, 'b': 5, 'c': 1}
max_key = None
max_val = 0
for k, v in freq.items():
    if v > max_val:
        max_val = v
        max_key = k
print(max_key)

print('----------------------------------------')


#Swap keys and values (values must be unique)
d = {"a": 1, "b": 2}
swapped = {}
for k, v in d.items():
    swapped[v] = k
print(swapped)

print('----------------------------------------')



#Check if a key exists in dictionary
d = {"id": 1, "name": "A"}
print("id" in d)
print("salary" in d)

print('----------------------------------------')

#Merge two dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}
d1.update(d2)
print(d1)

print('----------------------------------------')


#Access values from a nested dictionary
emp = {
    "id": 101,
    "name": "Shubham",
    "skills": {
        "primary": "Python",
        "secondary": "SQL"
    }
}
print(emp["id"],emp["name"])
print(emp)
print(emp["skills"]["primary"])


print('----------------------------------------')


#Safely access nested keys (avoid KeyError)
print(emp.get("skills", {}).get("primary"))

print('----------------------------------------')


#Group elements based on a condition (IMPORTANT)
words = ["apple", "ant", "ball", "bat"]
group = {}
for w in words:
    key = w[0]
    group.setdefault(key, []).append(w)
print(group)

print('----------------------------------------')


#Group numbers by even and odd
nums = [1, 2, 3, 4, 5]
result = {"even": [], "odd": []}
for n in nums:
    if n % 2 == 0:
        result["even"].append(n)
    else:
        result["odd"].append(n)
print(result)

print('----------------------------------------')



#Convert two lists into a dictionary
keys = ["id", "name", "role"]
values = [101, "Shubham", "Engineer"]
d = {}
for k, v in zip(keys, values):
    d[k] = v

print(d)


print('----------------------------------------')


#Sort dictionary by keys
d = {"c": 3, "a": 1, "b": 2}
sorted_dict = dict(sorted(d.items()))
print(sorted_dict)


print('----------------------------------------')


#sort dictionary by values
d = {"a": 3, "b": 1, "c": 2}
sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_dict)

print('----------------------------------------')


#Find key with maximum value
d = {"a": 10, "b": 50, "c": 20}
max_key = None
max_val = float("-inf")
for k, v in d.items():
    if v > max_val:
        max_val = v
        max_key = k
print(max_key)


print('----------------------------------------')


#Remove keys with specific values
d = {"a": 1, "b": 0, "c": 2}
result = {}
for k, v in d.items():
    if v != 0:
        result[k] = v
print(result)


print('----------------------------------------')


#Invert dictionary with duplicate values (GROUPING)
d = {"a": 1, "b": 2, "c": 1}
inv = {}
for k, v in d.items():
    inv.setdefault(v, []).append(k)
print(inv)

print('----------------------------------------')


#Shallow copy vs reference bug (VERY IMPORTANT)
d1 = {"a": [1, 2], "b": 3}
d2 = d1          # reference copy
d2["a"].append(99)
print(d1)


print('----------------------------------------')


#Fix the above bug using shallow copy
d1 = {"a": [1, 2], "b": 3}
d2 = d1.copy()
d2["a"].append(99)
print(d1)

print('----------------------------------------')


#Proper fix using deep copy
import copy
d1 = {"a": [1, 2], "b": 3}
d2 = copy.deepcopy(d1)
d2["a"].append(99)
print(d1)
print(d2)

print('----------------------------------------')


#Modify dictionary safely while iterating
d = {"a": 1, "b": 0, "c": 2}
for k in list(d.keys()):
    if d[k] == 0:
        del d[k]
print(d)

print('----------------------------------------')


#Merge dictionaries without overwriting existing keys
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}
result = d1.copy()
for k, v in d2.items():
    if k not in result:
        result[k] = v
print(result)

print('----------------------------------------')


#Find first non-repeating character using dictionary
s = "aabbcdde"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
for ch in s:
    if freq[ch] == 1:
        print(ch)
        break

print('----------------------------------------')


#Count frequency using defaultdict
from collections import defaultdict
nums = [1, 2, 2, 3, 1]
freq = defaultdict(int)
for n in nums:
    freq[n] += 1
print(dict(freq))

print('----------------------------------------')


# Build index mapping (value → list of indices)
nums = [10, 20, 10, 30, 20]
index_map = {}
for i, v in enumerate(nums):
    index_map.setdefault(v, []).append(i)
print(index_map)

print('----------------------------------------')


#LRU-style removal using popitem()
cache = {"a": 1, "b": 2, "c": 3}
cache.popitem()
print(cache)

print('----------------------------------------')


#   Convert list of dictionaries into single dictionary
records = [
    {"id": 1, "name": "A"},
    {"id": 2, "name": "B"}
]
result = {}
for r in records:
    result[r["id"]] = r["name"]
print(result)


#-------------------------------------------------Function-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
print('-----------------Function-----------------------')


#Find Maximum Using Function
def find_max(lst):
    return max(lst)
nums = [1, 2, 3, 4, 5]
print(find_max(nums))

#Count Vowels in String
def count_vowels(s):
    count = 0
    for ch in s:
        if ch in 'aeiouAEIOU':
            count += 1
    return count
print(count_vowels('shubham dhanayat from sambhajinagar'))

#Remove Duplicates Using Function
def remove_dub(lst):
    return list(set(lst))
print(remove_dub([1,2,3,1,2,4,5,4,7,3,6,0,2,4]))

#Reverse String Using Function
def revers_str(s):
    return s[::-1]
print(revers_str('Shubham'))

#Check Palindrome
def check_plindrom(s):
    return s == s[::-1]
print(check_plindrom('shubham'))

def check_plindrom(s):
    if s == s[::-1]:
        print("Plindrom")
    else:
        print("Not Plindrom")
print(check_plindrom('shubham'))

#Sum of Numbers Using *args
def sum_number(*args):
    return sum(args)
print(sum_number(1,2,3,4,5,6,7,8,9,0,1))

#Find Factorial (Recursion)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(5))

#Find Even Numbers Using Function
def even_num(lst):
    result = []
    for n in lst:
        if n % 2 == 0:
            result.append(n)
    return result
print(even_num([1,2,3,4,5,6,7,8,9,0,1]))

def even_nums(lst):
    return [x for x in lst if x%2==0]
print(even_nums([1,2,3,4,5,6]))

#Find Frequency Using Function
def freq_count(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    return freq
print(freq_count('7349583462865623048'))

#Find Largest Word
def largest_word(s):
    words = s.split()
    return max(words, key=len)
print(largest_word("I love Python Programming"))

def largest_word(s):
    words = s.split()
    max_len = words[0]
    for word in words[1:]:
        if len(word) > len(max_len):
            max_len = word
    return max_len
print(largest_word("I love Python Programming"))


#Find Minimum Using Function
def min_val(s):
    minimum_value = 0
    for i in s:
        if i < minimum_value:
            minimum_value = i
    return minimum_value
print(min_val([1,2,3,4,5,6,7,8,9,0,1]))

def min_val(s):
    return min(s)
print(min_val([1,2,3,4,5,6,7,8,9,1]))

#Count Words in Sentence
def count_words(s):
    return len(s.split())
print(count_words("I love Python very much"))

def count_words(s):
    word = s.split()
    count = 0
    for i in word:
        count += 1
    return count
print(count_words("I love Python very much"))

#Check Prime Number
def prime(s):
    if s <= 1:
        return False
    for i in range(2,s):
        if s%i == 0:
            return False
    return True
print(prime(8))

#Sum of Digits
def sum_digits(n):
    return sum(int(i) for i in str(n))

print(sum_digits(1234))


#Merge Two Lists Using Function
def merge_list(a, b):
    return a + b

print(merge_list([1,2],[3,4]))

#Find Second Largest Number
def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]

print(second_largest([10,20,30,40]))

#Check Anagram
def is_anagram(a, b):
    return sorted(a) == sorted(b)

print(is_anagram("listen","silent"))

#Count Uppercase Letters
def count_upper(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    return count

print(count_upper("PyThOn"))

#Find Common Elements in Two Lists
def common(a, b):
    return list(set(a) & set(b))

print(common([1,2,3],[2,3,4]))

#Fibonacci Series Using Function
def fib(n):
    a, b = 0, 1
    res = []
    for _ in range(n):
        res.append(a)
        a, b = b, a+b
    return res

print(fib(6))

#Default Argument Trap
def add_item(x, lst=[]):
    lst.append(x)
    return lst

print(add_item(1))
print(add_item(2))

#Fix Default Argument Trap
def add_item(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst

print(add_item(1))
print(add_item(2))

#Closure Example
def outer():
    x = 10
    def inner():
        return x + 5
    return inner

f = outer()
print(f())

#Function Returning Function
def greet(msg):
    def inner():
        print(msg)
    return inner

f = greet("Hello")
f()

#Using *args and **kwargs Together
def info(a, *b, **c):
    print(a)
    print(b)
    print(c)

info(10, 20, 30, name="Shubham", age=22)

#Generator Function
def even_gen(n):
    for i in range(1, n+1):
        if i%2 == 0:
            yield i

print(list(even_gen(10)))

#Count Function Calls (Closure)
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

c = counter()
print(c())
print(c())
print(c())

#Recursive Sum of List
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1,2,3,4]))

#Using map() with Function
def square(x):
    return x*x

nums = [1,2,3,4]
print(list(map(square, nums)))

#Using filter() with Function
def even(x):
    return x%2==0

nums = [1,2,3,4,5,6]
print(list(filter(even, nums)))


#Q1. Create Simple Class and Object




class Car:
    def __init__(self, brand):
        self.brand = brand

    def change_brand(self, new_brand):
        self.brand = new_brand


c = Car("BMW")
c.change_brand("Audi")
print(c.brand)

class car:
    def __init__(self,brand):
        self.brand = brand
    def change_brand(self,new_brand):
        self.brand = new_brand
a = car('audi')
a.change_brand('farrari')
print(a.brand)

#Q1. Create Simple Class and Object
class demo:
    def show(self):
        print('Hello There')
s = demo()
s.show()

#Q2. Using Constructor
class demo:
    def __init__(self):
        print('Hello i am from constructor')
s = demo()  # we can call this
demo()      # we can call this as well

class student:
    def __init__(self,name):
        self.name = name
        print('my name is',self.name)
student('Shubham')
s = student('yogesh')
print(s.name)


#Q3. Multiple Objects
class student:
    def __init__(self,name):
        self.name = name
        print(name)
a = student('Shubham')
b = student('yogesh')
student('shailesh')


#Q4. Instance Variable Outside Class
class Test:
    pass

t = Test()
t.x = 10

print(t.x)


#Q5. Class Variable
class company:
    name = 'wipro'
a = company()
print(a.name)
a.name = 'accenture'
print(a.name)


#Q6. Class Variable via Object (Trap)
class company:
    name = 'wipro'

t = company()
t.name = 'accenture'
print(t.name)
print(company.name)

#Q7. Instance Method
class demo:
    def show(self):
        print('Hello i am from constructor')
demo().show()
t = demo()
t.show()

#Q8. Class Method
class demo:
    x = 10
    @classmethod
    def show(self):
        self.x = 20
demo.show()
print(demo.x)

#Q9. Static Method
class math:
    @staticmethod
    def add(a,b):
        return a + b
print(math.add(43,43))
m = math()
print(m.add(43,43))


#Q10. Without @staticmethod (Trap)
class Math:
    def add(a,b):
        return a+b

print(Math.add(5,7))
# m = Math()
# print(m.add(43,43))

#Q11. Object dict
class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
a = A(1,2)
print(a.__dict__)

#Q12. Local Variable
class test:
    def show(self):      #when in method self is present then use test().show() is not then use test.show()
        x = 10
        print(x)
test().show()

#Q13. self is Not Keyword
class demo:
    def __init__(abc,x):
        abc.x = x
        print(abc.x)
demo(100).x
a = demo(90)
a.x
print(a.x)


#Q14. Missing self (Error)
class demo:
    def show():
        print("Hello")
#demo().show()   # give an error because method dont have self
demo.show()     # work fine


#Q15. Constructor Without Parameters
class demo:
    def __init__(self):
        print('constructor without parameter')
a = demo()
demo()
print(a)

#Q16. Instance vs Class Variable (Trap)
class test:
    x = 10
t1 = test()
t2 = test()
t1.x = 20
print(t1.x)
print(t2.x)
print(test.x)

#Q17. Modify Class Variable Correctly
class test:
    x = 10
t1 = test()
test.x = 50
print(t1.x)
print(test.x)


#Q18. Constructor Overwriting Variable
class A:
    x = 5
    def __init__(self):
        self.x = 20
a = A()
print(a.x)
print(A.x)

#Q19. Class Method Accessing Class Variable
class Demo:
    x = 10
    @classmethod
    def show(cls):
        print(cls.x)
Demo.show()

#Q20. Class Method via Object
class Demo:
    x = 15
    @classmethod
    def show(cls):
        print(cls.x)
d = Demo()
d.show()

#Q21. Static Method Accessing Variable (Trap)
class Demo:
    x = 10000
    @staticmethod
    def show():
        print(x)
#Demo().show()    # static methos can not access class variable directyly
class Demo:
    x = 10000
    @staticmethod
    def show():
        print(Demo.x)
Demo.show()         # but we can access using a class name in method


#Q22. Correct Static Method
class Demo:
    x = 10
    @staticmethod
    def show():
        print(Demo.x)
Demo.show()


#Q23. Instance Method Accessing Class Variable
class Demo:
    x = 70
    def show(self):
        print(self.x)
Demo().show()


#Q24. Instance Variable Hides Class Variable
class Demo:
    x = 5
    def __init__(self):
        self.x = 20
d = Demo()
print(d.x)
print(Demo.x)


#Q25. Multiple Attributes in Object
class A:
    def __init__(self):
        self.x = 10
        self.y = 20
a = A()
print(a.__dict__)
print(a.__str__)
print(a.__repr__)


#Q26. Delete Instance Variable
class A:
    def __init__(self):
        self.x = 10
a = A()
del a.x
print(a.__dict__)


#Q27. Delete Class Variable
class A:
    x = 10
del A.x
print(hasattr(A, "x"))

#Q28. Accessing Deleted Variable (Trap)
class A:
    x = 10
a = A()
del A.x
#print(a.x) attribute error

#Q29. Class Inside Class
class A:
    class B:
        def show(self):
            print("Hello")
obj = A.B()
obj.show()
A.B().show()


#Q30. Using getattr()
class A:
    x = 10
a = A()
print(getattr(a, "x"))



class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name)
        print(self.marks)
s1 = student('Shubham',100)
s2 = student('karan',200)
s1.display()
print(s1.marks)


"""Q2.
Create a class Employee with:
class variable company
instance variable name
method to show both"""
class Employee:
    company = 'abc'
    def __init__(self,name):
        self.name = name

    def show(self):
        print(Employee.company)
        print(self.name)
s1 = Employee('Shubham')
s1.show()

"""Q3.
Create a class Calculator with:
static method add(a, b)
static method sub(a, b)"""
class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
c1 = Calculator.add(10,23)
print(c1)
c2 = Calculator.sub(10,23)
print(c2)

"""Q4.
Create a class Counter with:
class variable count
class method to increase count"""

class counter:
    count = 0
    @classmethod
    def increase(self):
        self.count += 1
counter.increase()
counter.increase()
print(counter.count)

"""Q5.
Create a class Car with:
brand (constructor)
method to change brand"""

class car:
    def __init__(self,brand):
        self.brand = brand
    def change_brand(self,new_brand):
        self.brand = new_brand
a = car('audi')
a.change_brand('farrari')
print(a.brand)

"""Q6.
Create class Bank with:
balance (instance variable)
deposit() and withdraw()"""
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient Balance")
b = Bank(1000)
b.deposit(500)
b.withdraw(300)

print(b.balance)


"""Q7.
Create class Demo to show:
instance variable
class variable
local variable in one method"""
class Demo:
    x = 10   # class variable
    def __init__(self):
        self.y = 20   # instance variable
    def show(self):
        z = 30   # local variable
        print(self.y, Demo.x, z)
d = Demo()
d.show()
Demo().show()


"""Q8.
Create class Math with:
static method to check even/odd"""
class Math:

    @staticmethod
    def check(n):
        if n % 2 == 0:
            return "Even"
        return "Odd"

print(Math.check(10))
print(Math.check(7))


"""Q9.
Create class User and:
add attribute after object creation
print using dict"""
class User:
    pass
u = User()
u.name = "Shubham"
u.age = 22

print(u.__dict__)


"""Q10.
Create class Test and:
show difference between modifying class variable using class and object"""
class Test:
    x = 10
t = Test()
Test.x = 20
print(Test.x)
t.x = 30
print(t.x)
print(Test.x)


#Q1. Simple Single Inheritance
class A:
    def show_a(self):
        print('A')
class B(A):
    def show_b(self):
        print('B')
a = B()
a.show_a()
a.show_b()

#✅ Q2. Inheritance with Constructor
class A:
    def __init__(self):
        print('Constrauctor a')
class B(A):
    def __init__(self):
        super().__init__()
        print('Constrauctor b')
B()

#✅ Q3. Method Overriding
class A:
    def show(self):
        print('A')
class B(A):
    def show(self):
        print('B')
b = B()
b.show()

#✅ Q4. Calling Parent Method Using super()
class A:
    def show(self):
        print('A')
class B(A):
    def show(self):
        super().show()
        print('B')
b = B()
b.show()

#✅ Q5. Multilevel Inheritance
class A:
    def showA(self):
        print('A1')
class B(A):
    def showB(self):
        print('B2')
class C(B):
    def showC(self):
        print('C3')

c = C()
c.showA()
c.showB()
c.showC()

#✅ Q6. Multiple Inheritance (MRO Demo)
class A:
    def show(self):
        print('A')
        super().show()
class B:
    def show(self):
        print('B')
class C(A,B):
    pass
c = C()
c.show()



class A:
    def show(self):
        print('A1')
        super().show()
class B:
    def show(self):
        print('B2')
class C(A,B):
    def show(self):
        super().show()
        print('C3')

c = C()
c.show()

#✅ Q8. Instance vs Class Variable in Inheritance
class A:
    x = 10
class B(A):
    pass
b = B()
b.x = 20
print(A.x)
print(b.x)

#✅ Q10. Variable Shadowing
class A:
    x = 10
class B(A):
    x = 20
print(A.x)
print(B.x)



#✅ Q1. Create Class and Object
class A:
    def show(self):
        print('hello student')
s = A()
s.show()

#Using Constructor
class A:
    def __init__(self,name):
        self.name = name

    def show(self):
        print('hello ',self.name)
s = A('shubham')
s.show()

s = A('shubham')
print(s.name)

#✅ Q3. Instance vs Class Variable
class demo:
    x = 10
    def show(self):
        self.x = 20
        print(self.x)
a = demo()
print(a.x)
a.show()

class demo:
    x = 10
    def __init__(self,y):
        self.y = y
t1 = demo(5)
t2 = demo(10)
print(t1.x,t1.y)
print(t2.x,t2.y)

#✅ Q4. Modify Class Variable
class demo:
    x = 10
    def show(self):
        demo.x = 20
        print(demo.x)

demo.x = 60
print(demo.x)

#✅ Q5. Method Overriding
class animal:
    def show(self):
        print('dog')
class cat(animal):
    def show(self):
        print('cat')
cat().show()
a = cat()
a.show()

#✅ Q6. Using super()
class animal:
    def show(self):
        print('dog')
class cat(animal):
    def show(self):
        print('cat')
        super().show()
cat().show()


#✅ Q7. Multiple Inheritance (MRO)
class A:
    print('a')
class B:
    print('b')
class C(A,B):
    print('c')
C()

class A:
    def show(self):
     print('a')
class B:
    def show(self):
     print('b')
class C(A,B):
    print('c')
C().show()

print('==============')

class A:
    def show(self):
        print('a')
        super().show()
class B:
    def show(self):
     print('b')
class C(A,B):
    print('c')
C().show()

#Q8. Private Variable (Encapsulation)
class Test:
    def __init__(self):
        self.__x = 10

t = Test()
print(t._Test__x)

class Test:
    def __init__(self,y):
        self.__y = y

t = Test(100)
print(t._Test__y)


#✅ Q9. Getter & Setter (@property)
class Emp:
    def __init__(self,sal):
        self.__sal = sal
    @property
    def sal(self):
        return self.__sal
    @sal.setter
    def sal(self,s):
        self.__sal = s

e = Emp(40000)
e.sal = 50000
print(e.sal)

#✅ Q10. Abstract Class
from abc import ABC,abstractmethod

class Shape(ABC):
    def area(self):
        pass
class Square(Shape):
    def __init__(self,x):
        self.x = x
    def area(self):
        return self.x * self.x
print(Square(5).area())

#✅ Q11. Multilevel Inheritance
class A:
    def showa(self):
        print('A')
class B(A):
    def showb(self):
        print('B')
class C(B):
    def showc(self):
        print('C')
c = C()
c.showa()
c.showb()
c.showc()

#✅ Q12. Hierarchical Inheritance
class A:
    def show(self):
        print('hey student')
class B(A):
    def show(self):
        print('Hey shubham')
class C(A):
    def show(self):
        super().show()
        print('Hey abhishek')

C().show()

class A:
    def show(self):
        print('hey')
class B(A):
    pass
class C(A):
    pass
C().show()

#✅ Q13. Diamond Problem (MRO)
class A:
    def show(self):
        print('hey student')
class B(A):
    def show(self):
        print('Hey shubham')
class C(A):
    def show(self):
        print('Hey abhishek')
class D(B,C):
    pass
D().show()

print('==============')

class A:
    def show(self):
        print('hey student')
class B(A):
    def show(self):
        print('Hey shubham')
        super().show()
class C(A):
    def show(self):
        print('Hey abhishek')
        super().show()
class D(B,C):
    pass
D().show()

#✅ Q14. Check MRO
class A: pass
class B(A): pass
class C(B): pass

print(C.mro())

#✅ Q15. Constructor Overriding
class A:
    def __init__(self):
        print('init A')
class B(A):
    def __init__(self):
        print('init B')
        super().__init__()

B()

#✅ Q16. Protected Variable
class A:
    def __init__(self):
        self._x = 10
class B(A):
    def show(self):
        print(self._x)
B().show()

#✅ Q17. Polymorphism with List
class Dog:
    def sound(self):
        print('dog sound')
class Cat:
    def sound(self):
        print('cat sound')
Cat().sound()
Dog().sound()
animal = [Dog(),Cat()]
for i in animal:
    i.sound()

print('==============')

class Dog:
    def sound(self):
        print('dog sound')
        super().sound()
class Cat:
    def sound(self):
        print('cat sound')
class A(Dog,Cat):
    pass
A().sound()


#✅ Q18. Overloading Using *args
class A:
    def show(self,*args):
        return sum(args)
print(A().show(1,2,34))

#✅ Q19. Read-Only Property
class Test:
    def __init__(self):
        self.__x = 10
    def show(self):
        return self.__x
print(Test().show())

#✅ Q20. isinstance() & issubclass()
class A: pass
class B(A): pass

b = B()

print(isinstance(b,B))
print(isinstance(b,A))
print(issubclass(B,A))

#✅ Q21. Class Decorator (Basic)
def my_deco(cls):
    cls.company = 'Tcs'
    return cls
@my_deco                                          #Internally becomes:  class Emp:
class Emp:                                          #                       pass
    pass                                            #                   Emp = my_deco(Emp)
print(Emp.company) # it works
#Emp.my_deco()  # this not work because my_deco in not added in the class it is a seperate function


#✅ Q22. Method Decorator Inside Class
def deco(func):
    def wrap(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")
    return wrap

class Test:

    @deco
    def show(self):
        print("Hello")

Test().show()

#✅ Q23. Abstract + Inheritance
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def show(self):
        pass
class B(A):
    def show(self):
        print('Hey')
B().show()

#✅ Q24. Cannot Instantiate Abstract
from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def show(self):
        pass

#A()


#✅ Q25. Override Getter (@property)
class A:
    @property
    def x(self):
        return 10
class B(A):
    @property
    def x(self):
        return 20
      #  super().x #After return code not execute so super() is never execute
print(B().x)


#✅ Q26. Override Setter
class A:
    def __init__(self):
        self._x = 10

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,v):
        self._x = v

class B(A):

    @A.x.setter
    def x(self,v):
        self._x = v*2

b = B()
b.x = 5
print(b.x)

#✅ Q27. str Overloading
class Test:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return f"Value = {self.x}"

print(Test(10))


#✅ Q28. eq Overloading
class Box:
    def __init__(self,w):
        self.w = w

    def __eq__(self,other):
        return self.w == other.w

b1 = Box(10)
b2 = Box(10)

print(b1 == b2)


#✅ Q29. Multiple Constructors Trick
class test:
    def __init__(self,*x):
        if len(x) == 1 :
            print('one args')
        elif len(x) == 2:
            print('two args')
        else:
            print('more that one args')
test(10)
test(10,10)
test(3,22,4,5,3,5,3,5,43,2,34,4)

#✅ Q30. Class as Callable
class Test:
    def __call__(self):
        print('class like function')

t = Test()
t()

#✅ Q31. Method Resolution Order (Complex)
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    pass

print(D.mro())
D().show()

#✅ Q32. super() in Multiple Inheritan
class A:
    def show(self):
        print('A')
class B(A):
    def show(self):
        super().show()
        print('B')
class C(A):
    def show(self):
        super().show()
        print('C')
class D(B,C):
    def show(self):
        super().show()
        print('D')

D().show()


#✅ Q33. Private Variable in Inheritance
class A:
    def __init__(self):
        self.__x = 10
class B(A):
    def show(self):
        print(self._A__x)
B().show()


#✅ Q33. Private Variable in Inheritance
class AgeError(Exception):
    pass

class Person:
    def __init__(self, age):
        if age < 18:
            raise AgeError("Underage")
        self.age = age

p = Person(20)
print(p.age)


#✅ Q35. Overriding init Without super()
class A:
    def __init__(self):
        self.x = 10

class B(A):
    def __init__(self):
        self.y = 20

b = B()
print(hasattr(b,'x'), hasattr(b,'y'))


#✅ Q36. Singleton Pattern (Basic)
class Singleton:
    _obj = None

    def __new__(cls):
        if cls._obj is None:
            cls._obj = super().__new__(cls)
        return cls._obj

a = Singleton()
b = Singleton()

print(a is b)


#✅ Q37. Class Method as Alternative Constructor
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls,s):
        name,marks = s.split(',')
        return cls(name,int(marks))

s = Student.from_string("Amit,90")
print(s.name,s.marks)


#✅ Q38. slots Usage
class Test:
    __slots__ = ['x','y']

t = Test()
t.x = 10
t.y = 20
print(t.x,t.y)


#✅ Q39. Dynamic Attribute Binding
class A:
    pass

a = A()
a.name = "Shubham"

print(a.name)


#✅ Q40. Metaclass (Intro Level)
class MyMeta(type):
    def __new__(cls,name,bases,dct):
        dct['company'] = "TCS"
        return super().__new__(cls,name,bases,dct)

class Emp(metaclass=MyMeta):
    pass

print(Emp.company)


================================================================================================================================
                                                    Pandas
                                                    
import pandas as pd
import numpy as np


employee = pd.read_csv('data/HR.employees')
#print(employee.head(1))

pd.set_option('display.max_columns', None)


#Display only EMPLOYEE_ID, FIRST_NAME, SALARY
employee[['EMPLOYEE_ID','FIRST_NAME','SALARY']]

#Find all employees with salary > 10000
employee[employee['SALARY'] > 10000]

#Find employees working in department 90
employee[employee['DEPARTMENT_ID'] == 90]
employee[employee['DEPARTMENT_ID'].isin([80,90])] #-->For multiple dpt_id

#Get employees whose JOB_ID = 'IT_PROG'
employee[employee['JOB_ID'] == 'IT_PROG']

#Count total number of employees
employee['EMPLOYEE_ID'].count()
employee.shape[0]

#Count employees who do not have a manager
employee[employee['MANAGER_ID'].isna()].shape[0]

#Find employees whose COMMISSION_PCT is NULL
employee[employee['COMMISSION_PCT'].isna()]

#Show first 10 records using pandas
employee.head(10)

#Get unique department IDs
employee['DEPARTMENT_ID'].unique()

#Find minimum and maximum salary
employee['SALARY'].agg(['min','max'])

#Sort employees by salary (highest to lowest)
employee.sort_values(by='SALARY',ascending=False)

#Find employees whose FIRST_NAME starts with 'S'
employee[employee['FIRST_NAME'].str.startswith('S')]

#Find employees whose LAST_NAME contains 'an'
employee[employee['LAST_NAME'].str.contains('an')]

#Convert all employee names to UPPERCASE
employee[['FIRST_NAME','LAST_NAME']] = (employee[['FIRST_NAME','LAST_NAME']].apply(lambda x: x.str.upper()))
#print(employee)

#Create a new column ANNUAL_SALARY = SALARY * 12
employee['ANNUAL_SALARY'] = employee['SALARY'] * 12
#print(employee)

#Find employees with salary between 11500 and 12000
employee[employee['SALARY'].between(11500, 12000)]

#Show employees hired after 01-Jan-2005
#employee['HIRE_DATE'] = pd.to_datetime(employee['HIRE_DATE'])
#employees_after_2005 = employee[employee['HIRE_DATE'] > '2005-01-01']
#print(employees_after_2005)

#Find employees whose email ends with @oracle.com (if present)
employee[employee['EMAIL'].str.endswith('@oracle.com')]

#Rename column SALARY to MONTHLY_SALARY
employee.rename(columns={'SALARY' : 'MONTHLY_SALARY'},inplace=True)
#print(employee)


#Find total salary paid per department
employee.groupby('DEPARTMENT_ID',as_index=False)['SALARY'].sum()

#Find average salary per job role
employee.groupby('JOB_ID',as_index=False)['SALARY'].mean()

#Find the department with highest total salary
employee.groupby('DEPARTMENT_ID',as_index=False)['SALARY'].sum().sort_values(by='SALARY',ascending=False).head(1)

#Find job role with lowest average salary
employee.groupby('JOB_ID',as_index=False)['SALARY'].mean().sort_values(by='SALARY',ascending=True).head(1)

#Count employees per manager
employee.groupby('MANAGER_ID')['EMPLOYEE_ID'].count()

#Find managers managing more than 3 employees
employee.groupby('MANAGER_ID')['EMPLOYEE_ID'].count().reset_index(name='emp_count').query('emp_count > 3')

#Extract year and month from HIRE_DATE
employee['HIRE_DATE'] = pd.to_datetime(employee['HIRE_DATE'])
employee['Year'] = employee['HIRE_DATE'].dt.year
employee['Month'] = employee['HIRE_DATE'].dt.month

#Count employees hired per year
employee['Year'] = employee['HIRE_DATE'].dt.year
employee.groupby('Year')['EMPLOYEE_ID'].count()

#Find department-wise earliest hire
employee.groupby('DEPARTMENT_ID',as_index=False)['HIRE_DATE'].min().sort_values(by='HIRE_DATE')

#Find department-wise latest hire
employee.groupby('DEPARTMENT_ID',as_index=False)['HIRE_DATE'].max().sort_values(by='HIRE_DATE')

#Find employees hired on weekends
employee['HIRE_DATE'] = pd.to_datetime(employee['HIRE_DATE'])
        # Filter employees hired on weekends (Saturday=5, Sunday=6)
weekend_hires = employee[employee['HIRE_DATE'].dt.dayofweek >= 5]

#Find second highest salary
second_highest = employee['SALARY'].nlargest(2).iloc[-1]

#Find Top 3 salaries per department
#top3_per_dept = employee.groupby('DEPARTMENT_ID', group_keys=False).apply(lambda x: x.nlargest(3, 'SALARY'))
#print(top3_per_dept)

top3_per_dept = employee.groupby('DEPARTMENT_ID', group_keys=False).apply(
    lambda x: x.nlargest(3, 'SALARY')[['FIRST_NAME', 'SALARY']]
)
#print(top3_per_dept)

#Find employees earning above department average salary
employee['Dept_Avg_Salary'] = employee.groupby('DEPARTMENT_ID')['SALARY'].transform('mean')
ABOVE_AVG = employee[employee['SALARY'] > employee['Dept_Avg_Salary']]
#print(ABOVE_AVG)

#Replace NULL COMMISSION_PCT with 0
employee['COMMISSION_PCT'] = employee['COMMISSION_PCT'].fillna(0)
#print(employee)

#Create a flag column IS_MANAGER
employee['IS_MANAGER'] = employee['EMPLOYEE_ID'].isin(employee['MANAGER_ID']).map({True:'Y', False:'N'})
#print(employee)

#Find employees who are not managers
#1st way
employee[~employee['EMPLOYEE_ID'].isin(employee['MANAGER_ID'])]
#2nd way
non_managers = employee[employee['IS_MANAGER'] == 'N']
#print(non_managers)

#Find employees whose salary is in top 10%
salary_90th = employee['SALARY'].quantile(0.9)
top_10_percent = employee[employee['SALARY'] >= salary_90th]
#print(top_10_percent)

#Rank employees by salary within department
employee['Salary_Rank'] = employee.groupby('DEPARTMENT_ID')['SALARY'].rank(ascending=False, method='dense')
#print(employee[['DEPARTMENT_ID','FIRST_NAME','SALARY','Salary_Rank']])

#Detect duplicate emails
duplicate_emails = employee[employee.duplicated('EMAIL', keep=False)]
#print(duplicate_emails)

#Create a summary DataFrame with:
#Department ID
#Employee Count
#Avg Salary
#Max Salary
dept_summary = employee.groupby('DEPARTMENT_ID').agg(
    Employee_Count=('EMPLOYEE_ID','count'),
    Avg_Salary=('SALARY','mean'),
    Max_Salary=('SALARY','max')
).reset_index()

#print(dept_summary)

print(employee)


import pandas as pd
import numpy as np


employee = pd.read_csv('data/HR.employees')
#print(employee.head(1))

#Find total salary paid per department
employee.groupby('DEPARTMENT_ID',as_index=False)['SALARY'].sum()

#Find average salary per job role
employee.groupby('JOB_ID',as_index=False)['SALARY'].mean()

#Find the department with highest total salary
employee.groupby('DEPARTMENT_ID',as_index=False)['SALARY'].sum().sort_values(by='SALARY',ascending=False).head(1)

#Find job role with lowest average salary
employee.groupby('JOB_ID',as_index=False)['SALARY'].mean().sort_values(by='SALARY',ascending=True).head(1)

#Count employees per manager
employee.groupby('MANAGER_ID')['EMPLOYEE_ID'].count()

#Find managers managing more than 3 employees
employee.groupby('MANAGER_ID')['EMPLOYEE_ID'].count().reset_index(name='emp_count').query('emp_count > 3')

#Extract year and month from HIRE_DATE
employee['HIRE_DATE'] = pd.to_datetime(employee['HIRE_DATE'])
employee['Year'] = employee['HIRE_DATE'].dt.year
employee['Month'] = employee['HIRE_DATE'].dt.month

#Count employees hired per year
employee['Year'] = employee['HIRE_DATE'].dt.year
employee.groupby('Year')['EMPLOYEE_ID'].count()

#Find department-wise earliest hire
employee.groupby('DEPARTMENT_ID',as_index=False)['HIRE_DATE'].min().sort_values(by='HIRE_DATE')

#Find department-wise latest hire
employee.groupby('DEPARTMENT_ID',as_index=False)['HIRE_DATE'].max().sort_values(by='HIRE_DATE')

#Find employees hired on weekends
employee['HIRE_DATE'] = pd.to_datetime(employee['HIRE_DATE'])
        # Filter employees hired on weekends (Saturday=5, Sunday=6)
weekend_hires = employee[employee['HIRE_DATE'].dt.dayofweek >= 5]

#Find second highest salary
second_highest = employee['SALARY'].nlargest(2).iloc[-1]

#Find Top 3 salaries per department
#top3_per_dept = employee.groupby('DEPARTMENT_ID', group_keys=False).apply(lambda x: x.nlargest(3, 'SALARY'))
#print(top3_per_dept)

top3_per_dept = employee.groupby('DEPARTMENT_ID', group_keys=False).apply(
    lambda x: x.nlargest(3, 'SALARY')[['FIRST_NAME', 'SALARY']]
)
#print(top3_per_dept)

#Find employees earning above department average salary
employee['Dept_Avg_Salary'] = employee.groupby('DEPARTMENT_ID')['SALARY'].transform('mean')
ABOVE_AVG = employee[employee['SALARY'] > employee['Dept_Avg_Salary']]
#print(ABOVE_AVG)

#Replace NULL COMMISSION_PCT with 0
employee['COMMISSION_PCT'] = employee['COMMISSION_PCT'].fillna(0)
#print(employee)

#Create a flag column IS_MANAGER
employee['IS_MANAGER'] = employee['EMPLOYEE_ID'].isin(employee['MANAGER_ID']).map({True:'Y', False:'N'})
#print(employee)

#Find employees who are not managers
#1st way
employee[~employee['EMPLOYEE_ID'].isin(employee['MANAGER_ID'])]
#2nd way
non_managers = employee[employee['IS_MANAGER'] == 'N']
#print(non_managers)

#Find employees whose salary is in top 10%
salary_90th = employee['SALARY'].quantile(0.9)
top_10_percent = employee[employee['SALARY'] >= salary_90th]
#print(top_10_percent)

#Rank employees by salary within department
employee['Salary_Rank'] = employee.groupby('DEPARTMENT_ID')['SALARY'].rank(ascending=False, method='dense')
#print(employee[['DEPARTMENT_ID','FIRST_NAME','SALARY','Salary_Rank']])

#Detect duplicate emails
duplicate_emails = employee[employee.duplicated('EMAIL', keep=False)]
#print(duplicate_emails)

#Create a summary DataFrame with:
#Department ID
#Employee Count
#Avg Salary
#Max Salary
dept_summary = employee.groupby('DEPARTMENT_ID').agg(
    Employee_Count=('EMPLOYEE_ID','count'),
    Avg_Salary=('SALARY','mean'),
    Max_Salary=('SALARY','max')
).reset_index()

#print(dept_summary)

print(employee)


                                                    






















