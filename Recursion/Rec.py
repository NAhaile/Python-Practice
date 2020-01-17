def recursive_add(n):
    if n == 1:
        return n
    else:
        return n+recursive_add(n-1)
        
        
        
print(recursive_add(5))
    