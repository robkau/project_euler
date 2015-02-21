"""       
PROBLEM:  
          
APPROACH: See if the built in math and string processing can handle this in reasonable time.
          
RESULT:   It works in less than a second.
           
"""

sum = 0
num = 2**1000
for i in range(len(str(num))):
    sum += int(str(num)[i])

print(str(sum))

"""
OUTPUT:   
          
"""