# def outer_function():
#     a = 20

#     def inner_function():
#         a = 30
#         print('a =', a)

#     inner_function()
#     print('a =', a)


# a = 10
# outer_function()
# print('a =', a)

# def outer_function():
    
#     a = 20

#     def inner_function():
#         global a
#         a = 30
#         print('a =', a)

#     inner_function()
#     print('a =', a)


# # a = 10
# outer_function()
# print('a =', a)

# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])
# print(thislist[:])
# print(thislist[2:5])
# print(thislist[::-1])
# thislist[0:3] = ["mango","blackcurrant", "watermelon"]
# print(thislist)
# thislist.insert(2, "papaya")
# print(thislist)
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]

# thislist.extend(tropical)
# print(thislist)
# thislist.remove("banana")
# print(thislist)
# del thislist[0]
# print(thislist)
# thislist.pop(0)
# print(thislist)
# thislist.pop() # remove last element by default
# print(thislist)



# thisdict = {1:"apple", 2:"banana", 3:"cherry"}
# tropical = {4:"mango", 5:"pineapple", 6:"papaya"}

# thisdict.update(tropical)
# print(thisdict)

# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# x = zip(a, b)
# print(tuple(x))

# thisdict = {1:"apple", 2:"banana", 3:"cherry"}
# thisdict = {4:"mango", 5:"pineapple", 6:"papaya"}

# x = zip(thisdict,thisdict)
# print(dict(x))


# name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
# roll_no = [ 4, 1, 3, 2 ]

# x = zip(name,roll_no)
# print(list(x))






# Python program to
# demonstrate accessing of
# variables of nested functions
 
# def f1():
#     s = 'I love GeeksforGeeks'
     
#     def f2():
#         print(s)
         
#     f2()

# f1()

# student_name = 'Jules'

# marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

# for student in marks:

#     if student == student_name:
#         print(marks[student])
#         break
# else:
#     print('No entry with that name found.')


# student_name = 'v'
# marks={'James': 90, 'Jules': 55, 'Arthur': 77}

# get_mark={student[1]:marks[student] for student in marks}

# get_mark = {marks[student]  if student == student_name else "wrong" for student in marks}

# print ({k : v  if  k == student_name else "wrong" for k, v in marks.items()})
# get_mark={marks[student]  if student == student_name else "wrong" for student in marks}
# print(get_mark)

# get_mark=[marks[student] for student in marks if student == student_name]


# x = 10
# print("x in main: ", x)
# def foot():
  
#     def foo():
#         x=20
#         def bar():
#             global x 
#             x = 25
#             print("Before calling inner: ", x)
#         print("Before calling bar: ", x)
#         print("Calling bar now")
#         bar()
#         print("After calling bar: ", x)

#     foo()
#     print("After calling foo: ", x)

# foot()
# print("x in main: ", x)




    
# a = 20

# def inner_function():
#     global a
#     a = 30
#     print('a =', a)

   



# a = 10

# print('a =', a)

# my_list = ["mouse", [8, 4, 6], ['a']]
# # print(my_list[2][0])
# # print(my_list[1][0])
# # print(my_list[1][0])


# odd = [2, 4, 6, 8]

# # change the 1st item    
# odd[0] = 1            

# print(odd)

# # change 2nd to 4th items
# odd[1:4] = [3, 5, 7]  

# print(odd)

# odd = [1, 3, 5]
# odd.append(7)
# print(odd)
# odd.extend([9, 11, 13])
# print(odd)


# letters = list(map(lambda x: x, 'human'))
# print(letters)

# number_list = [ x for x in range(20) if x % 2 == 0]
# print(number_list)


# num_list = [y for y in range(10) if y % 2 == 0 if y % 5 == 0]
# print(num_list)



# obj = [i if i%2==0 else "Odd" for i in range(10)]
# print(obj)

# grocery =["milk","butter","bread"]

# print(list(enumerate(grocery)))

# print(list(enumerate(grocery, 10)))
# print(dict(enumerate(grocery, 10)))

# for count, item in enumerate(grocery):
#   print(count, item)


# fruits ={1:"banana","4":"apple",3:"cheeku",4:7} 

# new_dict ={keys:values for keys,values in sorted(fruits.items())}

# new_dict ={keys:values for keys,values in sorted(fruits.items(), key = lambda kv: kv[0])}

# new_dict ={keys:values for keys,values in sorted(fruits.items(), key = lambda kv: kv[0])}
# print(new_dict)






# dictionary_of_names = {'beth': 37, 
#                        'jane': 32,
#                        'john': 41, 
#                        'mike': 59
# }


# # print(sorted(dictionary_of_names))


# sorted_age = sorted(dictionary_of_names.items(), key = lambda kv: kv[1])
# print(sorted_age)

# def myfunc1():
#   x = "J"
#   def myfunc2():
#     global x
#     x = "hello"
#   myfunc2() 
#   return x

# print(myfunc1())
 
# x="p"
# def myfunc1():
#   x=21
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2() 
#   return x

# print(myfunc1())
# print(x)






# class Student:

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def msg(self):
#         print(self.name + "got" + self.marks, "%")
    
#     @classmethod
#     def get_per(cls, name, marks):
#         return cls(name, str(int(marks)/600)*100)


# s1 = Student("rahul", "94")
# marks = "560"
# name = "rahul"
# s2 = Student.get_per(name, marks)
# s2.msg()



# class Parrot:
    
#     # instance attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     # instance method
#     def sing(self, song):
#         return "{} sings {}".format(self.name, song)

#     def dance(self):
#         return "{} is now dancing".format(self.name)

#     def move(cls, name,age):
#         cls.name = name
#         cls.age = age 


# p= Parrot().move()

# instantiate the object
# blu = Parrot("Blu", 10)



# # call our instance methods
# print(blu.sing("'Happy'"))
# print(blu.dance())


# inheritance 


# parent class
# class Bird:
    
#     def __init__(self):
#         print("Bird is ready")

#     def whoisThis(self):
#         print("Bird")

#     def swim(self):
#         print("Swim faster")

# # child class
# class Penguin(Bird):

#     def __init__(self):
#         # call super() function
#         super().__init__()
#         print("Penguin is ready")

#     def whoisThis(self):
#         print("Penguin")

#     def run(self):
#         print("Run faster")

# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()


# data encapsulation

# class Computer:

#     def __init__(self):
#         self.__minprice = 900

#     def sell(self):
#         print("Selling Price: {}".format(self.__minprice))

#     def setMinPrice(self, price):
#         self.__minprice = price



# c = Computer()
# c.sell()



# # change the price
# c.__minprice = 1000
# c.sell()

# # using setter function
# c.setMinPrice(1000)
# c.sell()




#Polymorphism

# class Parrot:

#     def fly(self):
#         print("Parrot can fly")
    
#     def swim(self):
#         print("Parrot can't swim")

# class Penguin:

#     def fly(self):
#         print("Penguin can't fly")
    
#     def swim(self):
#         print("Penguin can swim")

# # common interface
# def flying_test(bird):
#     bird.fly()

# #instantiate objects
# blu = Parrot()
# peggy = Penguin()

# # passing the object
# flying_test(blu)
# flying_test(peggy)


# class Person:
#     "This is a person class"
#     age = 10

#     def greet(self):
#         print('Hello')


# print(Person.age)


# # Output: <function Person.greet>
# print(Person.greet)

# # Output: "This is a person class"
# print(Person.__doc__)


# harry = Person()

# print(harry.greet)
# harry.greet()


# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,3)

#     def findArea(self):
#         a, b, c = self.sides
#         # calculate the semi-perimeter
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)




# t = Triangle()

# t.inputSides()

# t.dispSides()

# t.findArea()


# a_tuple =(10,20,30)

# x= iter(a_tuple)
# print(next(x))


# new_list = [num for num in range(50) if  num > 20 and num % 2 == 0]
# print(new_list)


# static and class method



# from datetime import date as dt


# class Employee:
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age
      
#    @staticmethod
#    def isAdult(age):
#         if age > 18:
#          return True
#         else:
#          return False
#    @classmethod
#    def emp_from_year(emp_class, name, year):
#       return emp_class(name, dt.today().year - year)
#    def __str__(self):
#       return 'Employee Name: {} and Age: {}'.format(self.name, self.age)

# e1 = Employee('Dhiman', 25)
# print(e1)
# print(Employee.emp_from_year('Subhas', 1987))
# # print(e2)
# print(Employee.isAdult(25))
# # print(e2)
# print(Employee.isAdult(16))

# positional and keyword argument


# keyword arguments

# def rectangleArea(width, height):
#     return width * height


# # print(rectangleArea(width=1, height=2)) # keyword arguments
# # print(rectangleArea(height=1, width=2))
# print(rectangleArea(2, height=1))
# print(rectangleArea(height=1, 2)) # error



# positional arguments 

# def info(name, age, gender):
#     print(f"name {age} and age {name}) and gender {name}")

# # info("Alice", 23.0) # positional argument
# # info("vivek", age =36) # positional arguments follows keyword arguments
# info(10, "male", gender="sonu") # sequence is important


# print(rectangleArea(height=1, height=2))

# examples:

# def test_args_2(x, y,z):
#     print(x, z,y)
    
# test_args_2(5,3,z=4) 
# # test_args_2(x=4,y=2,z=5) 
# # test_args_2(y=2,z=5,x=4) 


# def test_args_2(x, y, z=0):
#     print(x, y, z)
# test_args_2(1,2)


# cnt = Counter()
# for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#     cnt [word] += 1


# str1 = "vivek"
# dic = {x: str1.count(x) for x in str1}
# dic = {x: str1.count(x) for x in sorted(str1)}

# print(dic)


# str1= "my code is repeatT "
# dic = {x:str1.lower().count(x)  for x in str1.lower()}
# print(dic)

# nums =[i for i in range(1,1001)]
# # nums =[i for i in range(1,1001) if i%8==0]
# nums =[i for i in range(1,1001) if i%6==0]
# print(nums)
# print(nums)
# q1_ans = [num for num in nums if num%8==0 ]
# print(q1_ans)


# footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

# sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
# sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1], reverse=True) 
# print(sorted_footballers_by_goals)




# sales = {
#     'apples': 12,
#     'bananas': 32,
#     'oranges': 24,
#     'grapes': 43,
#     'tangerines': 55
# }

# sorted = sorted(sales, key=sales.get)
# print(sorted)

# sorted_dict = {}

# for key in sorted:
#     sorted_dict[key] = sales[key]
  
# print(sorted_dict)



# fruits ={1:"banana","4":"apple",3:"cheeku",4:7} 

# sorted_dict = {}

# sorted_dict ={sorted_dict[key] : fruits[key] for key in sorted(fruits, key=fruits.get)}

# print((sorted_dict))

# sorted_dict = {k:v for k,v in sorted(sales.get())}
# print(sorted_dict)
# (apple, 12)

# from collections import defaultdict
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
 
# d = defaultdict(list)


# from collections import deque,defaultdict
# import itertools

# def tail(filename, n=10):
#     'Return the last n lines of a file'
#     with open(filename) as f:
#         return deque(f, n)

# def moving_average(iterable, n=3):
#     it = iter(iterable)
#     d = deque(itertools.islice(it, n-1))
#     d.appendleft(0)
#     s = sum(d)
#     for elem in it:
#         s += elem - d.popleft()
#         d.append(elem)
#         yield s / n



# from collections import deque,defaultdict
# import itertools



# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
 
# d = defaultdict(list)

# for k, v in s:
#     d[k].append(v)

# print(sorted(d.items()))


# d =defaultdict(list(v for k,v  in s sorted(d.items()) if d[k]))


# from collections import defaultdict


# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
  
# # Defining a dict
# d = defaultdict(list)
  
# for k,v in s:
#     d[k].append(v)
      
# print("Dictionary with values as list:")
# print(d)


# a=[[1,2],[3,4],[5,6]]

# a=[ x[1] for x in a]
# print(a)


# a=[[1,2],[3,4],[5,6]]

# a=[ x[1] for x in a]
# a=[x.append('a') or x for x in a]
# a = [x + ['a'] for x in all] 

# print(a)




# all = [[], [], [], []]
# all = [],[],[],[]

# x = [i.append('x') or i for i in all[::]]
# print(x)

# all = [],[],[],[]
# a = [x + ['a'] for x in all] 

# print(a)

# tmp ={
#     "frames": ['0', '12', '56', '35', None, '77', '120', '1000'],
#     "fra": ['0', '12', '56', '35', '77', '120']
# }

# # tmp = {"frames": ['0', '12', '56', '35', None, '77', '120', '1000']}

# # output = [frame if frame else None for frame in tmp['fra']]
# output = [int(value) for value in tmp['frames'] if value is not None]
# print(output)



# nums = [i for i in range(1,1001)]

# string = "Practice Problems to Drill List Comprehension in Your Head."

# q2_answer = [num for num in nums if "6" in str(num)]
# print(q2_answer)

# nums = [i for i in range(1,1001) if "6" in str(i)]
# print(nums)

# q3_answer = len([char for char in string if char == " "])
# print(q3_answer)

# q3_answer = len([char for char in string if char == " "])
# print(q3_answer)

# q4_answer = "".join([char for char in string if char not in ["a","e","i","o","u"]])
# print(q4_answer)

# words = string.split(" ") 
# q5_answer = [word for word in words if len(word) < 5]
# q6_answer = {word:len(word) for word in words}
# print(q5_answer)
# print(q6_answer)

# q7_answer = [num for num in nums if True in [True for divisor in range(2,10) if num % divisor == 0]]
# print(q7_answer)

# q8_answer = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums}
# print(q8_answer)

# class is universal and init method is also public.

# class Emp:
#     def __init__(self,name):
#         self.name=name

#         # print(name)
    
#     def get_name(self):
#         return self.name
  
     
#     def add_one(self,x):

#         return x + 1

# d=Emp("vivek")
# print(d.add_one(5))

# d=Dog("tim")
# print(d.get_name())
# print(d.get_na())



# define static method
# class Emp:
#     def __init__(self,name):
#         self.name=name
        
    
#     def get_name(self):
#         return self.name
  
     
#     def add_one(x):
        
#         return x + 1

# # d=Dog("s")

# print(Emp.add_one(5))
# d.add_one("tim",5)


# class Emp:
#     def __init__(self,name,age):
#         self.name=name
#         self.age = age

#         # print(name)
    
#     def get_name(self):
#         return self.age
  
     
#     def add_one(self,x):

#         return x + 1

# d=Emp("vivek",20)
# print(d.get_name())



# class Emp:
#     def __init__(self,name,age):
#         self.name=name
#         self.age = age

#         # print(name)
    
#     def set_age(self,age):
#         self.age = age
    

#     def get_age(self):
#         return self.age

#     def add_one(self,x):

#         return x + 1

# d=Emp("vivek",20)
# d.set_age(23)
# print(d.get_age())

# authors = ["jane austen","george orwell","james clear","cal newport"]

# author_list = [author for author in authors] 

# author_list = [author.title() for author in authors] # for capitalize first letter
# print(author_list)

# str1 = "I'm learning Python3 in 2022"

# digits = [char for char in str1 if char.isdigit()]

# print(digits)

# l_arr = [4,5,1,3]
# b_arr = [2,1,7,9]
# area = [l*b for l,b in (l_arr,b_arr)]
# print(area)

# fruits = ['blueberry','apple','banana','orange','cherry']

# starts = [fruit for fruit in fruits if fruit.startswith('b')]

# print(starts)

# item_name = "GalaxyDevices"
# sale_type = "buy"
# item_dict = {"buy_Galaxys_pip": [11111, 2232], "sell_Galaxy_tix": [2111],"profit_gap_pix":[311]}
# results = []



# item_name = "GalaxyDevices"
# sale_type = "sell"
# item_dict = {"buy_Galaxys": [11111, 2232], "sell_Galaxy": [2111]}
# item_dict = {"buy_Galaxys_bst_sdf": [11111, 2232], "sell_txt_dsf": [2111],"sell_Galaxy_txp_pst":[1122223]}

# results = []

# results = [value for key, values in item_dict.items() if (key.split('_')[0] == sale_type and key.split('_')[1] in item_name) for value in values]
# results = [ values for key, values in item_dict.items()  if key.split('_')[1] == sale_type ]
# results = [ values for key, values in item_dict.items()  if sale_type in key.split('_')  for i in sale_type.split(" ") if i == sale_type ]

# results = [ values for key, values in item_dict.items()  if sale_type in key.split('_')  for i in sale_type.split(" ") if i == sale_type ]
# print(results)




# class Student:
#     # class variables
#     school_name = 'ABC School'

#     # constructor
#     def __init__(self, name, age):
#         # instance variables
#         self.name = name
#         self.age = age
#         school_name = 'ABC School'

#     # instance variables
#     def show(self):
#         print(self.name, self.age, Student.school_name)

#     @classmethod
#     def change_School(cls, name):
#         cls.school_name = name
#         print(name)

#     @staticmethod
#     def find_notes(subject_name):
#         print(subject_name)
       


# # print(Student.school_name)

# p1 = Student("rohit",25)
# p1.show()
# Student.change_School('xyz')
# Student.find_notes('math')

# json.loads- input must be string format
# json.dumps- input must be json object

# import json
# x =  { "name":"John", "age":30, "city":"New York"}
# y = json.dumps(x)
# print(y)


# import json
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"])


# test_dict = {"list":[4,3,8,-6,7],"tupel":(9,6,89,45,3),"dict":{'b':3,'f':4,'a':7,'c':1}}



# new_dict ={keys:values for keys,values in sorted(test_dict.items(), key = lambda kv: kv[0])}

# def countdown(value):
#   call_stack = {}
#   while type(test_dict['list']) == list:
#     sorted(call_stack.update({"list":value}))
#     print("Call Stack:",call_stack)
#     value -= 1
#   print("Base Case Reached")
#   while len(call_stack) != 0:
#     print("Popping {} from call stack".format(call_stack.pop()))
#     print("Call Stack:",call_stack)
# countdown(4)

# final ={}

# final_dict = { k:val for k,val in test_dict}




# def countdown(value):

#     final_dict = {}
#     for k ,val in value.items():
#         if type(val)==dict:
          
#             d=dict(sorted(val.items(), key=lambda item: item[1]))
#             final_dict.update(d)
#         else:
#             val = test_dict[k]
#             key = k
#             final_dict.update({k:sorted(val)})
    
        

        # print(sorted(test_dict['list'].values()))


    # elif type(test_dict['tupel']) == tuple:
    #     print(sorted(test_dict['tuple'].values()))
    
    # else:
    #     print(sorted(test_dict['tuple'].values()))
    
#     return final_dict

# print(countdown(test_dict))

print("hello")