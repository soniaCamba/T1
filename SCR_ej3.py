# SONIA CAMBA RODRÍGUEZ
# 1. declaramos todas las variables. Son las mismas que antes pero cambiando el archivo de audio

T= 2.5
fm=8000
fx=440
A=4
pi=np.pi
L = int(fm * T)
Tm=1/fm
t=Tm*np.arange(L)
x = A * np.cos(2 * pi * fx * t)
sf.write('nom_fitxer.wav', x, fm)

# 2. representamos graficamente
Tx=1/fx
Ls=int(fm*5*Tx)
plt.figure(0)
plt.plot(t[0:Ls], x[0:Ls])
plt.xlabel('t en segons')
plt.title('5 periodes de la sinusoide')
plt.show() 

# 4. calculamos los parametros de la transformada
from numpy.fft import fft
N=5000
X=fft(x[0 : Ls], N)
XdB = 20*log(abs(X)/max(abs(X)))

# 5. representamos modulo y fase graficamente
k=np.arange(fm/2) # aquí es donde cambiamos el eje de abcisas
plt.figure(1)
plt.subplot(211)
plt.plot(k,abs(XdB))
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')
plt.ylabel('|X[k]|')
plt.subplot(212)
plt.plot(k,np.unwrap(np.angle(X)))
plt.xlabel('dB') # aquí es donde cambiamos la etiqueta del eje
plt.ylabel('$\phi_x[k]$')
plt.show()

# la amplitud la podemos saber calculando el maximo de la sinusoide que nos dará la amplitud de pico a pico y luego lo dividiendo entre 2
amplitud = (max(XdB))/2