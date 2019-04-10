fc = 2

hrng = PVector(-1,1)
ns = 1e-3
nd = 9999
maxIter = 4
rot = -tan(.5)*0

posi = PVector(0,0)
psft = PVector(-.5,-1.5)
Ri = 90
rdiv = 2.
hi = .25
wd = 1080/fc; ht = wd

def settings():
    size(wd,ht)

def setup():
    global P
    rectMode(RADIUS)
    colorMode(HSB,1.)
    background(0)
    # noFill()
    # noStroke()
    ###
    P = syst(posi,psft,Ri,hi)
    translate(width/2,height/2)
    rotate(rot)
    P.show()

def draw():
    translate(width/2,height/2)
    rotate(rot)
    
    P.iter()
    

##########################

class particle():
    def __init__(self,pos,R,h):
        self.pos = pos
        self.R = R
        self.h = h
        self.b = 1
    
    def show(self):
        stroke(self.h,1,self.b)
        fill(self.h,1,1)
        rect(self.pos.x,self.pos.y,self.R,self.R)

class syst():
    def __init__(self,pos,shift,R,h):
        self.pos = pos
        self.r = R
        self.shift = shift
        self.shifts = []
        for i in xrange(4):
            v = shift.copy()
            v.rotate(PI/2*i)
            self.shifts.append(v)
        self.h = h
        self.p = [particle(self.pos,R,h)]
        self.iters = 0
        
    def show(self):
        for i in xrange(len(self.p)):
            self.p[i].show()
    
    def iter(self):
        if self.iters >= maxIter or self.r < 1:
            print "Done.\niter =",self.iters, "r =", self.r
            self.p = []
            noLoop()
            # return
        newp = []
        for i in xrange(len(self.p)):
            # self.p[i].show()
            ch = self.p[i].h
            R = self.p[i].R; nR = R/rdiv
            self.r = R
            x = self.p[i].pos.x; y = self.p[i].pos.y
            for j in xrange(4):
                nx = x + R*self.shifts[j].x
                ny = y + R*self.shifts[j].y
                hs = map(noise((nx+nd)*ns,(ny+nd)*ns),
                         0,.8,hrng.x,hrng.y)
                nh = hloop(ch + self.h + hs)
                np = particle(PVector(nx,ny),nR,nh)
                np.show()
                newp.append(np)
        self.p = newp[:]
        self.iters += 1

#############

def hloop(h):
    return h - floor(h)
