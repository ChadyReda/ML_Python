import numpy as np


'''
a = np.array([1, 2, 3, 4, 5]) # cree une list de 5 elements

print(type(a))      # <class 'numpy.ndarray'>

print(a)            # afficher la list dans cmd

print(a[1])         # afficher le premier element de list 

print(a[1:])        # afficher une section de la list [de element dindex 1 jusqua la fin]

print(a[:-2])       # [1, 2, 3]

a[2] = 10           # changer lelement de index 2 du list 

'''


a_mul = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    ]
)


'''

# creation des list simples

list1 = np.zeros(3)           
# [0, 0, 0]

list2 = np.ones(4)            
# [1, 1, 1, 1]

list3 = np.arange(5)          
# [1, 2, 3, 4, 5]

list4 = np.full(2, 9)         
# [9, 9]

list5 = np.linspace(0, 10, 2) 
# [5, 5]

list6 = np.empty(3)
# [random, random, random]
'''




# arrays attributes

'''
print(a_mul.ndim)  # number of dimentions
print(a_mul.shape) # shape in form of a tuple
print(a_mul.size)  # number of elements
print(a_mul.dtype) # the type of array element
'''

# creation of basic array

a_z = np.zeros(3)               # (shape, dtype, order) create an array of zeros
a_o = np.ones(3)                # (shape, dtype, order) create an array of ones
a_e = np.empty(3)               # (shape, dtype, order) allocate the momory
a_f = np.full((2,3,4), 9)       # (shape, fill_value, dtype, order)
a_l = np.linspace(0, 100, 5)    # (first_num, last_num, numbers_to_spread_between)
a_a1 = np.arange(5)             # (final_num, dtype) array([0, 1, 2, 3, 4])
a_a2 = np.arange(2, 9, 2, dtype=np.int64) # (first_num, last_num, step_size, data_type)

# numpy data type 

'''
print(a_z.dtype)  #float
print(a_o.dtype)  #int32
print(a_a2.dtype) #int64
'''

dictionary = {"1": "A"} # dictionary (object)

array_demo1 = np.array([
    [1, 2, 3],
    [4, 5, dictionary],
    [7, 8, 9]
])

# whenever we have an element that is not a primitive
# data type the whole array get typecast into (object)
# that means dynamic typing so everything is an object

'''
print(array_demo1[1, 2]) # {'1': 'A'}
print(array_demo1.dtype) # object
'''


# Mathematicale operations

l1 = [1,2,3,4,5] # python list
l2 = [6,7,8,9,0]

array_demo2 = np.array(l1) # numpy list
array_demo3 = np.array(l2)

'''
print(l1 * 5)
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(array_demo2 * 5)
# [5 10 15 20 25]

print(array_demo2 + 5)
# [6  7  8  9 10]

print(array_demo2 * array_demo3)
# [6 14 24 36  0]

print(array_demo2 + array_demo3)
# [7  9 11 13  5]
'''

# mathematical operations

# lists a 2d

list1 = np.array([
    [1,2,3],
    [4,5,6]
])
list2 = np.array([
    [7,8,9],
    [10,11,12]
])

print(list1 * list2)
# [[ 7 16 27][40 55 72 ]]

print(list1 / list2)
# [[ 0.14285714 0.25 0.33333333 ][ 0.4 0.45454545 0.5 ]]

print(list1 + list2)
# [[ 8 10 12 ] [ 14 16 18 ]]

print(list1 - list2)
# [[ -6 -6 -6 ][ -6 -6 -6 ]]

print(list1 ** list2)
# [[ 1 256 19683 ][ 1048576 48828125 -2118184960 ]]

# produit matriciel
produit = np.dot(list1, list2)



#list1 = np.array([1, 2, 3, 4])
#list2 = np.array([5, 6, 7, 8])

'''
print(list1 * 5)
# [ 5 10 15 20]

print(list1 + 5)
# [6 7 8 9]

print(list1 * list2)
# [ 5 12 21 32]

print(list1 - list2)
# [-4 -4 -4 -4]

print(list1 / list2)
# [0.2 0.33333333 0.42857143 0.5]
'''


demo_list = np.array([
    [1,2,3],
    [4,5,6]
])

#print(np.cos(demo_list))
# [[ 0.54030231 -0.41614684 -0.9899925], [-0.65364362  0.28366219  0.96017029]]

#print(np.abs(demo_list))
# [[1 2 3], [4 5 6]]

#print(np.sqrt(demo_list))
# [[1. 1.41421356 1.73205081], [2. 2.23606798 2.44948974]]

#print(np.sin(demo_list))
# [[ 0.84147098  0.90929743  0.14112001], [-0.7568025  -0.95892427 -0.2794155 ]]

#print(np.exp(demo_list))
# [[  2.71828183   7.3890561   20.08553692], [ 54.59815003 148.4131591  403.42879349]]




# mathematical function
# http://numpy.org/doc/stable/reference/routines.math.html

# zwei demontion array
array_demo4 = np.array([
    [1,2,3],
    [4,5,6]
])

'''
print(np.cos(array_demo4))
print(np.sqrt(array_demo4))
print(np.sin(array_demo4))
print(np.exp(array_demo4))
'''

# array methods

# adding
array_demo5 = np.array([1, 2, 3])
array_demo5 = np.append(array_demo5, [7, 8, 9])     # array, array to append or element
array_demo5 = np.insert(array_demo5, 3 , [4, 5, 6]) # array, position , array to insert or element
array_demo5 = np.array_split(array_demo5, 2)
array_demo5 = np.array_equal(array_demo5, array_demo5) # true
array_demo5 = np.array2string()
#deleting
array_demo5 = np.delete(array_demo5, 1) # delete the element at index 1
 
#reshaping
array_demo6 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])



array_a_2d = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

# adition de nouveau element ou de nouveau list a la fin de la list
print(np.append(array_a_2d, [13, 14, 15, 16]))

# insersion de nouveau element ou de nouveau list a une place pricie
# en utilison lindex
print(np.insert([17, 18 ,19 ,20]))

# division de la list a troi
print(np.array_split(array_a_2d, 3))

# verifions legaliter de deux lists
print(np.array_equal([1,2,3], [1,2,3])) # True (oui)
























'''
print(array_demo6.shape) # (4,5)
# the reshape muss be compativble with the older shape
# zum biespiel : 4 x 5 = 5 x 4 "sie mussen gleich sind!"
array_demo6 = array_demo6.reshape((5,4)) 
print(array_demo6.shape) # (5, 4)
print(array_demo6)
# auch 
array_demo6 = array_demo6.reshape((20, 1))
print(array_demo6.shape)
print(array_demo6)
# auch
array_demo6 = array_demo6.reshape((10, 2))
print(array_demo6.shape)
print(array_demo6)
# auch
array_demo6 = array_demo6.reshape((2, 2, 5))
print(array_demo6.shape)
print(array_demo6)
# das applied die changes without returning
array_demo6.resize((2, 10))
print(array_demo6.shape) # (2, 10)
'''

# flatting
array_demo7 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])


var1 = array_demo7.flatten() # return a flatten copy of the original array
var2 = array_demo7.ravel()   # return the original array with a flotten view

# zum biespiel
var1[2] = 150 # the original array wont changed
var2[2] = 150 # the original array will changed

var3 = [v for v in array_demo7.flat]



# swaping rows by columns
array_demo8 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])
'''
print(array_demo8.T)
# oder
print(array_demo8.transpose())
# oder
print(array_demo8.swapaxes(0, 1))
'''

# joining and spliting arrays
array_demo9 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])
array_demo10 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])

'''
# concatenate the rows
array_demo11 = np.concatenate((array_demo9, array_demo10), axis=0)
print(array_demo11)
# concatenate the columns
array_demo11 = np.concatenate((array_demo9, array_demo10), axis=1)
print(array_demo11)

# spliting by rows
print(np.split(array_demo9, 4, axis=0))
# spliting by columns
print(np.split(array_demo9, 5, axis=1))

'''

# aggregate functions

array_demo12 = [1, 5, 6, 7, 1, 6, 9]
'''
print(np.min(array_demo12))     # min value
print(np.max(array_demo12))     # max value
print(np.mean(array_demo12))    # middle value
print(np.std(array_demo12))     # https://en.wikipedia.org/wiki/Standard_deviation
print(np.sum(array_demo12))     # total values sum
print(np.median(array_demo12))  # A median is the middle number in a sorted list of either ascending or descending numbers.
'''


# generating random numbers

# generate an array with the giving shape filled with a random float from 0 to 1
# np.random.rand(shape)
'''
random_numbers = np.random.rand(3, 2)
print(random_numbers)

# generate an array with the giving shape
# np.random.randint(max_value, size=(shape))
# np.random.randint(min_value, max_value, size=(shape))
random_numbers = np.random.randint(10, 40, size=(2, 3, 4))
print(random_numbers)

# generate a random value or array based on a percentage and a defined shape
# 10 trials and a percentage of 0.5 to hit 10
# result of flipping a coin 10 times, tested 50 times
random_numbers = np.random.binomial(10, p=0.5, size=(5, 10))
print(random_numbers)

# (mean, mean_deviation, shape)
random_numbers = np.random.normal(loc=170, scale=15, size=(5, 6))
print(random_numbers)

# (array_to_choose_from, shape)
random_numbers = np.random.choice([10, 20, 30, 40, 50], size=(2, 2))
print(random_numbers)
'''

# exporting and importing numpy arrays

array_to_export = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])

# this create a binary file that contains the the array
# np.save("myarray.npy", array_to_export)

# this saves the array as a .csv (Excel) file
# np.savetxt("myarray.csv", array_to_export ,delimiter=",")

# loading the numpy array
array_imported = np.load("myarray.npy")
#print(array_imported)

# loading the array from a excel file
array_imported = np.loadtxt("myarray.csv", delimiter=",")
#print(array_imported)



# notion des nombre complexe

# .real()  partie reel
# .imag()  partie imaginair
# .abs()   le module
# .angle() argument en radien

