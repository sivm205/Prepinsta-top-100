#Python program to find out the quadrant in which the given co-ordinate lie

''' Get value of x & y
If ( x>0 and y>0 ) First Quadrant
If ( x<0 and y>0 ) Second Quadrant
If ( x<0 and y<0 ) Third Quadrant
If ( x>0 and y>0 ) Fourth Quadrant
If ( x=0 and y=0 ) Origin
If ( x!=0 and y=0 ) x-axis
If ( x>0 and y>0 ) y-axis  '''


def get_quardant(x:int, y :int):
    if x==0 and y ==0:
        return 'origin point'
        
    elif x!=0 and y==0:
        return "on the x axis line"
        
    elif x==0 and y!=0:
        return "on the y axis line"
    
    elif x>0 and y>0:
        return "first Quadrant"
    
    elif x>0 and y<0:
        return  "Fourth Quadrant"
        
    elif x<0 and y >0:
        return "Second Quadrant"
        
    elif x<0 and y<0 :
        return "Third Quadrant"
    
    else:
        return 0
        
        
inp1 = int(input("enter the X value\n"))
inp2 = int(input("enter the y value\n"))
print(get_quardant(inp1, inp2))
        
    

















