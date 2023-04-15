a= [] 
count= 0 
  
for i in range(8): 
                b = input() 
                a.append(list(b)) 
  
for i in range(8): 
        for j in range(8): 
         if((i+j) % 2 == 0) and (a[i][j] == "F"): 
                        count+= 1 
  
print(count) 
