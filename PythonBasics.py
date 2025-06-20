#%% [Hello World Print]
print("Hello World!")

#%% [Basic Variable Assignment and Printing]
x = 5
print(x)

#%% [String Assignment]
x = "world"
print(x)

#%% [Variable Scope Example]
c = "How Are You"
def func():
    c = "Are you"
    print(c)
func()
print(c)

#%% [Data Type: Integers]
x = 10
y = 20
print(type(x), type(y))

#%% [Data Type: Float]
r = 45.6
print(type(r))

#%% [Data Type: Boolean]
v = 2 > 6
print(type(v))
print(v)

#%% [Data Type: String]
x = 'class'
print(type(x))

#%% [Data Type: Complex Number]
s = 10 + 6j
print(type(s))

#%% [If-Else with Modulo]
x = 13
if x % 2 == 0:
    print("x is divisible by 3")
else:
    print("x is not divisible by 3")

#%% [Check Even/Odd from User Input]
x = int(input("Enter a number: "))
if x % 2 == 0:
    print(f"{x} is divisible by 2")
else:
    print(x, "is not divisible by 2")

#%% [Check Even/Odd using Elif]
x = int(input())
if x % 2 == 0:
    print(x, "even")
elif x % 2 == 1:
    print(x, "odd")
else:
    print(x, "is even")

#%% [Check for Prime Number (Basic)]
a = int(input("Enter a value: "))
if a > 1:
    for i in range(1, a):
        if a % i == 0:
            print("not a prime ")
            break
        else:
            print("prime")
            break
else:
    print("Value of A is less than 1")

#%% [For Loop with List]
list = [1, 2, 3, 4, 5]
for i in list:
    print(i)

#%% [Looping Over String Slices]
x = "benji is learning"
for i in x[0:5]:
    print(i)

#%% [String Cleaning: Strip & Title Case]
raw = "   Charanya "
clean = raw.strip().title()
print(clean)

#%% [Nested If Statement]
x = 8
r = x % 2
if r == 0:
   print("Even")
   print("good")
if True:
   print("Great")
else:
   print("Odd")

#%% [If-Elif-Else Logic Test]
a = 1
b = 4
c = 3
if a > b:
    print("a", a)
elif a > c:
    print("a with c", a)
elif b > c:
    print("b with c", b)
else:
    print(c)

#%% [For Loop with Empty Range]
num = 9
for i in range(0, 0):
    table = i * 1
print(num)

#%% [Using Math Library]
import math
x = math.sqrt(95)
print(x)

#%% [Simple Function with Argument]
def greet(name):
    print("Hello, " + name + ". Welcome to Python Programming!")
greet('ravi')

#%% [Function with Parameters and Return]
def employeedetails(empid, name):
    print("Employee Name:", name)
    print("Employee ID:", empid)
    return
employeedetails(empid=25, name="ravi")

#%% [Average of Two Numbers - User Input]
def avgof2num(num1, num2):
    sum = num1 + num2
    result = sum / 2
    return result
avgof2num(int(input("Enter a number: ")), int(input("Enter another number: ")))

#%% [Average of Two Numbers - Static]
def avgof2num(num1, num2):
    sum = num1 + num2
    result = sum / 2
    return result
print(avgof2num(5, 5))

#%% [Class Example: Computer Config]
class computer:
    def __init__(self, ram, hardisk):
        self.ram = ram
        self.hardisk = hardisk
    def config(self):
        print("Computer configuration")
        print(self.ram, self.hardisk)

comp = computer("16GB", "80GB")
comp1 = computer("8GB", "30GB")
comp.config()
comp1.config()

#%% [List Operations]
fruits = ["apple", "banana", "cherry", "apple"]
print("Original:", fruits)

fruits.append("date")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits[1] = "blueberry"
print("After modify:", fruits)

print("Iterate:")
for f in fruits:
    print("-", f)

#%% [Inheritance Example: Hexa_Project]
class Hexa_Project:
    def Project1(self):
        print("BFS")
    def Project2(self):
        print("ATM")

class Hexa_Admin(Hexa_Project):
    def Project3(self):
        print("Hexavarsity")
    def Project4(self):
        print("HR")

print("--- Hexa_Project Object ---")
project_obj = Hexa_Project()
project_obj.Project1()
project_obj.Project2()

#%% [Set Operations]
A = {1, 2, 3}
B = {2, 3, 4}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A-B:", A - B)

#%% [Dictionary Comprehension: Students & Scores]
students = [("Alice", 85), ("Bob", 92), ("Cara", 78), ("Bob", 75)]
print("All students:", students)

names = {name for name, _ in students}
print("Unique names:", names)

grades = {name: [] for name in names}
for name, score in students:
    grades[name].append(score)

avg_scores = {name: sum(scores)/len(scores) for name, scores in grades.items()}
print("Average scores:", avg_scores)

#%% [Class: Student Manager with Top Scorer Logic]
class studentmanager:
    def __init__(self):
        self.students = {}

    def addstudent(self, rollno, studentname, grade):
        if rollno in self.students:
            print(f"{rollno} already exists")
        else:
            self.students[rollno] = {"studentname": studentname, "grade": grade}
            print(f"{rollno} added to {studentname} in list")

    def getstudents(self, rollno):
        if rollno in self.students:
            return self.students[rollno]
        else:
            return f"No student with rollno {rollno}"

    def gettopstudents(self, criteria):
        top_students = [
            {"rollno": rollno, "studentname": data["studentname"], "grade": data["grade"]}
            for (rollno, data) in self.students.items()
            if data["grade"] > criteria
        ]
        return top_students

# Add student data
result = studentmanager()
student_data = [
    {"rollno": 1234, "studentname": "ravi", "grade": 100},
    {"rollno": 5678, "studentname": "mavi", "grade": 103},
    {"rollno": 1534, "studentname": "navi", "grade": 140},
]

for student in student_data:
    result.addstudent(student["rollno"], student["studentname"], student["grade"])

print(result.getstudents(1234))

top_students = result.gettopstudents(102)
print(top_students)
for student in top_students:
    print(student)

#%% [Class: Bank Account Basic]
class bankaccount:
    def __init__(self, accholder, balance=0):
        self.accholder = accholder
        self._balance = balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited, and my final balance is: {self._balance}")
        else:
            print("Deposit failed")
    def checkbalance(self):
        return self._balance

account = bankaccount("Ali", 100)
print(account.accholder)
account.deposit(100000)
print(account.checkbalance())
print(account._balance)

#%% md
# Inheritance

#%% [Class Inheritance: Savings Account with Interest]
class bankaccount:
    def __init__(self, accholder, balance=0):
        self.accholder = accholder
        self._balance = balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited, and my final balance is: {self._balance}")
        else:
            print("Deposit failed")
    def checkbalance(self):
        return self._balance

class savings_account(bankaccount):
    def __init__(self, accholder, balance=0, interestrate=0.05):
        super().__init__(accholder, balance)
        self.interestrate = interestrate
    def calculate_interest(self):
        interest = self._balance * self.interestrate
        self._balance += interest
        print(f"Interest added: {interest} and balance is: {self._balance}")

savings = savings_account("Ali", balance=10000, interestrate=0.03)
savings.deposit(1200)
savings.calculate_interest()
print(f"Final balance is: {savings.checkbalance()}")

#%% [Inheritance with Method Overloading and Overriding]
class bankaccount:
    def __init__(self, accholder, balance=0):
        self.accholder = accholder
        self._balance = balance
    def deposit(self, amount, currency="INR"):
        if amount > 0:
            self._balance += amount
            print(f"{amount} {currency} deposited, and final balance is: {self._balance}")
        else:
            print("Deposit failed")
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn, new balance: {self._balance}")
        else:
            print("Insufficient balance")

class savings_account(bankaccount):
    def __init__(self, accholder, balance=0, overdraft_limit=500):
        super().__init__(accholder, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"{amount} withdrawn and new balance is: {self._balance}")
        else:
            print("Exceeded overdraft limit")

basic_account = bankaccount("Ali", balance=10000)
basic_account.deposit(1200, "INR")  # method overloading by currency

saving_account = savings_account("Miri", balance=2000, overdraft_limit=399)
saving_account.withdraw(1200)  # method overriding
saving_account.withdraw(1200)

# ================================
# 1. Student Class with Instance Attributes
# ================================

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")

# Example usage
print("---- Student Info ----")
student1 = Student(101, "Aisha")
student1.display()


# ================================
# 2. Rectangle Class with Area Calculation
# ================================

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage
print("\n---- Rectangle Area ----")
rect = Rectangle(10, 5)
print("Area of Rectangle:", rect.area())


# ================================
# 3. Employee Class with Overtime Calculation
# ================================

class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def calculate_overtime(self, hours, rate_per_hour):
        overtime_pay = hours * rate_per_hour
        return overtime_pay

# Example usage
print("\n---- Employee Overtime ----")
emp = Employee(201, "Imran", 50000, "HR")
print(f"Employee: {emp.name}, Overtime Pay: {emp.calculate_overtime(5, 200)}")


# ================================
# 4. Find the Sum & Product of a List
# ================================

def sum_and_product(lst):
    total_sum = sum(lst)
    product = 1
    for num in lst:
        product *= num
    return total_sum, product

# Example usage
print("\n---- Sum & Product of List ----")
numbers = [2, 3, 4]
s, p = sum_and_product(numbers)
print(f"List: {numbers}")
print(f"Sum: {s}, Product: {p}")


# ================================
# 5. String Reversal
# ================================

def reverse_string(s):
    return s[::-1]

# Example usage
print("\n---- String Reversal ----")
text = "Python"
print(f"Original String: {text}")
print("Reversed String:", reverse_string(text))
