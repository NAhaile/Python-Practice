def recursive_add(n):
    if n == 1: #<---- Base case, if n ever becomes 1 then return 1 because you cant go any lower
        return n
    else:
        return n+recursive_add(n-1) #<----- recursive call, this is where the magic happens
        
        
        
print(recursive_add(5)) #<----- This will print out 15 ie: 5+4+3+2+1 = 15
    
