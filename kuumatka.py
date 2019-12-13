import numpy as np
mMaa = 5.974*pow(10,24)
mKuu = 7.348*pow(10,22)
G = 6.67428*pow(10,-11)
maaSade = 6371*10**3
kuuSade = 1737.1*10**3
RMaaKuu = 384400*10**3
R = 0
deltaT = 100
v0 = 12000
deltaV = 150
paasiko = True
paasikoEnnen = True
vIteraatio = v0
while (True) :

    R = 0
    f = -G*(mMaa/((maaSade+R)**2))+G*(mKuu/((RMaaKuu-maaSade-R)**2))
    vavg = 0
    v1 = deltaT*f+v0
    vavg = (v1+v0)/2

    while (R<=RMaaKuu-kuuSade-maaSade) :
    
        R = vavg*deltaT+R
        f = -G*(mMaa/((maaSade+R)**2))+G*(mKuu/((RMaaKuu-maaSade-R)**2))
        v1 = deltaT*f + v1
        vavg = (v1+vavg)/2
        if (v1<0) :
            paasiko = False
            break

    if (R>=RMaaKuu-kuuSade-maaSade) :
        paasiko = True

    if(deltaV<=0.001 and paasiko==True):
        print('pienin mahdollinen nopeus on ',v0)
        break

    if(((paasiko==True and paasikoEnnen==False)or(paasiko==False and paasikoEnnen==True))and (deltaV>0.001)):
        deltaV = deltaV/2
        print(deltaV)

    if (paasiko==True):
        v0 = v0 - deltaV
        paasikoEnnen = True

    if (paasiko==False):
        v0 = v0 + deltaV
        paasikoEnnen = False

tiedostonNimi = 'kuumatkanopeuksia.txt'
with open(tiedostonNimi, 'a') as siirtaja:
    siirtaja.write('nopeus ja aika-askel: ')
    siirtaja.write(str(v0))
    siirtaja.write(' , ')
    siirtaja.write(str(deltaT))
    siirtaja.write('\n')
