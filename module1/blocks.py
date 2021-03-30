blocks = int(input("Enter the number of blocks"))

i = 0

if blocks == 1 :

    height = 1 

    print("height =",height)

elif blocks > 1 :

    height = 1

    for i in range(1,blocks+1) :
    
        blocks = blocks - i 
            
    
        if blocks > i :
            
            height = height + 1
                
        else : 
            
            break

                
    print("height : ",height)
    
