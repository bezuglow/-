
q=0
w=0
e=0
def setup():
    global q,w,e
    size(1000,1000)

def draw():
    
    
    global q,w,e
    background(41,198,211)
    
    if collidePointRect(mouseX, 500, 500, q, 30, 60):
        background(242,22,22)



    if collidePointRect(mouseX, 500, 284, w, 30, 60):
        background(242,22,22)


    if collidePointRect(mouseX, 500, 146, e, 30, 60):
        background(242,22,22)
        
    if collidePointRect(mouseX, 500, 1, e, 30, 60):
        background(242,22,22)

    if collidePointRect(mouseX, 500, 937, w, 30, 60):
        background(242,22,22)

    if collidePointRect(mouseX, 500, 748, q, 30, 60):
        background(242,22,22)
        
    if collidePointRect(mouseX, 500, 638, e, 30, 60):
        background(242,22,22)   
            
   
    if collidePointRect(mouseX, 500, 948, w, 30, 60):
        background(242,22,22)   
        
    if collidePointRect(mouseX, 500, 671, e, 30, 60):
        background(242,22,22)
        
    if collidePointRect(mouseX, 500, 65, w, 30, 60):
        background(242,22,22)   
        
    if collidePointRect(mouseX, 500, 96, e, 30, 60):
        background(242,22,22)  
        
    if collidePointRect(mouseX, 500, 346, q, 30, 60):
        background(242,22,22)
        
    if collidePointRect(mouseX, 500, 83, w, 30, 60):
        background(242,22,22)   
        
    if collidePointRect(mouseX, 500, 267, e, 30, 60):
        background(242,22,22)  
        
    if collidePointRect(mouseX, 500, 648, q, 30, 60):
        background(242,22,22)
        
    if collidePointRect(mouseX, 500, 662, w, 30, 60):
        background(242,22,22)   
        
    if collidePointRect(mouseX, 500, 474, e, 30, 60):
        background(242,22,22)  
        
    if collidePointRect(mouseX, 500, 345, q, 30, 60):
        background(242,22,22)
             
        
    fill(255,0,0)
    ellipse(mouseX,500,20,20)
        
    fill(245,133,42)
    rect(500,q,30,60)
    rect(284,w,30,60)    
    rect(146,e,30,60)
    rect(1,e,30,60)
    rect(937,w,30,60)
    rect(748,q,30,60)
    rect(638,e,30,60)
    rect(948,w,30,60)
    rect(171,e,30,60)
    rect(65,w,30,60)
    rect(96,e,30,60)
    rect(346,q,30,60)
    rect(83,w,30,60)
    rect(267,e,30,60)
    rect(648,q,30,60)
    rect(662,w,30,60)
    rect(474,e,30,60)
    rect(345,q,30,60)
    rect(986,q,30,60)
    if e>=1000: e=0
    if w>=1000: w=0
    if q>=1000: q=0
    e=e+3 
    w=w+7
    q=q+5


 
def collidePointRect(pointX, pointY, x, y, xW, yW):

    if (pointX >= x) and (pointX <= x + xW) and (pointY >= y) and (pointY <= y + yW): 
        return True
    return False
     
                
                    
                        
                            
                                
                                    
                                        
                                            
                                                
                                                    
                                                        
                                                            
                                                                
                                                                    
                                                                            
  
 









































    
