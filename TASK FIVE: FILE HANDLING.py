#1.	Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError

def syntax_func (x):
    try:
        print(x/0
    except SyntaxError:
        print("Exception")
    finally:
        print("The 'try except' is finished")


syntax_func(5)

#2.
	      
import sys

def func_fileOpen():
    try:

        filename = str(sys.argv[0])
        txt_file = open(filename, 'r')
        print(txt_file)

    except:

        filename = input('Exception:  Entered name is incorrect,Please enter the name again.')
        txt_file  = open(filename, 'r')
        print(txt_file )

func_fileOpen()



#3.

while True:
     user_input = input("Enter the number: ")
     try:
          if len(user_input) > 4:
               raise Exception (print("Please length is too short/long !!! Please provide only four digits"))
          elif len(user_input) <= 4:
               print("execution complte")
               break
     except Exception :
          pass
     finally:
          pass
	      
#4. 
	      

def login_page():
    UserEmail = input("Enter you Useremail: ")
    password = input("Enter your password: ")
    stored_password = "1234"
    #stored_UserEmail ="rahul@gmail.com"
    count=0
    if password !="1234":
        print("Incorrect Password,Re-Type Password")
        while count<3:
            password = input("Enter your password: ")
            if password != "1234":
                print("Incorrect Password,Re-Type Password")
                count=count+1
            else:
                print("log in SucessFull")
    else:
        print("Login Sucessfull")
	      
#5. 	https://www.programiz.com/python-programming/exception-handling Go through this link to understand Finally and
	      Raise concept.
	      
The finally keyword is used in try...except blocks. It defines a block of code to run when the try...except...else block is final.
The finally block will be executed no matter if the try block raises an error or not.

The raise keyword is used to raise an exception.You can define what kind of error to raise, and the text to print to the user.

#6. 
	      
file_open = open('doc','r')
file_string=[]
file_length=[]
for data in file_open:
     file_string.append((data[0:-1]))
     file_length.append(len(data))

final_zip = list(zip(file_string,file_length))
final1 = { k:v  for k,v in final_zip   if (v %2==0)}

print(final1)
