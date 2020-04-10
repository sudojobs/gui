# Simple pygame program


# Import and initialize the pygame library

import pygame
from pygame import *
import math
import time
import sys
#Colour Definition

trans      = (0, 0, 0, 0)
grey       = (115,111,111)
red        = (219,33,41)
stop_red   = (245,3,3)
start_green= (3,245,3)
white      = (255,255,255)
black      = (0,0,0)
button     = (30,160 , 160, 50)
rect_set   = (120,240 , 375, 30)

#Font Size Definition
b1=90
h1=55
s1=40
h2=35
h3=25
h4=20
h5=15
h6=10


#Menu Y Cordinates
select_item=150
spacer=70
first_item =select_item + spacer 
second_item=first_item + spacer 
third_item =second_item + spacer
fourth_item=third_item + spacer
fivth_item =fourth_item + spacer
sixth_item =fivth_item  + spacer

pygame.init()


# Set up the drawing window

width=1280
height=800

screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()

state=["UMC750","VFS22","VF2","VM-3","TM3-P","Robodrill"]

#Images used
gearimg = pygame.image.load('gear.png')
m1= pygame.image.load('UMC750.png')
m1f= pygame.image.load('UMC750t.png')
m2= pygame.image.load('VF2SS.png')
m2f= pygame.image.load('VF2SSt.png')
m3= pygame.image.load('VF2.png')
m3f= pygame.image.load('VF2t.png')
m4= pygame.image.load('VM_3.png')
m4f= pygame.image.load('VM_3t.png')
m5= pygame.image.load('Tm3_P.png')
m5f= pygame.image.load('Tm3_Pt.png')
m6= pygame.image.load('Robodrill.png')
m6f= pygame.image.load('Robodrillt.png')
right= pygame.image.load('right.png')
left=  pygame.image.load('left.png')
up=pygame.image.load('up.png')
down=pygame.image.load('down.png')
lt1=pygame.image.load('left_1.png')
rt1=pygame.image.load('right_1.png')
#g1=pygame.image.load('gear.svg')
count=5
gallon=1
add5=5
add1=1
sub1=1
sub5=5
setting=0
strt=0
stp=0
index=0
start_delay=0
def gear(x,y):
    screen.blit(gearimg, (x,y))

def image_load(img,x,y):
    screen.blit(img, (x,y))

def create_font(t,s=55,c=white, b=False,i=False):
    font = pygame.font.SysFont("Arial", s, bold=b, italic=i)
    text = font.render(t, True, c)
    return text

def display(txt,x,y):
    screen.blit(txt,(x,y))

#def machine_trans(m1):
#    print("clear")
#    select.fill(transparent)

# Text to be rendered with create_font    
Banner = create_font("COOLANT AUTOMATION SYSTEM")
tap    = create_font("TAP TO SELECT", 20, black)
tapc   = create_font("TAP TO SELECT", 20, white)
select = create_font("QUICK SELECT", h2,b=True)
txtm1  = create_font("UMC 750",h2)
txtm2  = create_font("VF2SS",h2)
txtm3  = create_font("VF2",h2)
txtm4  = create_font("VM-3",h2)
txtm5  = create_font("TM3-P",h2)
txtm6  = create_font("Robodrill",h2)
footer = create_font("Designed & Created by Roka Automation",h6,(67,70,75))
start  = create_font("START",s1,white,b=True)
stop   = create_font("STOP",s1,white,b=True)
backp  = create_font("BACK",h2)
backw  = create_font("BACK",h2,black,b=True)
timer  = create_font("START",h4,white,b=True)
s      = create_font("s Delay",h4,white,b=True)
sec    = create_font(str(count),h4,white,b=True)
sb     = create_font("SECONDS",h4,black,b=True)
secb   = create_font(str(count),b1,black)
gal    = create_font(str(gallon),b1,black,b=True)
gals   = create_font(str(gallon),b1,black,b=True)
adb5b  = create_font(str(add5),b1,black,b=True)
adb5   = create_font(str(add5),h3,black,b=True)
ad1    = create_font(str(add1),h3,black,b=True)
ad5    = create_font(str(add5),h3,black,b=True)
sb1    = create_font(str(sub1),h3,black,b=True)
sb5    = create_font(str(sub5),h3,black,b=True)
sa     = create_font("+",h3,black,b=True) 
ss     = create_font("-",h3,black,b=True) 
g      = create_font("GAL",h3,black,b=True)
sh1    = create_font("Default Starting Quantity",h3,black,b=True)
sh2    = create_font("Default Double Chevron QTY",h3,black,b=True)
sh3    = create_font("Start Delay Seconds",h3,black,b=True)

m1click = 0
m2click = 0
m3click = 0
m4click = 0
m5click = 0
m6click = 0

m1on   =  0
m2on   =  0
m3on   =  0
m4on   =  0
m5on   =  0
m6on   =  0


m1off  =  0
m2off  =  0
m3off  =  0
m4off  =  0
m5off  =  0
m6off  =  0

running = True

def on_m1():
    print("Switch ON Machine1")

def off_m1():
    print("Switch 0FF Machine1")

def on_m2():
    print("Switch ON Machine2")

def off_m2():
    print("Switch 0FF Machine2")

def on_m3():
    print("Switch ON Machine3")

def off_m3():
    print("Switch 0FF Machine3")

def on_m4():
    print("Switch ON Machine4")

def off_m4():
    print("Switch 0FF Machine4")

def on_m5():
    print("Switch ON Machine5")

def off_m5():
    print("Switch 0FF Machine5")

def on_m6():
    print("Switch ON Machine6")

def off_m6():
    print("Switch 0FF Machine6")



def vertical_frame():
    pygame.draw.rect(screen, grey, pygame.Rect(920,120, width/3, height))

def horizontal_frame():
    pygame.draw.rect(screen, red, pygame.Rect(0, 0, width, 120))
    display(Banner,10,25)
    display(footer,20,780)

def highlight(x,y): 
    pygame.draw.rect(screen,red, pygame.Rect(x,y , width/3, 50))

def main_frame():
    horizontal_frame()
    vertical_frame()

def drawCircle(pos,size,c=(0,255,0),w=0):
    pygame.draw.circle(screen,c,pos,size,w) # Here <<<

def drawCircleB(pos,size,thick,c=(255,212,59)):
    pygame.draw.circle(screen,c,pos,size,thick) # Here <<<

def menu(index):
    display(select,980,select_item)
    if(index==0):
       image_load(m1,90,150)
       image_load(right,750,350)
       pygame.draw.rect(screen,red, pygame.Rect(920,first_item-5 , width/3, 50))
       display(txtm1,1020,first_item)
       display(txtm2,1035,second_item)
       display(txtm3,1050,third_item)
       display(txtm4,1045,fourth_item)
       display(txtm5,1035,fivth_item)
       display(txtm6,1020,sixth_item)
    elif(index==1):
       image_load(m2,90,150)
       image_load(right,750,350)
       image_load(left,100,350)
       display(txtm1,1020,first_item)
       pygame.draw.rect(screen,red, pygame.Rect(920,second_item-5 , width/3, 50))
       display(txtm2,1035,second_item)
       display(txtm3,1050,third_item)
       display(txtm4,1045,fourth_item)
       display(txtm5,1035,fivth_item)
       display(txtm6,1020,sixth_item)
    elif(index==2):
       image_load(m3,180,180)
       image_load(right,750,350)
       image_load(left,100,350)
       display(txtm1,1020,first_item)
       display(txtm2,1035,second_item)
       pygame.draw.rect(screen,red, pygame.Rect(920,third_item-5 , width/3, 50))
       display(txtm3,1050,third_item)
       display(txtm4,1045,fourth_item)
       display(txtm5,1035,fivth_item)
       display(txtm6,1020,sixth_item)
    elif(index==3):
       image_load(m4,180,180)
       image_load(right,750,350)
       image_load(left,100,350)
       display(txtm1,1020,first_item)
       display(txtm2,1035,second_item)
       pygame.draw.rect(screen,red, pygame.Rect(920,fourth_item-5 , width/3, 50))
       display(txtm3,1050,third_item)
       display(txtm4,1045,fourth_item)
       display(txtm5,1035,fivth_item)
       display(txtm6,1020,sixth_item)
    elif(index==4):
       image_load(m5,200,210)
       image_load(right,750,350)
       image_load(left,100,350)
       display(txtm1,1020,first_item)
       display(txtm2,1035,second_item)
       pygame.draw.rect(screen,red, pygame.Rect(920,fivth_item-5 , width/3, 50))
       display(txtm3,1050,third_item)
       display(txtm4,1045,fourth_item)
       display(txtm5,1035,fivth_item)
       display(txtm6,1020,sixth_item)
    elif(index==5):
       image_load(m6,230,270)
       image_load(right,750,350)
       image_load(left,100,350)
       display(txtm1,1020,first_item)
       display(txtm2,1035,second_item)
       pygame.draw.rect(screen,red, pygame.Rect(920,sixth_item-5 , width/3, 50))
       display(txtm3,1050,third_item)
       display(txtm4,1045,fourth_item)
       display(txtm5,1035,fivth_item)
       display(txtm6,1020,sixth_item)

    display(tap,400,720)

def back_button(col,bor):
    pygame.draw.rect(screen, col, pygame.Rect(button))
    pygame.draw.rect(screen, bor, pygame.Rect(button),4)
    display(backp,62,165)

def back_buttonw(col,bor):
    pygame.draw.rect(screen, col, pygame.Rect(button))
    pygame.draw.rect(screen, bor, pygame.Rect(button),4)
    display(backw,62,165)

def start_button(bg):
    right.fill(trans)
    image_load(bg,90,150)
    display(tapc,350,650)
    drawCircle((380,400),85)
    drawCircleB((380,400),87,6,black)
    drawCircle((590,400),60)
    drawCircleB((590,400),62,6,black)
    display(start,316,378)
    display(timer,560,373)
    display(sec,550,398)
    display(s,572,398)
    back_button(grey,black)

def stop_button():
    drawCircle((480,400),90,stop_red)
    drawCircleB((480,400),92,6,black)
    display(stop,430,375)

def side_pannel():
    vertical_frame()
    highlight(920,140)
    display(txtm1,1020,145)
    drawCircle((1100,450),90,white)
    drawCircle((1099,449),92,red,6)
    if(gallon<10):
       display(gal,1070,400)
    else:   
       display(gal,1050,400)
    display(g,1110,480)
    display(up,1060,200)
    display(up,1060,230)
    display(up,1060,300)
    display(down,1060,560)
    display(down,1060,630)
    display(down,1060,660)
    drawCircle((1170,230),30,white)
    drawCircle((1170,230),32,red,2)
    drawCircle((1170,330),30,white)
    drawCircle((1170,330),32,red,2)
    drawCircle((1170,570),30,white)
    drawCircle((1170,570),32,red,2)
    drawCircle((1170,670),30,white)
    drawCircle((1170,670),32,red,2)
    display(sa,1155,212)
    display(ad5,1170,215)
    display(sa,1155,315)
    display(ad1,1170,315)
    display(ss,1155,555)
    display(sb1,1170,555)
    display(ss,1155,655)
    display(sb5,1170,655)

def settings_menu():
    horizontal_frame()
    pygame.draw.rect(screen, grey, pygame.Rect(0,120 , width, height))
    back_buttonw(white,black)
    pygame.draw.rect(screen, white, pygame.Rect(120,240 , 375, 30))
    pygame.draw.rect(screen, black, pygame.Rect(120,240 , 375, 30),3)
    pygame.draw.rect(screen, white, pygame.Rect(120,510 , 375, 30))
    pygame.draw.rect(screen, black, pygame.Rect(120,510 , 375, 30),3)
    pygame.draw.rect(screen, white, pygame.Rect(720,240 , 375, 30))
    pygame.draw.rect(screen, black, pygame.Rect(720,240 , 375, 30),3)
    drawCircle((300,350),70,white)
    drawCircle((300,620),70,white)
    drawCircle((900,350),70,white)
    image_load(lt1,120,300)
    image_load(lt1,170,300)
    image_load(lt1,120,580)
    image_load(lt1,170,580)
    image_load(lt1,720,300)
    image_load(lt1,770,300)
    image_load(rt1,400,300)
    image_load(rt1,450,300)
    image_load(rt1,400,580)
    image_load(rt1,450,580)
    image_load(rt1,1000,300)
    image_load(rt1,1050,300)
    display(gals,275,290)
    display(g,275,380)
    if(add5>9):
        display(adb5b,245,560)
    else:
        display(adb5b,275,560)
    display(g,275,650)
    if(count<10):
        display(secb,875,290)
    else:
        display(secb,855,290)
    display(sb,850,380)
    display(sh1,160,240)
    display(sh2,130,510)
    display(sh3,800,240)

def touch(pos,x1,y1,x2,y2):
    if(x > x1 and y > y1 and x < x2 and y < y2):
       return 1
    else:
       return 0

def stop_menu(img):
    image_load(img,90,150)
    display(tapc,350,650)
    stop_button()
    side_pannel()
    back_button(grey,black)

temp=0
while running:
    # Did the user click the window close button?
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
           pos = pygame.mouse.get_pos()
           print (pos) 
        if event.type == pygame.MOUSEBUTTONUP:
           pos = pygame.mouse.get_pos()
           print (pos) 
           x,y = pos
           sqx = (x - 380) ** 2
           sqy = (y - 400) ** 2
           spx = (x - 440) ** 2
           spy = (y - 400) ** 2
           sdx = (x - 590) ** 2
           sdy = (y - 400) ** 2

           if(touch(pos,158,190,640,600) and m1click==0 and setting==0 and index==0 ):
              m1click=1
           if(touch(pos,158,190,640,600) and m2click==0 and setting==0 and index==1):
              m2click=1
           if(touch(pos,158,190,640,600) and m3click==0 and setting==0 and index==2):
              m3click=1
           if(touch(pos,158,190,640,600) and m4click==0 and setting==0 and index==3):
              m4click=1
           if(touch(pos,158,190,640,600) and m5click==0 and setting==0 and index==4):
              m5click=1
           if(touch(pos,158,190,640,600) and m6click==0 and setting==0 and index==5):
              m6click=1
           if(touch(pos,1160,17,1236,93) and setting==0):
              setting=1 
           if(touch(pos,751,353,873,474) and setting==0 and m1click==0 and index==0):
              index+=1
              break
           if(touch(pos,751,353,873,474) and setting==0 and m1click==0 and index==1):
              index+=1
              break
              print("here2")
           if(touch(pos,751,353,873,474) and setting==0 and m1click==0 and index==2):
              index+=1
              break
           if(touch(pos,751,353,873,474) and setting==0 and m1click==0 and index==3):
              index+=1
              break
           if(touch(pos,751,353,873,474) and setting==0 and m1click==0 and index==4):
              index+=1
              break
           if(touch(pos,751,353,873,474) and setting==0 and m1click==0 and index==5):
              index=0
              break
           if(touch(pos,101,351,223,474) and setting==0 and m1click==0 and index==1):
              index-=1
              break
           if(touch(pos,101,351,223,474) and setting==0 and m1click==0 and index==2):
              index-=1
              break
           if(touch(pos,101,351,223,474) and setting==0 and m1click==0 and index==3):
              index-=1
              break
           if(touch(pos,101,351,223,474) and setting==0 and m1click==0 and index==4):
              index-=1
              break
           if(touch(pos,101,351,223,474) and setting==0 and m1click==0 and index==5):
              index-=1
              break
           #if(touch(pos,1110,20,1192,112) and setting==0 and m1click==1 and index==0):
           #   setting=1 
           if(touch(pos,30,160,190,210) and setting==1):
              setting=0
              m1click=0
           if(touch(pos,30,160,190,210) and setting==1):
              setting=0
              m1click=1
           if(touch(pos,30,160,190,210) and setting==0):
              setting=0
              m1click=0
              m2click=0
              m3click=0
              m4click=0
              m5click=0
              m6click=0
           if(touch(pos,1064,304,1130,338) and setting==0 ):
              if(gallon<99):
                 gallon+=1 
              gal    = create_font(str(gallon),b1,black,b=True)
              if(gallon<10):
                 display(gal,1070,400)
              else: 
                 display(gal,900,400)
           if(touch(pos,1064,578,1130,602) and setting==0 and m1click==1 and index==0):
              if(gallon>1):
                 gallon-=1 
              gal    = create_font(str(gallon),b1,black,b=True)
              if(gallon<10):
                 display(gal,1070,400)
              else: 
                 display(gal,900,400)
           if(touch(pos,1064,202,1130,252) and setting==0 and m1click==1 and index==0):
              if(gallon<99-add5):
                 gallon+=add5 
              gal    = create_font(str(gallon),b1,black,b=True)
              if(gallon<10):
                 display(gal,1070,400)
              else: 
                 display(gal,900,400)
           if(touch(pos,1064,650,1130,697) and setting==0 and m1click==1 and index==0):
              if(gallon>sub5+1):
                 gallon-=sub5 
              gal    = create_font(str(gallon),b1,black,b=True)
              if(gallon<10):
                 display(gal,1070,400)
              else: 
                 display(gal,900,400)
           #Circle Click Check
           if ((math.sqrt(sqx + sqy) < 80 ) and (m1click==1) and strt==0 and index==0) :
              strt=1
              stp=0
              print(math.sqrt(sqx+sqy))
           #Circle Click Check   
           if ((math.sqrt(spx + spy) < 90 ) and (m1click==1) and stp==1 and index==0) :
              print ("inside")
              strt=0
              m1click=1
              start_delay=0
              if(m1off==0):
                 off_m1()
                 m1on=0
                 m1off=1
              print(math.sqrt(sqx+sqy))
           #Circle Click Check
           if ((math.sqrt(sdx + sdy) < 60 ) and (m1click==1) and strt==0 and index==0 and start_delay==0) :
              start_delay=1
              strt=1
              temp=count
              stp=0
              print(math.sqrt(sdx+sdy))
           #Setting Bar
           if(touch(pos,401,301,443,369) and setting==1):
              if(gallon<9):
                 gallon+=1;
                 print(gallon)
                 gals    = create_font(str(gallon),b1,black,b=True)
                 gal    = create_font(str(gallon),b1,black,b=True)
           if(touch(pos,171,301,211,369) and setting==1):
              if(gallon>1):
                 gallon-=1;
                 print(gallon)
                 gals    = create_font(str(gallon),b1,black,b=True)
                 gal    = create_font(str(gallon),b1,black,b=True)
           if(touch(pos,120,301,160,369) and setting==1):
              if(gallon>2):
                 gallon-=2;
                 print(gallon)
                 gals    = create_font(str(gallon),b1,black,b=True)
                 gal    = create_font(str(gallon),b1,black,b=True)
           if(touch(pos,470,301,510,369) and setting==1):
              if(gallon<8):
                 gallon+=2;
                 print(gallon)
                 gals    = create_font(str(gallon),b1,black,b=True)
                 gal    = create_font(str(gallon),b1,black,b=True)
           if(touch(pos,1000,301,1040,369) and setting==1):
              if(count<99):
                 count+=1;
                 sec    = create_font(str(count),h4,white,b=True)
                 secb   = create_font(str(count),b1,black)
           if(touch(pos,770,301,810,369) and setting==1):
              if(count>1):
                 count-=1;
                 sec    = create_font(str(count),h4,white,b=True)
                 secb   = create_font(str(count),b1,black)
           if(touch(pos,720,301,760,369) and setting==1):
              if(count>6):
                 count-=5;
                 sec    = create_font(str(count),h4,white,b=True)
                 secb   = create_font(str(count),b1,black)
           if(touch(pos,1050,301,1090,369) and setting==1):
              if(count<95):
                 count+=5;
                 sec    = create_font(str(count),h4,white,b=True)
                 secb   = create_font(str(count),b1,black)
           if(touch(pos,401,580,443,650) and setting==1):
              if(add5<25):
                 add5+=1;
                 sub5=add5
                 adb5b  = create_font(str(add5),b1,black,b=True)
                 ad5   = create_font(str(add5),h3,black,b=True)
                 sb5    = create_font(str(sub5),h3,black,b=True)
           if(touch(pos,171,580,211,650) and setting==1):
              if(add5>5):
                 add5-=1;
                 sub5=add5
                 adb5b  = create_font(str(add5),b1,black,b=True)
                 ad5   = create_font(str(add5),h3,black,b=True)
                 sb5    = create_font(str(sub5),h3,black,b=True)
           if(touch(pos,120,580,160,650) and setting==1):
              if(add5>9):
                 add5-=5;
                 sub5=add5
                 adb5b  = create_font(str(add5),b1,black,b=True)
                 ad5   = create_font(str(add5),h3,black,b=True)
                 sb5    = create_font(str(sub5),h3,black,b=True)
           if(touch(pos,470,580,510,650) and setting==1):
              if(add5<21):
                 add5+=5;
                 sub5=add5
                 adb5b  = create_font(str(add5),b1,black,b=True)
                 ad5   = create_font(str(add5),h3,black,b=True)
                 sb5    = create_font(str(sub5),h3,black,b=True)
          # Circle Click Check
          # if ((math.sqrt(sqx + sqy) < 80 ) and (m2click==1) and strt==0 and index==1) :
          #    print ("inside")
          #    strt=1
          #    stp=0
          #    print(math.sqrt(sqx+sqy))
          # #Circle Click Check   
          # if ((math.sqrt(spx + spy) < 90 ) and (m2click==1) and stp==1 and index==1) :
          #    print ("inside")
          #    strt=0
          #    m2click=1
          #    print(math.sqrt(sqx+sqy))



# Add this somewhere after the event pumping and before the display.flip()
    screen.fill((255, 255, 255))
    main_frame()
    image_load(gearimg,1160,15)

    if(index==0):
       if(m1click==0 and setting==0):
          menu(index)
          right= pygame.image.load('right.png')
          image_load(right,750,350)
       elif(setting==1): 
          settings_menu()
       elif(strt==1 and m1click==1 and start_delay==0):
          if(m1on==0):
              on_m1()
              m1on=1
              m1off=0
          stop_menu(m1f)
          stp=1
       elif(strt==1 and m1click==1 and start_delay==1):
          time.sleep(1)
          temp-=1
          sec    = create_font(str(temp),h4,white,b=True)
          start_button(m1f)
          side_pannel()
          if(temp==0):
             stp=1
             stop_menu(m1f)
             start_delay=0
             sec    = create_font(str(count),h4,white,b=True)
             if(m1on==0):
                on_m1()
                m1on=1
                m1off=0
       elif(m1click==1 and setting==0):
          start_button(m1f)
          side_pannel()
    elif(index==1):   
       if(m2click==0 and setting==0):
          menu(index)
          right= pygame.image.load('right.png')
          image_load(right,750,350)
       elif(setting==1): 
          settings_menu()
       elif(strt==1 and m2click==1 and start_delay==0):
          stop_menu(m2f)
          stp=1
       elif(m2click==1 and setting==0 and start_delay==1):  
          time.sleep(1)
          temp-=1
          sec    = create_font(str(temp),h4,white,b=True)
          start_button(m2f)
          side_pannel()
          if(temp==0):
             stp=1
             stop_menu(m2f)
             start_delay=0
             sec    = create_font(str(count),h4,white,b=True)
       elif(m2click==1 and setting==0):  
          start_button(m2f)
          side_pannel()
    elif(index==2):      
       if(m3click==0 and setting==0):
          menu(index)
          right= pygame.image.load('right.png')
          image_load(right,750,350)
       elif(setting==1): 
          settings_menu()
       elif(strt==1 and m3click==1 and start_delay==0):
          stop_menu(m3f)
          stp=1
       elif(m3click==1 and setting==0 and start_delay==1):  
          time.sleep(1)
          temp-=1
          sec    = create_font(str(temp),h4,white,b=True)
          start_button(m3f)
          side_pannel()
          if(temp==0):
             stp=1
             stop_menu(m3f)
             start_delay=0
             sec    = create_font(str(count),h4,white,b=True)
       elif(m3click==1 and setting==0):  
          start_button(m3f)
          side_pannel()
    elif(index==3):      
       if(m4click==0 and setting==0):
          menu(index)
          right= pygame.image.load('right.png')
          image_load(right,750,350)
       elif(setting==1): 
          settings_menu()
       elif(strt==1 and m4click==1 and start_delay==0):
          stop_menu(m4f)
          stp=1
       elif(m4click==1 and setting==0 and start_delay==1):  
          time.sleep(1)
          temp-=1
          sec    = create_font(str(temp),h4,white,b=True)
          start_button(m4f)
          side_pannel()
          if(temp==0):
             stp=1
             stop_menu(m4f)
             start_delay=0
             sec    = create_font(str(count),h4,white,b=True)
       elif(m4click==1 and setting==0):  
          start_button(m4f)
          side_pannel()
    elif(index==4):      
       if(m5click==0 and setting==0):
          menu(index)
          right= pygame.image.load('right.png')
          image_load(right,750,350)
       elif(setting==1): 
          settings_menu()
       elif(strt==1 and m5click==1 and start_delay==0):
          stop_menu(m5f)
          stp=1
       elif(m5click==1 and setting==0 and start_delay==1):  
          time.sleep(1)
          temp-=1
          sec    = create_font(str(temp),h4,white,b=True)
          start_button(m5f)
          side_pannel()
          if(temp==0):
             stp=1
             stop_menu(m5f)
             start_delay=0
             sec    = create_font(str(count),h4,white,b=True)
       elif(m5click==1 and setting==0):  
          start_button(m5f)
          side_pannel()
    elif(index==5):      
       if(m6click==0 and setting==0):
          menu(index)
          right= pygame.image.load('right.png')
          image_load(right,750,350)
       elif(setting==1): 
          settings_menu()
       elif(strt==1 and m6click==1 and start_delay==0):
          stop_menu(m6f)
          stp=1
       elif(m6click==1 and setting==0 and start_delay==1):  
          time.sleep(1)
          temp-=1
          sec    = create_font(str(temp),h4,white,b=True)
          start_button(m6f)
          side_pannel()
          if(temp==0):
             stp=1
             stop_menu(m6f)
             start_delay=0
             sec    = create_font(str(count),h4,white,b=True)
       elif(m6click==1 and setting==0):  
          start_button(m6f)
          side_pannel()
    pygame.display.flip()
  

pygame.quit()
