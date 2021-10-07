# import thread6
# import time

# 	# Define a function for the thread
# def print_time( threadName, delay):
# 	count = 0
# 	while count < 5:
# 		time.sleep(delay)
# 		count += 1
# 		print("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 	# Create two threads as follows
# try:
# 	thread6.start_new_thread( print_time, ("Thread-1", 2, ) )
# 	thread6.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
# 	print("Error: unable to start thread")

# # while 1:
# # 	pass 	 

# def divide(x,y):  
#     print(x/y)  
# def outer_div(func):  
#     def inner(x,y):  
#         if(x<y):  
#         	x,y = y,x  
#         return func(x,y)  
#     return inner  
# divide1 = outer_div(divide)  
# divide1(2,4)  	

# import functools  

# class Count_Calls:  
# 	def __init__(self, func):  
# 		functools.update_wrapper(self, func)  
# 		self.func = func  
# 		self.num_calls = 0  

# 	def __call__(self, *args, **kwargs):  
# 		self.num_calls += 1  
# 		print(f"Call{self.num_calls} of {self.func.__name__!r}")  
# 		return self.func(*args, **kwargs)  

# @Count_Calls  
# def say_hello():  
# 	print("Say Hello")  

# say_hello()  
# say_hello()  
# say_hello()  	
	
# Generators in python
# def simple():  
# 	for i in range(10):  
# 		if(i%2==0):  
# 			yield i  

# #Successive Function call using for loop  
# for i in simple():  
# 	print(i)  	


# multiple yield statement in function
# def multiple_yield():  
#     str1 = "First String"  
#     yield str1  
  
#     str2 = "Second string"  
#     yield str2  
  
#     str3 = "Third String"  
#     yield str3  
# obj = multiple_yield()  
# print(next(obj))  
# print(next(obj))  
# print(next(obj))	

# Generator list comprehension instead of for loop
# list = [1,2,3,4,5,6,7]  
  
# # List Comprehension  
# z = [x**3 for x in list]  
  
# # Generator expression  
# a = (x**3 for x in list)  
  
# print(a)  
# print(z) 	
	

# using next instead of for loop
# list = [1,2,3,4,5,6]  

# z = (x**3 for x in list)  

# print(next(z))  

# print(next(z))  

# print(next(z))  

# print(next(z)) 
 	
# Write a program to print the table of the given number using the genrator	
# n  = int(input("Enter Number:"))
# def table(n):
#     for i in range(1,11):
#         yield i*n
#         i = i+1
# for i in table(n):
#     print(i)


# import sys  
# # List comprehension  
# nums_squared_list = [i * 2 for i in range(1000)]  
# print(sys.getsizeof("Memory in Bytes:", nums_squared_list))  
# # Generator Expression  
# nums_squared_gc = (i ** 2 for i in range(1000))  
# print(sys.getsizeof("Memory in Bytes:", nums_squared_gc))  	
	
# iterator using count(start,stop)
# import itertools  

# for i in itertools.count(10,5):  
# 	if i == 50:  
# 		break  
# 	else:  
# 		print(i,end=" ")  	

# iterator using Cycle()

# import itertools
# temp = 0
# for i in itertools.cycle("5490"):
#     if temp>7:
#         break
#     else:
#         print(i,end=" ")
#     temp =  temp + 1


# import itertools  

# val = ['Java', 'T', 'Point']  

# iter = itertools.cycle(val)  

# for i in range(6):  
# 	# Using next function  
# 	print(next(iter), end = " ")  	
	

# import itertools  
# print("Printing the number repeadtly:")  
# print(list(itertools.repeat(40,100)))  	



# from itertools import product  

# print("We are computing cartesian product using repeat Keyword Argument:")  
# print(list(product([1, 2], repeat=2)))  
# print()  

# print("We are computing cartesian product of the containers:")  
# print(list(product(['Java', 'T', 'point'], '5')))  
# print()  

# print("We are computing product of the containers:")  
# print(list(product('CD', [4, 5]))) 



# from itertools import combinations_with_replacement  
  
# print("Combination of string in sorted order(with replacement) is:")  
# print(list(combinations_with_replacement("XY", 3)))  
# print()  
  
# print("Combination of list in sorted order(with replacement) is:")  
# print(list(combinations_with_replacement([4, 2], 3)))  
# print()  
  
# print("Combination of container in sorted order(with replacement) is:")  
# print(list(combinations_with_replacement(range(3), 2))) 	
	

# import itertools  
# import operator  

# # initializing list 1  
# list1 = [2,9,86]  

# # using accumulate() that will prints the successive summation of elements  
# print("The sum is : ", end="")  
# print(list(itertools.accumulate(list1)))  

# # using accumulate() that will prints the successive multiplication of elements  
# print("The product is : ", end="")  
# print(list(itertools.accumulate(list1, operator.mul)))  


# # using accumulate() that will prints the successive summation of elements  
# print("The sum is : ", end="")  
# print(list(itertools.accumulate(list1)))  

# # using accumulate() that will prints the successive multiplication of elements  
# print("The product is : ", end="")  
# print(list(itertools.accumulate(list1, operator.mul)))  	
	



# import itertools  
# print(" The combined value of iterrables is :")  
# print(*(itertools.zip_longest('Java', 'Tpoint', fillvalue='_')))  	
	


    
 
# from tkinter import *  
# parent = Tk()  
# redbutton = Button(parent, text = "Red", fg = "red")  
# redbutton.pack( side = LEFT)  
# greenbutton = Button(parent, text = "Black", fg = "black")  
# greenbutton.pack( side = RIGHT )  
# bluebutton = Button(parent, text = "Blue", fg = "blue")  
# bluebutton.pack( side = TOP )  
# blackbutton = Button(parent, text = "Green", fg = "red")  
# blackbutton.pack( side = BOTTOM)  
# parent.mainloop()   	


    
 
# from tkinter import *  
# parent = Tk()  
# name = Label(parent,text = "Name").grid(row = 0, column = 0)  
# e1 = Entry(parent).grid(row = 0, column = 1)  
# password = Label(parent,text = "Password").grid(row = 1, column = 0)  
# e2 = Entry(parent).grid(row = 1, column = 1)  
# submit = Button(parent, text = "Submit").grid(row = 10, column = 0)  
# parent.mainloop()   				 
	

      
# from tkinter import *   
     
# top = Tk()  
      
# top.geometry("200x100")  
      
# b = Button(top,text = "simple",activeforeground="red",bd=10,highlightcolor="green")  
      
# b.pack()  

# top.mainloop()   				


    
# from tkinter import *
# import tkinter
# from tkinter import messagebox
# top = Tk()  
      
# top.geometry("200x100")  
      
# def fun():  
#     tkinter.messagebox.showerror("Hello","Red Button clicked",)  
      
      
# b1 = Button(top,text = "Red",
# 	        command = fun,
# 			activeforeground = "red",
# 			activebackground = "pink",
# 			pady=10)  
      
# b2 = Button(top,text = "Blue",
# 			activeforeground = "blue",
# 			activebackground = "pink",
# 			pady=10)  
      
# b3 = Button(top,text = "Green",
# 			activeforeground = "green",
# 			activebackground = "pink",
# 			pady = 10)  
      
# b4 = Button(top,text = "Yellow",
# 			activeforeground = "yellow",
# 			activebackground = "pink",
# 			pady = 10)  

# b1.pack(side = LEFT)  
      
# b2.pack(side = RIGHT)  
      
# b3.pack(side = TOP)  
      
# b4.pack(side = BOTTOM)  
      
# top.mainloop()   				 
	
    
# from tkinter import *   
      
# top = Tk()  
      
# top.geometry("200x200")  
      
#     #creating a simple canvas  
# c = Canvas(top,
# 	bg = "grey",
# 	height = "200")  
      
      
# c.pack()  
      
# top.mainloop()   	

    
# from tkinter import *   
      
# top = Tk()  
  
# top.geometry("200x200")  
      
#     #creating a simple canvas  
# c = Canvas(top,bg = "pink",
# 	height = "200",
# 	width = 200)  
      
# arc = c.create_arc(
# 		(10,10,200,150),
# 		start = 0,
# 		extent = 150,
# 		fill= "white")  
      
# c.pack()  
      
# top.mainloop()   

			 
    
# from tkinter import *   
      
# top = Tk()  
      
# top.geometry("200x200")  
      
# checkvar1 = IntVar()  
      
# checkvar2 = IntVar()  
    
# checkvar3 = IntVar()  
    
# chkbtn1 = Checkbutton(top,
#         text = "C", 
#         variable = checkvar1, 
#         onvalue = 1, 
#         offvalue = 0, 
#         height = 2, 
#         width = 10)  
    
# chkbtn2 = Checkbutton(top, 
#         text = "C++", 
#         variable = checkvar2, 
#         onvalue = 1, 
#         offvalue = 0, 
#         height = 2, 
#         width = 10)  
    
# chkbtn3 = Checkbutton(top, 
#         text = "Java", 
#         variable = checkvar3, 
#         onvalue = 1, 
#         offvalue = 0, 
#         height = 2, 
#         width = 10)  
    
# chkbtn1.pack()  
    
# chkbtn2.pack()  
    
# chkbtn3.pack()  
    
# top.mainloop()   				 

	
  # !/usr/bin/python3  

# from tkinter import *  

# top = Tk()  

# top.geometry("400x250")  

# name = Label(top, 
#     text = "Name").place(x = 30,
#     y = 50)  

# email = Label(top, 
#     text = "Email").place(x = 30, 
#     y = 90)  

# password = Label(top, 
#     text = "Password").place(x = 30, 
#     y = 130)  

# sbmitbtn = Button(top, 
#     text = "Submit",
#     activebackground = "pink", 
#     activeforeground = "blue").place(x = 30, 
#     y = 170)  

# e1 = Entry(top).place(x = 80, 
#     y = 50)  


# e2 = Entry(top).place(x = 80, 
#     y = 90)  


# e3 = Entry(top).place(x = 95, 
#     y = 130)  

# top.mainloop()  				 

            
    
# from tkinter import *  
      
# top = Tk()  
# top.geometry("140x100")  
# frame = Frame(top)  
# frame.pack()  
    
# leftframe = Frame(top)  
# leftframe.pack(side = LEFT)  
    
# rightframe = Frame(top)  
# rightframe.pack(side = RIGHT)  
    
# btn1 = Button(frame, 
#     text="Submit", fg="red",
#     activebackground = "red")  
# btn1.pack(side = LEFT)  
    
# btn2 = Button(frame, 
#     text="Remove", fg="brown", 
#     activebackground = "brown")  
# btn2.pack(side = RIGHT)  
    
# btn3 = Button(rightframe, 
#     text="Add", fg="blue", 
#     activebackground = "blue")  
# btn3.pack(side = LEFT)  
    
# btn4 = Button(leftframe, 
#     text="Modify", fg="black", 
#     activebackground = "white")  
# btn4.pack(side = RIGHT)  
    
# top.mainloop()   				 
	
    
#   # !/usr/bin/python3  
      
# from tkinter import *  
    
# top = Tk()  
    
# top.geometry("400x250")  
    
# #creating label  
# uname = Label(top, 
#     text = "Username").place(x = 30,
#     y = 50)  
    
# #creating label  
# password = Label(top, 
#     text = "Password").place(x = 30, 
#     y = 90)  
    
    
# sbmitbtn = Button(top, 
#     text = "Submit",
#     activebackground = "pink", 
#     activeforeground = "blue").place(x = 30, 
#     y = 120)  
    
# e1 = Entry(top,
#     width = 20).place(x = 100, 
#     y = 50)  
    
    
# e2 = Entry(top, 
#     width = 20).place(x = 100, 
#     y = 90)  
    
    
# top.mainloop()   				 
	
# from tkinter import *  

# top = Tk()  

# top.geometry("200x250")  

# lbl = Label(top,
#     text = "A list of favourite countries...")  

# listbox = Listbox(top)  

# listbox.insert(1,"India")  

# listbox.insert(2, "USA")  

# listbox.insert(3, "Japan")  

# listbox.insert(4, "Austrelia")  

# lbl.pack()  
# listbox.pack()  

# top.mainloop()  	 				 

	
from tkinter import *  

top = Tk()  

top.geometry("200x250")  

lbl = Label(top,
    text = "A list of favourite countries...")  

listbox = Listbox(top)  

listbox.insert(1,"India")  

listbox.insert(2, "USA")  

listbox.insert(3, "Japan")  

listbox.insert(4, "Austrelia")  

#this button will delete the selected item from the list   

btn = Button(top, text = "delete", 
    command = lambda listbox=listbox: listbox.delete(ANCHOR))  

lbl.pack()  


listbox.pack()  

btn.pack()  
top.mainloop()   				 
	