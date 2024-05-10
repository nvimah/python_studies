#they are used to handle errors 
try:
    f = open("testfile.txt")
    var = bad_var
except FileNotFoundError:
    print("Sorry . This file does not exist")
except Exception as e:#prints the exact line with the error
    print(e)
else:#rus the code if the exception is not hit
    pass
finally: #runs no matter what happens,whether their is an error or not
    print("executing my finally")