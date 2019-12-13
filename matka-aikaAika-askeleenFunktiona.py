import numpy as np
import matplotlib.pyplot as pl

matkaAjat = [68705.09999951128, 68743.5, 68792, 69185, 69690, 70740, 82400]
aikaAskeleet = [0.1, 0.5, 1, 5, 10, 20, 100]
pl.plot(aikaAskeleet, matkaAjat, 'x', color='red')
pl.xlabel('aika-askel dt (s)')
pl.ylabel('matka-aika T (s)')
pl.title('Matka-aika aika-askeleen funktiona')

x = np.linspace(0, 150, 100)
sovitus = np.polyfit(aikaAskeleet, matkaAjat, 2)

pl.figure(1)
pl.plot(x, sovitus[0]*x**2+sovitus[1]*x+sovitus[2], color='blue')
pl.text(1,90000, 'T= %f*dt^2 + %f*dt + %f' %(sovitus[0], sovitus[1], sovitus[2]), color='blue')
pl.xlim(0,151)

pl.figure(2)
pl.plot(x, sovitus[0]*x**2+sovitus[1]*x, color='red')
pl.text(1,20000, r'$virhe:  \Delta T= %f*dt^2 + %f*dt$' %(sovitus[0], sovitus[1]), color='red')
pl.xlabel('aika-askel dt (s)')
pl.ylabel('matka-aika T (s)')
pl.title('Matka-ajan virhe aika-askeleen funktiona')
pl.xlim(0,151)

pl.show()
