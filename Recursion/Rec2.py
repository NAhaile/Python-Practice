
def recursive_add(n):
    if n == 1: #<---- Base case, if n ever becomes 1 then return 1 because you cant go any lower
        return n
    else:
        return n*recursive_add(n-1) #<----- recursive call, this is where the recursion happens
        
        
        
print(recursive_add(5)) #<----- Similarly to addition we can do multiplication this will print out 120 ie; 5*4*3*2*1 = 120
