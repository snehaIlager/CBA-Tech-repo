#arrays, lists and dictioanries
import array
 
array_1 = array.array('i',([5,4,7,222,3,4]))
print(type(array_1))

array_1.append(43)
print(array_1)
array_1[3]=50
print(array_1)
array_1.remove(4)
print(array_1)
array_1.reverse()
print(array_1)