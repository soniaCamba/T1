# SONIA CAMBA RODRÍGUEZ
# 1. leemos el fichero y lo sacamos junto a su fm

x, fm = sf.read('nom_fitxer.wav')
# fm = frecuencia de mostratge
num_muestras = len(x)/ fm # Nombre de mostres de senyal

# 2. representamos graficamente
Ls=int(0.025) # aquí es donde decidimos la longitud del eje X
plt.figure(0)
plt.plot(t[0:Ls], x[0:Ls])
plt.xlabel('t en segons')
plt.title('evolución temporal') # título
plt.show() 

# 4. calculamos los parametros de la transformada
from numpy.fft import fft
N=5000
X=fft(x[0 : Ls], N)
XdB = 20*log(abs(X)/max(abs(X))) # pasamos la transformada a dB

# 5. representamos modulo y fase graficamente
k=np.arange(fm,fm/2) # aqui definimos el margen de la transformada
plt.figure(1)
plt.subplot(211)
plt.plot(k,abs(XdB))
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')
plt.ylabel('|X[k]|')
plt.subplot(212)
plt.plot(k,np.unwrap(np.angle(X)))
plt.xlabel('Index k')
plt.ylabel('$\phi_x[k]$')
plt.show()