Web VPython 3.2
body = sphere(radius = 0.5,color = color.red,texture = "https://i.postimg.cc/pLD3cKgF/541339a6c39cebf8483dfab75f3bd709a85a89e35de7219c01b34bd88cd486c5.png")
arm1 = box(pos=vec(0,1,0))
arm2 = box(pos=vec(0,-1,0))
roling ball = compound([body,arm1,arm2])
while True :
    rate(100)
    k = keysdown()
    if 'd' in k :
        s.pos.x += 0.1
    if 'a' in k :
        s.pos.x -= 0.1

2차시 
Web VPython 3.2
import random
body = sphere(radius=0.5)
arm1 = box(pos=vec(0.3,0.38,0),size = vec(0.5,0.2,0.3),color = color.blue)
arm2 = box(pos=vec(-0.3,0.38,0),size = vec(0.5,0.2,0.3),color = color.red)

rolling_ball = compound([body,arm1,arm2])

for i in range(100):
   z = -1+i * 3
   map = box(pos=vec(0,-0.6,z),size=vec(3.4,0.3,3),color=vec(0.2,0.8,0))
s = rolling_ball
while True :
    rate(100)
    k = keysdown()
    if 'd' in k :
        s.pos.x += 0.1
    if 'a' in k :
        s.pos.x -= 0.1
        
