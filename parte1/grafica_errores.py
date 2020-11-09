import matplotlib.pyplot as plt
import numpy as np

data_path = './datos/errores.dat'
data = np.loadtxt(data_path, skiprows=1, delimiter=',')

plt.figure(figsize=(10,10))
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.plot(data[:,0], data[:,2], 'o')
plt.title('')
plt.xlabel(r'$\Delta \ t$')
plt.ylabel(r'Error en el momento')
plt.title(r'Error en el momento en función del intervalo temporal, $\Delta t$, utilizado')
plt.yscale('log')
plt.xscale('log')
plt.savefig('./datos/error_momento_tiempo.png')
