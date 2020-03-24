smallest=None
largest=-1
while True:
    	
     num=input('Enter the values')
        
     if(num=='done'):
            break
     
     try:
               num= int(num)
                
   
     except:
                    print('Invalid input')
                    continue
       
     if smallest is None:
                smallest=num
     
     if num> largest:
                  largest=num
                    
     elif num<smallest:
        		smallest=num
                
print('Maximum is',largest)
print('Minimum is',smallest)
