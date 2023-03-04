# SONIA CAMBA RODRÍGUEZ
#  1. leemos el fichero y lo sacamos junto a su fm

x, fm = sf.read('nom_fitxer.wav')

# 2. representamos graficamente
Tx=1/fm
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

# 5. representamos modulo y fase graficamente
k=np.arange(N)
plt.figure(1)
plt.subplot(211)
plt.plot(k,abs(X))
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')
plt.ylabel('|X[k]|')
plt.subplot(212)
plt.plot(k,np.unwrap(np.angle(X)))
plt.xlabel('Index k')
plt.ylabel('$\phi_x[k]$')
plt.show()