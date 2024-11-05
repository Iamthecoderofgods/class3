import pgzrun

WIDTH=500
HEIGHT=500


#Rect((x,y),(width,hight))
def draw():
    r = 255
    g = 0
    b=  0
    w = 200
    h = 100
    for i in range(20):
        rect = Rect((0,0),(w, h))
        rect.center = 250,250
        screen.draw.rect(rect,(r,g,b))
        w = w-10
        h = h+10
        r = r-10
        g = g+11
        b = b+4
        r = r+10


pgzrun.go()