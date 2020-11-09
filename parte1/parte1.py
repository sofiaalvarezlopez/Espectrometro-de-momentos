import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import datetime
import os

# e es la carga elemental, m_p es la masa del proton
#from scipy.constants import e, m_p
print('-----Simulación de trayectorias de partículas bajo un campo magnético uniforme-----')
num_particulas = int(input('Escriba el numero de partículas que desea simular:\n'))
max_vel = float(input('Escriba la velocidad máxima que una partícula puede tener:\n'))
magnitud_B = float(input('Escriba la magnitud del campo magnético:\n'))
delta_t = float(input('Escriba el valor del paso temporal:\n'))

def momento_inicial(v_inicial, m_p):
    return np.linalg.norm(v_inicial)*m_p

def fuerza_y_aceleracion(q, v, B, m):
    # Fuerza magnetica
    F = q*np.cross(v, B)
    a = F/m
    return F, a

def mover_particula(dt, posicion_anterior, velocidad_anterior, aceleracion_anterior):
    posicion_actual = posicion_anterior + velocidad_anterior*dt + 0.5*aceleracion_anterior*(dt**2)
    velocidad_actual = velocidad_anterior + aceleracion_anterior*dt
    return posicion_actual, velocidad_actual

def evolucionar_verlet(e, m_p, B, delta_t, posicion_inicial, v_inicial, aceleracion_inicial, archivo_trayectoria):
    archivo_trayectoria.write('x,y,z\n')
    trayectoria = np.array(posicion_inicial)
    velocidad = np.array(v_inicial)
    aceleracion = np.array(aceleracion_inicial)
    F_1, a_1 = fuerza_y_aceleracion(e, v_inicial, B, m_p)
    pos_1, v_1 = mover_particula(delta_t, posicion_inicial, v_inicial, a_1)
    trayectoria = np.append(trayectoria, pos_1, axis=0)
    velocidad = np.append(velocidad, v_1, axis=0)
    aceleracion = np.append(aceleracion, a_1, axis=0)
    y = pos_1[:,1]
    i = 1
    t = 0.0
    formato = '{},{},{}\n'
    archivo_trayectoria.write(formato.format(trayectoria[0, 0], trayectoria[0,1], trayectoria[0,2]))
    archivo_trayectoria.write(formato.format(trayectoria[1, 0], trayectoria[1,1], trayectoria[1,2]))
    while y >= 0:
        f, a = fuerza_y_aceleracion(e, velocidad[i], B, m_p)
        pos, v = mover_particula(delta_t, trayectoria[i], velocidad[i], a)
        trayectoria = np.append(trayectoria, pos, axis=0)
        velocidad = np.append(velocidad, v, axis=0)
        aceleracion = np.append(aceleracion, a, axis=0)
        i += 1
        archivo_trayectoria.write(formato.format(trayectoria[i, 0], trayectoria[i,1], trayectoria[i,2]))
        t += delta_t
        y = pos[:,1]
    return trayectoria, velocidad, aceleracion

def momento_final(trayectoria, e, B):
    R = trayectoria[-1,0]/2
    return R*e*np.linalg.norm(B)

def error_momento(p_inicial, p_final):
    return np.abs(p_inicial - p_final)

path = './datos/'
try:
    os.mkdir('datos')
except:
    pass
fecha = str(datetime.datetime.now())
carpeta = ''
try:
    carpeta = os.path.join(path, fecha)
    os.mkdir(carpeta)
except:
    print('No se ha podido crear el directorio para almacenar los archivos')
    exit(-1)
carpeta_trayectorias = os.path.join(carpeta, 'trayectorias')
os.mkdir(carpeta_trayectorias)
archivo_momentos = open(carpeta + '/momentos.dat', 'w')
archivo_momentos.write('id_particula,p_inicial,p_final\n')
archivo_xfinal = open(carpeta + '/x_finales.dat', 'w')
archivo_xfinal.write('{},{}\n'.format('id_particula', 'x_final'))
errores = open(path + 'errores.dat', 'a+')
if os.stat(path + 'errores.dat').st_size == 0:
    errores.write('{},{},{}\n'.format('delta_tiempo', 'error_maximo', 'error_medio'))

B = np.array([[0.0, 0.0, magnitud_B]])
posicion_inicial = np.array([[0.0, 0.0, 0.0]])
a_inicial = np.array([[0.0, 0.0, 0.0]])
t_inicial = 0
e = 5
m_p = 2
plt.figure(figsize=(15,7.5))
plt.xlabel('Posición en x [m]')
plt.ylabel('Posición en y [m]')
plt.title('Trayectorias de {} partículas bajo un campo mágnetico uniforme B = {:.1f} T'.format(num_particulas, magnitud_B))
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
formato = '{},{},{}\n'
momentos_iniciales, momentos_finales = [], []

for p in range(num_particulas):
    archivo_trayectoria = open(carpeta_trayectorias + '/' + str(p+1) + '.dat', 'w')
    v_inicial = np.array([[0.0, max_vel*np.random.rand() + 0.001, 0.0]])
    p_inicial = momento_inicial(v_inicial, m_p)
    momentos_iniciales.append(p_inicial)
    trayectoria, velocidad, aceleracion = evolucionar_verlet(e, m_p, B, delta_t, posicion_inicial, v_inicial, a_inicial, archivo_trayectoria)
    archivo_trayectoria.close()
    p_final = momento_final(trayectoria, e, B)
    momentos_finales.append(p_final)
    archivo_momentos.write(formato.format(p+1, p_inicial, p_final))
    archivo_xfinal.write('{},{}\n'.format(p+1, trayectoria[-1,0]))
    plt.plot(trayectoria[:,0], trayectoria[:,1], label='Partícula {} con momento p={:.3f}'.format(p+1, p_inicial))
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)
archivo_momentos.close()
archivo_xfinal.close()
plt.savefig(carpeta + '/trayectorias.png', bbox_inches='tight')

plt.figure(figsize=(10,10))
plt.xlabel('Momento inicial')
plt.ylabel('Momento final')
plt.title('Momento inicial y final de las partículas en el espectrómetro de momentos')
slope, intercept, r_value, p_value, std_err = stats.linregress(momentos_iniciales, momentos_finales)
x = np.linspace(min(momentos_iniciales), max(momentos_iniciales), 1000)
plt.plot(x, intercept + slope*x, 'r', label=r'Ajuste lineal $p_f$ = {:3f}$p_i$ + {:.3f} con $R^2$={:.3f}'.format(slope, intercept, r_value**2))
plt.plot(momentos_iniciales, momentos_finales, '.')
plt.legend(loc='best')
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
plt.savefig(carpeta + '/momentos.png')

errores_momento = error_momento(np.array(momentos_iniciales), np.array(momentos_finales))
plt.figure(figsize=(10,10))
plt.xlabel('Momento inicial')
plt.ylabel('Error en el momento')
plt.title('Relación entre el momento inicial de una partícula y el error respecto a su momento final')
plt.plot(momentos_iniciales, errores_momento, '.')
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
plt.savefig(carpeta + '/error_momento.png')

errores.write('{},{},{}\n'.format(delta_t, np.max(errores_momento), np.mean(errores_momento)))


