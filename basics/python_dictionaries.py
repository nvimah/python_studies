#Dictionaries
#allow as to work with key value pairs
#have a key and a value
student = {'name': 'John', 'Age': '25', 'courses': ['math', 'compsci']}
print(student)#prints all the values ad keys in relation to the student
print(student['courses'])#prints values at a specific index
#print(student['phone'])# an error is displayed when a key is absent
print(student.get('phone'))#displays none if a key is absent
print(student.get('phone', 'Not found'))#displays not found if the key is absent
student['phone'] = '555-555-555'#adds a key if it already exists it updates the existing one
student.update({'name': 'Mike', 'Age': '17'})#updates multiple keys at a go
del student['Age']#deletes a key
age = student.pop('age')#deletes and prints the deleted value
print(len(student))#returns the number of things in our dictionary
print(student.key())#prints all the values in a dictionary
print(student.values())#prints out all the values
print(student.items())#prints both the keys and values
for key,value in student.items():
    print(key, value)#loops through a dictionary and prints the keys and values
    
