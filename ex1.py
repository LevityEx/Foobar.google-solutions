index = 10000

sti = ''


for n in range(2, 20000*2):
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:  
        sti += str(n)    

print( sti[index : index + 5] )   

