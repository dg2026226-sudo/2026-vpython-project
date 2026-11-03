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
