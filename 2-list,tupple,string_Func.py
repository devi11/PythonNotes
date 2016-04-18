
# Lists
print "$$ Learning Lists \n" # \n newline

mylist = []     #creating empty list
mylist.append(1)
mylist.append(2)
mylist.append(3)
print mylist

stringlist=[]
stringlist= [ "John" , "Eric" , "Jessica"]  # 0 indexing
print stringlist[0]
print stringlist[-2]  # negative indexing

print ("The last person's name is %s" % stringlist[2])

#*******************************************************************************
# Arithmetic operators

square= 7 ** 2
cube= 4 ** 3
print ("square of 7 is %s" %square )
print ("cube of 4 is %s" %cube)

lotsofhellos = "hello" * 5
print lotsofhellos

print [1,2,3] * 3

odds=[1,3,5,7]
even=[2,4,6,8]
whole= odds + even
print whole

#General info
i=1000
print i.bit_length() # gives the number of bits reqd for storing

# To know what a function does
l=[1,2,3]
print l.reverse.__doc__

#*******************************************************************************
# List functions

l=[1,2,3]
print type(l)

print dir(l) # gives the functions of type list

# o/p
#['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__',
#  '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
#  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
#  '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__',
#  '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']

l.append(5)     # adds number 5 to the end of the list ; function does not return value
l.append(3)      # adds number 3 to the end of the list ;
print l
# o/p [1, 2, 3, 5]

print l.count(3)  # counts the number of 3's
#o/p 2

print l.index(1)  # gives the position(index as we call it) of the number 1
#o/p 0      # index starts from 0

print l.index(3)
# o/p 2

print l.index(7)
# Error false value

print l.pop() # removes the last entry from the list
# o/p 3
# [1, 9, 2, 3, 5]

l.insert(1,9) # inserts 9 in index 1 ; function does not return value
print l
# [1, 9, 2, 3, 5]

l.remove(2) # removes the particular list entry; function does not return value
# o/p [1, 9, 3, 5]

l.reverse() # reverses the list ; function does not return value
# o/p [5, 3, 9, 1]

l.sort() # sorts the list in ascending order ; function does not return value
# o/p [1, 3, 5, 9]

l2=['a', 'b', 'c']
l.extend(l2)    # extends the list by adding l2 to l ; function does not return value
print l
# o/p [1, 3, 5, 9, 'a', 'b', 'c']

#*******************************************************************************
# TUPPLE functions

t=(1,2,3,4)
print type(t)

print dir(t)

# ['__add__', '__class__', '__contains__','__delattr__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
# '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__',
# '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count',
# 'index']

# tupple is immutable so no insert remove or append kind of functions

print t.count(1)      # counts the number of 1's in the tupple
# o/p 1

print t.index(1)      # returns the index of the element
# o/p 0

#*******************************************************************************
# STRING functions

s='mississippi'
s2='i am learning\t python!!'
print dir(s)

# ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
#  '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__',
#  '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
#  '__subclasshook__', '_formatter_field_name_split', '_formatter_parser',
#  'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs',
#  'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
#  'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace',
#  'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
#  'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

print s.capitalize()      # Capitalizes the 1st alphabet of the word
# o/p 'Mississippi'
print s2.capitalize()
# o/p 'I am learning\t python!!'


print s2.center(30,'$')   # Centers the string with leading and trailing given argument ,
# o/p '$$$$i am learning\t python!!$$$$'    # total length is 30

print s.count('s')    # counts the number of s
# o/p 4

print "Encoded string:" + s2.encode(encoding='UTF-8',errors='strict') # encode a string with type of encoding,error

print "Decoded String:" +  s2.decode(encoding='UTF-8',errors='strict') # decodes the encoded string

print s.endswith('i')   # Boolean T/F
# o/p TRUE
print s2.endswith('am',2,4)  # is the suffix(a part of string) between start and end position

print "Original:" + s2
print "Expanded: " + s2.expandtabs(30)   # to extend the tab space

print s.find('s')   # finds the index of first occurance of the argument
# o/p 2
print s.find('z')
# o/p -1   # default value for argument not found

print s2.find('l',2,9)   # find 'l' between 2 and 9 indexes
# o/p 5

s.index('s')    # returns the index value of the argument
#o/p 2
s.index('z')
# o/p substring not found   # throws an error

s2.index('l',2,9)
#o/p 5

s.isalnum()     # boolean , returns False is it contains other than alphabets or numeric
#o/p True
s2.isalnum()
#o/p False

s.isalpha()     # boolean, check if it has only alphabets
#o/p True

s.isdigit()     # boolean, check if it contains only numbers
#o/p False

s.lower()           # Output the string to with lower case ; original value not changed
s.upper()          #  Outputs the string with upper case ; original value not changed
s2.title()          # Outputs the string with all words having 1st letter upper case
#o/p 'I Am Learning\t Python!!'
s.islower()          # boolean , to check if it is all lower case
s.isupper()         #boolean, to check if its all in upper case
s.isspace()         # boolean, to check if its just blank space
s.istitle()          #boolean , to check if its titled

s.startswith('M')   # Boolean, checks if the string starts with the given argument
# o/p False         # case sensitive

','.join(s)         # fill in between the string
'm,i,s,s,i,s,s,i,p,p,i'

a=s.ljust(30)                # adds spaces on the left side, for a total len of 30
# o/p 'mississippi                   '

b= s.rjust(30)               # adds spaces on the left side, for a total len of 30
# o/p  '                  mississippi'
a.lstrip()                   # strips spaces on left side
b.rstrip()                    #strips spaces on right side
c= '       spaces on both sides         '
c.strip()                    # strips spaces on both sides

c.split()                    # splits at default space
# o/p  ['spaces', 'on', 'both', 'sides']
c.split('s')                 # splits whenever it encounters the given argument
# o/p   ['       ', 'pace', ' on both ', 'ide', '         ']

s.swapcase()                # outputs changed upper to lower or vice versa

s.replace('s','c',3)        # outputs changed 's' to 'c' for 3 encounters
# o/p   'miccicsippi'

s.zfill(30)                 # adds zeros to fill up 30 character space
#o/p '0000000000000000000mississippi'







