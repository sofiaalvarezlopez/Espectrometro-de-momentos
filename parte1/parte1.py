import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import *
from matplotlib import cm
import datetime
import os
# e es la carga elemental, m_p es la masa del proton
#from scipy.constants import e, m_p
print('-----Simulación de trayectorias de partículas bajo un campo magnético uniforme-----')
num_particulas = int(input('Escriba el numero de partículas que desea simular:\n'))
max_vel = float(input('Escriba la velocidad máxima que una partícula puede tener:\n'))
magnitud_B = float(input('Escriba la magnitud del campo magnético:\n'))

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

path = './datos/'
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

B = np.array([[0.0, 0.0, magnitud_B]])
posicion_inicial = np.array([[0.0, 0.0, 0.0]])
a_inicial = np.array([[0.0, 0.0, 0.0]])
t_inicial = 0
delta_t = 0.0001
e = 5
m_p = 2
plt.figure(figsize=(15,7.5))
plt.xlabel('Posición en x [m]')
plt.ylabel('Posición en y [m]')
plt.title('Trayectorias de {} partículas bajo un campo mágnetico uniforme B = {:.1f} T'.format(num_particulas, magnitud_B))
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
formato = '{},{},{}\n'

for p in range(num_particulas):
    archivo_trayectoria = open(carpeta_trayectorias + '/' + str(p+1) + '.dat', 'w')
    v_inicial = np.array([[0.0, max_vel*np.random.rand(), 0.0]])
    p_inicial = momento_inicial(v_inicial, m_p)
    trayectoria, velocidad, aceleracion = evolucionar_verlet(e, m_p, B, delta_t, posicion_inicial, v_inicial, a_inicial, archivo_trayectoria)
    archivo_trayectoria.close()
    p_final = momento_final(trayectoria, e, B)
    archivo_momentos.write(formato.format(p+1, p_inicial, p_final))
    plt.plot(trayectoria[:,0], trayectoria[:,1], label='Partícula {} con momento p={:.3f}'.format(p+1, p_inicial))
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)

archivo_momentos.close()
plt.savefig(carpeta_trayectorias + '/Trayectorias.png')
plt.show()
