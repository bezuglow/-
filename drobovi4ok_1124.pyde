

#                                                 игра убеги от керпичей              


#                                                                                                золотая подписка 100 рублей
#управление                                                                                         получишь новые скины.
#пауза-p
#распауза-o                                                               описание: ваш персонаж мужик который решил построить
#рестарт-a                                                                сарай но у него не было денег на кирпичи и он решил
#хардкор режим-s                                                          накрасть кирпичей со стройки но после кражи первого 
#сменить фон-ё                                                            кирпича дом начинает падать вам надо уворачиваться 
#рестарт в хардкоре-s                                                     от падающих с него кирпичей.
#
#версия 0.8 кипичи эдишон
# 











q=0
w=0
e=0

r=6
t=9
y=7

d=245
f=115
g=42

c=255
v=0
b=0

z=41
x=198
s=211



def setup():
    global q,w,e,r,t,y,d,f,g,c,v,b,z,x,s
    size(1000,1000)

def draw():
    
    
    global q,w,e,r,t,y,d,f,g,c,v,b,z,x,s
    background(z,x,s)
    
    
    
    if keyPressed:
        if key=='p':
            r=0   
            t=0
            y=0
            
    if keyPressed:
        if key=='o':
            r=6   
            t=9
            y=7
            
    if keyPressed:
        if key=='m':
           d=248
           f=252
           g=31
           c=40
           v=250
           b=206
           z=(203)
           x=(14)
           s=(157)
            
            
    if keyPressed:
        if key=='`':                      
            z=(random(1,255))
            x=(random(1,255))
            s=(random(1,255))
            
    
    if keyPressed:
        if key=='s':                      
            r=12
            t=16
            y=13
            q=0
            w=0
            e=0           
    
    if keyPressed:
        if key=='a':
            r=6
            t=9
            y=7
            q=0
            w=0
            e=0
            
    
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
    
    # hfty
    
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
    

    
    if collidePointRect(mouseX, 500, 500, q, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        text(u"ты нашёл баг , поздравляю  но",200,200)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 284, w, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
              
    if collidePointRect(mouseX, 500, 986, q, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        text(u"получено достежение на краю экрана",40,300)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 146, e, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 1, e, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 937, w, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(30)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 748, q, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 638, e, 30, 60):
        background(242,22,22)   
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 948, w, 30, 60):
        background(242,22,22)   
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 671, e, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 65, w, 30, 60):
        background(242,22,22)   
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 96, e, 30, 60):
        background(242,22,22)  
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 346, q, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 83, w, 30, 60):
        background(242,22,22)   
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 267, e, 30, 60):
        background(242,22,22)  
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 648, q, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 662, w, 30, 60):
        background(242,22,22)   
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 474, e, 30, 60):
        background(242,22,22)  
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 345, q, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)   
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
 #разделитель верха и низа      
        
                 
    if collidePointRect(mouseX, 500, 986, q, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        text(u"получено достежение на краю экрана",40,300)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 285, w, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 147, e, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 2, e, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 938, w, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(30)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 749, q, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 639, e, 30, 60):
        background(242,22,22)   
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 949, w, 30, 60):
        background(242,22,22)   
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 672, e, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 66, w, 30, 60):
        background(242,22,22)   
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 97, e, 30, 60):
        background(242,22,22)  
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 347, q, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 84, w, 30, 60):
        background(242,22,22)   
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 268, e, 30, 60):
        background(242,22,22)  
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 649, q, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 663, w, 30, 60):
        background(242,22,22)   
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 475, e, 30, 60):
        background(242,22,22)  
        text(u"ты проиграл",500,500)
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
    if collidePointRect(mouseX, 500, 346, q, 30, 60):
        background(242,22,22)
        text(u"ты проиграл",500,500)   
        textSize(50)  
        fill(64,98,227)
        r=0
        t=0
        y=0
        
        
    fill(c,v,b) #zxcvbcvbnmdfyuicvbnmdfghixfghjvhfdgzdfghjnjuygdtyukrt5erhtycgtryvvtreyvrrteri
    ellipse(mouseX,500,20,20) 
        
    fill(d,f,g)  
   
    if e>=1000: e=0
    if w>=1000: w=0
    if q>=1000: q=0
    e=e+r 
    w=w+t
    q=q+y


 
def collidePointRect(pointX, pointY, x, y, xW, yW):

    if (pointX >= x) and (pointX <= x + xW) and (pointY >= y) and (pointY <= y + yW): 
        return True
    return False
     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
