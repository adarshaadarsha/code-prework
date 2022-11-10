def func(n, y):

     if n<y:
          arr = [[0 for i in range(n)] for j in range(y)]
          p = 1

          for k in range(n*y):
               j = k   
               i = 0

               while (j >= 0):
                    try:
                         arr[j][i] = p 
                    except:
                         break
                    p += 1 
                    i = i + 1  
                    j = j - 1

          
          for k in range(1, y, 1):
               i = k 
               j = y - 1
               f = k
               while (j >= f):
                    try:
                         arr[j][i] = p 
                    except:
                         break
                    p += 1   
                    i = i + 1 
                    j = j - 1

          for i in range(0, y, 1):
               for j in range(0, n, 1):
                    print(arr[i][j], end = " ")
               print("\n", end = "")
     else:

          arr = [[0 for i in range(n)] for j in range(y)]
          p = 1
         
          for k in range(n*y):
               
               j = k
               i = 0

               while (j >= 0):
                    try:
                         arr[j][i] = p
                    except:
                         break
                    p += 1
                    i = i + 1
                    j = j - 1


          for k in range(1, c, 1):
               i = k
               j = y - 1
               f = k
               while (i < j):
                    try:
                         arr[j][i] = p
                         p += 1
                         i = i + 1
                         j = j - 1
                    except:
                         p = p - 1     
                         break
               while (0 <= j):
                    try:
                         arr[j][i] = p
                         p += 1
                         i = i + 1
                         j = j - 1
                    except:
                         break
                    
          for i in range(0, y, 1):
               for j in range(0, n, 1):
                    print(arr[i][j], end = " ")
               print("\n", end = "")
          

c = int(input("Enter column: "))

r = int(input("Enter row: "))

func(c,r)

