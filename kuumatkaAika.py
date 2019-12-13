import numpy as np
mMaa = 5.974*pow(10,24)
mKuu = 7.348*pow(10,22)
G = 6.67428*pow(10,-11)
maaSade = 6371*10**3
kuuSade = 1737.1*10**3
RMaaKuu = 384400*10**3

deltaT = 100 #maksimi jolla pääsee kuuhun on 281

v0 = 11073.963890
v0 = v0*1.1
aika = 0
R = 0

f = -G*(mMaa/((maaSade+R)**2))+G*(mKuu/((RMaaKuu-maaSade-R)**2))
vavg = 0
v1 = deltaT*f+v0
vavg = (v1+v0)/2
paasiko = True

while (R<=RMaaKuu-kuuSade-maaSade) :
    
    R = vavg*deltaT+R
    f = -G*(mMaa/((maaSade+R)**2))+G*(mKuu/((RMaaKuu-maaSade-R)**2))
    v1 = deltaT*f + v1
    vavg = (v1+vavg)/2
    aika = aika+deltaT
    if(v1<0):
        print('ei päässyt kuuhun')
        paasiko  = False
        break

if (paasiko==True) :
    print('Matkaan meni aikaa ',aika,'sekuntia')

tiedostonNimi = 'kuumatka-aikoja.txt'
with open(tiedostonNimi, 'a') as siirtaja:
    siirtaja.write('matka-aika ja aika-askel: ')
    siirtaja.write(str(aika))
    siirtaja.write(' , ')
    siirtaja.write(str(deltaT))
    siirtaja.write('\n')