import numpy as np
import matplotlib.pyplot as plt
import datetime
import os
# e es la carga elemental, m_p es la masa del proton
#from scipy.constants import e, m_p
print('-----Simulación de trayectorias de partículas, con ángulo de incidencia theta0, bajo un campo magnético uniforme-----')
opcion = int(input('Opciones:\n 1) Mantener theta0 constante para todas las partículas y variar la velocidad.\n 2) Mantener velocidad constante para todas las partículas y variar theta0.\n'))
num_particulas = int(input('Escriba el numero de partículas que desea simular:\n'))
max_vel = 0
theta0 = 0
magnitud_B = float(input('Escriba la magnitud del campo magnético:\n'))
if opcion == 1:
    max_vel = float(input('Escriba la velocidad máxima que una partícula puede tener:\n'))
    theta0 = float(input('Escriba el ángulo de incidencia de la partícula (theta0) en grados:\nNOTA:theta0 debe ser mayor a 0\n'))
elif opcion == 2:
    max_vel = float(input('Escriba la velocidad de las partículas:\n'))
    theta0 = float(input('Escriba el ángulo de incidencia MÁXIMO de una partícula (theta0) en grados:\nNOTA:theta0 debe ser mayor a 0\n'))
else:
    print('Opción incorrecta. Finalizando ejecucion del programa.')
    exit(-1)

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
carpeta_graficas_trayectorias = os.path.join(carpeta, 'graficas_trayectorias')
os.mkdir(carpeta_trayectorias)
os.mkdir(carpeta_graficas_trayectorias)
archivo_xfinal = open(carpeta + '/x_finales.dat', 'w')
if opcion == 1:
    archivo_xfinal.write('id_particula,vel_particula,x_final_+theta0,x_final_-theta0\n')
else:
    archivo_xfinal.write('id_particula,theta_0,x_final_+theta0,x_final_-theta0\n')

B = np.array([[0.0, 0.0, magnitud_B]])
posicion_inicial = np.array([[0.0, 0.0, 0.0]])
a_inicial = np.array([[0.0, 0.0, 0.0]])
t_inicial = 0
delta_t = 0.0001
e = 5
m_p = 2
formato = '{},{},{},{}\n'
for p in range(num_particulas):
    v_magnitud = max_vel
    theta_0 = theta0
    if opcion == 1:
        v_magnitud *= np.random.rand() + 0.001
    else:
        theta_0 *= np.random.rand() + 1
    archivo_trayectoria_theta0pos = open(carpeta_trayectorias + '/' + str(p+1) + '_theta0+.dat', 'w')
    archivo_trayectoria_theta0neg = open(carpeta_trayectorias + '/' + str(p+1) + '_theta0-.dat', 'w')
    v_inicial = np.array([[v_magnitud*np.sin(np.deg2rad(theta_0)), v_magnitud*np.cos(np.deg2rad(theta_0)), 0.0]])
    v_inicial_m = np.array([[-v_magnitud*np.sin(np.deg2rad(theta_0)), v_magnitud*np.cos(np.deg2rad(theta_0)), 0.0]])
    trayectoria, velocidad, aceleracion = evolucionar_verlet(e, m_p, B, delta_t, posicion_inicial, v_inicial, a_inicial, archivo_trayectoria_theta0pos)
    trayectoria_m, velocidad_m, aceleracion_m = evolucionar_verlet(e, m_p, B, delta_t, posicion_inicial, v_inicial_m, a_inicial, archivo_trayectoria_theta0neg)
    archivo_trayectoria_theta0pos.close()
    archivo_trayectoria_theta0neg.close()
    titulo = ''
    plt.figure(figsize=(15,7.5))
    if opcion == 1:
        archivo_xfinal.write(formato.format(p+1, v_magnitud, trayectoria[-1,0], trayectoria_m[-1,0]))
        titulo = 'Trayectoria de dos partículas con velocidad inicial v={:.3f} m/s bajo B={:.1f} T'
        plt.title(titulo.format(v_magnitud, magnitud_B))
    else:
        archivo_xfinal.write(formato.format(p+1, theta_0, trayectoria[-1,0], trayectoria_m[-1,0]))
        titulo = r'Trayectoria de dos partículas con ángulo de incidencia $\theta_0$=$\pm${:.3f} bajo B={:.1f} T'
        plt.title(titulo.format(theta_0, magnitud_B))
    plt.xlabel('Posición en x [m]')
    plt.ylabel('Posición en y [m]', loc='top')
    ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    plt.plot(trayectoria[:,0], trayectoria[:,1], label=r'Partícula con ángulo de incidencia $\theta_0$={:.1f}'.format(theta_0))
    plt.plot(trayectoria_m[:,0], trayectoria_m[:,1], label=r'Partícula con ángulo de incidencia $\theta_0$={:.1f}'.format(-theta_0))
    plt.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.savefig(carpeta_graficas_trayectorias + '/Trayectoria_particula' + str(p+1) +'.png', bbox_inches='tight')
    plt.close()
 

archivo_xfinal.close()


