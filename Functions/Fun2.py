#Reversing using the reverse() mathod in python

def Rev(x):
    x.reverse() #<--- function for reversing 
    return x

#Reversing using the slicing technique
def Rev2(x):
    var = x[::-1]
    return var



lst = [1,2,3,4]
print(Rev(lst))
#Output: [4,3,2,1]
lst2 = [1,2,3,4]
print(Rev2(lst2))
#Output: [4,3,2,1]


