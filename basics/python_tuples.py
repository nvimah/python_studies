#tuples
#they are immutable - they can not be modified
tuple_1 = ('math', 'history')

#sets
#unordered values that have no duplicates
set_1 = {'math', 'physics'}
#used to remove duplicates
#used to check whether a value in part of a set
#determine what values they share with other sets
cs_courses = {'History', 'Math', 'Physics', 'compsci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))#intersection shows similar courses
#difference shows the courses they dont share
#union joins the two sets- still doesn't include duplicates
#emptylist = list()
#emptytuple = tuple()
#emptyset = set()
