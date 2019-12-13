import numpy as np
import matplotlib.pyplot as pl

alkunopeudet = [11074.286270141602, 11075.444412231445, 11076.8949508667, 11088.605690002441, 11103.500747680664, 11134.090805053711, 11409.63306427002]
aikaAskeleet = [0.1, 0.5, 1, 5, 10, 20, 100]
pl.plot(aikaAskeleet, alkunopeudet, 'x', color='red')
pl.xlabel('aika-askel dt (s)')
pl.ylabel('alkunopeus v0 (m/s)')
pl.title('Pienin nopeus aika-askeleen funktiona')

x = np.linspace(0, 100, 100)

sovitus = np.polyfit(aikaAskeleet, alkunopeudet, 2)

pl.figure(1)
pl.plot(x, sovitus[0]*x**2+sovitus[1]*x+sovitus[2], color='blue')
pl.text(1,11350, 'v0= %f*dt^2 + %f*dt + %f' %(sovitus[0], sovitus[1], sovitus[2]), color='blue')
pl.xlim(0,101)

pl.figure(2)
pl.plot(x, sovitus[0]*x**2+sovitus[1]*x, color='red')
pl.text(1,300, r'$virhe:  \Delta v0= %f*dt^2 + %f*dt$' %(sovitus[0], sovitus[1]), color='red')
pl.xlabel('aika-askel dt (s)')
pl.ylabel('matka-aika T (s)')
pl.title('Pienimmän nopeuden virhe aika-askeleen funktiona')
pl.xlim(0,101)


pl.show()
