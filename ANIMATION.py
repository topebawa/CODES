##"""      turtle-example-suite:
##
##         tdemo_round_dance.py
##
##(Needs version 1.1 of the turtle module that
##comes with Python 3.1)
##
##Dancing turtles have a compound shape
##consisting of a series of triangles of
##decreasing size.
##
##Turtles march along a circle while rotating
##pairwise in opposite direction, with one
##exception. Does that breaking of symmetry
##enhance the attractiveness of the example?
##
##Press any key to stop the animation.
##
##Technically: demonstrates use of compound
##shapes, transformation of shapes as well as
##cloning turtles. The animation is
##controlled through update().
##"""
##
##from turtle import *
##
##def stop():
##    global running
##    running = False
##
##def main():
##    global running
##    clearscreen()
##    bgcolor("gray10")
##    tracer(False)
##    shape("triangle")
##    f =   0.793402
##    phi = 9.064678
##    s = 5
##    c = 1
##    # create compound shape
##    sh = Shape("compound")
##    for i in range(10):
##        shapesize(s)
##        p =get_shapepoly()
##        s *= f
##        c *= f
##        tilt(-phi)
##        sh.addcomponent(p, (c, 0.25, 1-c), "black")
##    register_shape("multitri", sh)
##    # create dancers
##    shapesize(1)
##    shape("multitri")
##    pu()
##    setpos(0, -200)
##    dancers = []
##    for i in range(180):
##        fd(7)
##        tilt(-4)
##        lt(2)
##        update()
##        if i % 12 == 0:
##            dancers.append(clone())
##    home()
##    # dance
##    running = True
##    onkeypress(stop)
##    listen()
##    cs = 1
##    while running:
##        ta = -4
##        for dancer in dancers:
##            dancer.fd(7)
##            dancer.lt(2)
##            dancer.tilt(ta)
##            ta = -4 if ta > 0 else 2
##        if cs < 180:
##            right(4)
##            shapesize(cs)
##            cs *= 1.005
##        update()
##    return "DONE!"
##
##if __name__=='__main__':
##    print(main())
##    mainloop()



#######


















#!/usr/bin/env python3
"""       xturtle-example-suite:

          xtx_kites_and_darts.py

Constructs two aperiodic penrose-tilings,
consisting of kites and darts, by the method
of inflation in six steps.

Starting points are the patterns "sun"
consisting of five kites and "star"
consisting of five darts.

For more information see:
 http://en.wikipedia.org/wiki/Penrose_tiling
 -------------------------------------------
"""
from turtle import *
from math import cos, pi
from time import clock, sleep

f = (5**0.5-1)/2.0   # (sqrt(5)-1)/2 -- golden ratio
d = 2 * cos(3*pi/10)

def kite(l):
    fl = f * l
    lt(36)
    fd(l)
    rt(108)
    fd(fl)
    rt(36)
    fd(fl)
    rt(108)
    fd(l)
    rt(144)

def dart(l):
    fl = f * l
    lt(36)
    fd(l)
    rt(144)
    fd(fl)
    lt(36)
    fd(fl)
    rt(144)
    fd(l)
    rt(144)

def inflatekite(l, n):
    if n == 0:
        px, py = pos()
        h, x, y = int(heading()), round(px,3), round(py,3)
        tiledict[(h,x,y)] = True
        return
    fl = f * l
    lt(36)
    inflatedart(fl, n-1)
    fd(l)
    rt(144)
    inflatekite(fl, n-1)
    lt(18)
    fd(l*d)
    rt(162)
    inflatekite(fl, n-1)
    lt(36)
    fd(l)
    rt(180)
    inflatedart(fl, n-1)
    lt(36)

def inflatedart(l, n):
    if n == 0:
        px, py = pos()
        h, x, y = int(heading()), round(px,3), round(py,3)
        tiledict[(h,x,y)] = False
        return
    fl = f * l
    inflatekite(fl, n-1)
    lt(36)
    fd(l)
    rt(180)
    inflatedart(fl, n-1)
    lt(54)
    fd(l*d)
    rt(126)
    inflatedart(fl, n-1)
    fd(l)
    rt(144)

def draw(l, n, th=2):
    clear()
    l = l * f**n
    shapesize(l/100.0, l/100.0, th)
    for k in tiledict:
        h, x, y = k
        setpos(x, y)
        setheading(h)
        if tiledict[k]:
            shape("kite")
            color("black", (0, 0.75, 0))
        else:
            shape("dart")
            color("black", (0.75, 0, 0))
        stamp()

def sun(l, n):
    for i in range(5):
        inflatekite(l, n)
        lt(72)

def star(l,n):
    for i in range(5):
        inflatedart(l, n)
        lt(72)

def makeshapes():
    tracer(0)
    begin_poly()
    kite(100)
    end_poly()
    register_shape("kite", get_poly())
    begin_poly()
    dart(100)
    end_poly()
    register_shape("dart", get_poly())
    tracer(1)

def start():
    reset()
    ht()
    pu()
    makeshapes()
    resizemode("user")

def test(l=200, n=4, fun=sun, startpos=(0,0), th=2):
    global tiledict
    goto(startpos)
    setheading(0)
    tiledict = {}
    a = clock()
    tracer(0)
    fun(l, n)
    b = clock()
    draw(l, n, th)
    tracer(1)
    c = clock()
    print("Calculation:   %7.4f s" % (b - a))
    print("Drawing:  %7.4f s" % (c - b))
    print("Together: %7.4f s" % (c - a))
    nk = len([x for x in tiledict if tiledict[x]])
    nd = len([x for x in tiledict if not tiledict[x]])
    print("%d kites and %d darts = %d pieces." % (nk, nd, nk+nd))

def demo(fun=sun):
    start()
    for i in range(8):
        a = clock()
        test(300, i, fun)
        b = clock()
        t = b - a
        if t < 2:
            sleep(2 - t)

def main():
    #title("Penrose-tiling with kites and darts.")
    mode("logo")
    bgcolor(0.3, 0.3, 0)
    demo(sun)
    sleep(2)
    demo(star)
    pencolor("black")
    goto(0,-200)
    pencolor(0.7,0.7,1)
    write("Please wait...",
          align="center", font=('Arial Black', 36, 'bold'))
    test(600, 8, startpos=(70, 117))
    return "Done"

if __name__ == "__main__":
    msg = main()
    mainloop()













