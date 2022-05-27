import math 

img_x, img_y = [640, 640]
center_x, center_y = img_x / 2, img_y / 2

x=[0, 0, 640, 640, 22, 74, 88, 478.0, 635.0, 350]
y=[0, 640, 0, 640, 114, 154, 540.0, 529.0, 217.0, 500]


for i in range(len(x)):
    a = y[i] - center_y
    b = (x[i]) - center_x
    
    myradians = math.atan2(a, b) 
    mydegrees = math.degrees(myradians) 
    if mydegrees < 0:
        mydegrees = -mydegrees + 180
    
    print(mydegrees)