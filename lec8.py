def my_function(a,b=0):
    
    print(a)
   
    
    result = a +b
    
    return result
     
    print(b)
    
#

#ex1 cal abs values

def cal_abs(a):
    
    if type(a) is str:
        return ('wrong data type')
    elif a >=0:
        return a
        
    else:
        return -a
print(cal_abs(-1)) 

#ex2

def cal_s(n,m):
    
    result = 0
    
    for i in range(n,m+1):
        
        result = result + i
        
    return result
    
print(cal_sigma(1,6))    