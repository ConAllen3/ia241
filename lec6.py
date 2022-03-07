'''
lec6 
'''

for item in ['a', 'b', 'c']:
    
    print(item)

demo_string = 'this is my string'    

for c in demo_string:
    print(c)
    
for word in demo_string.split():
    print(word)
    
for num in range(5):    
    print(num)
    
for num in range(1,5):
    print(num)
    
for num in range(1,5,2):
    print(num)


num_list = [1,12,3,1,2]

max_item = num_list[0]

for num in num_list:
    if max_item<= num:
        max_item = num
        
print(max_item)        