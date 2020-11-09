## Aceleradores de Partículas y sus Aplicaciones
### Proyecto 1: Espectrómetro de momentos
> Elaborado por: Juan Daniel Castrellón Botero (201729285) y María Sofía Álvarez López (201729031)

<div align="center"><a name="menu"></a>
  <h4>
    <a href="#intro">
      Introducción al proyecto
    </a>
    <span> | </span>
    <a href=#correr>
      Correr el proyecto
    </a>
    <span> | </span>
    <a href=#parte-1>
      Acerca de la parte 1
    </a>
    <span> | </span>
    <a href=#parte-2>
      Acerca de la parte 2
    </a>
  </h4>
</div>

***
<h2 name="intro">Introducción al proyecto</h2>
<p align="justify"> 
  El objetivo de este proyecto fue el de simular la trayectoria de una partícula cargada en un espectrómetro de momentos. Asimismo, se verificó que el radio de una partícula cargada depende de su momento. Además, se quiso indagar en la propiedad de enfoque que tiene el espectrómetro, según lo propuesto por Feynman en su volumen 2 del Feynman Lectures on Physics, capítulo 29. 
</p>
<p align="justify">
  Con el fin de lograr el objetivo propuesto, se crearon dos programas en el lenguaje de programación Python. El primero simula una partícula que incide perpendicularmente a la base del espectrómetro, es decir, tiene una velocidad en la dirección <i>j</i>. Por su lado, el campo magnético tenía una magnitud B=8T en dirección <i>k</i>. El objetivo de este programa era verificar que el momento de la partícula al entrar al espectrómetro, calculado como |p| = m|v|, es el mismo al salir, calculado según la ecuación |p| = q|B|R, donde <i>B</i> es el campo magnético, <i>R</i> el radio de la trayectoria semicircular que sigue la partícula y q = 5 C la carga de la partícula. El radio de la partícula se calculó con la distancia x_final a la que sale la partícula del espectrómetro, medida desde su punto de entrada, teniendo en cuenta que x_final = 2R. El código implementado para llevar a cabo este objetivo se encuentra en la carpeta <code>parte1</code>, el archivo <code>parte1.py</code>.
</p>
</p>

<h2 name="correr">Correr el proyecto</h2>
<p align="justify"> 
  Con el fin de correr este repositorio, deben seguirse los pasos mostrados a continuación. 
</p>
<ol>
<li> Antes de correr el proyecto, asegúrese de tener instalado <code>python3</code> en su máquina local y <code>pip</code> o <code>pip3</code> para instalar las dependencias y librerías necesarias para la ejecución del programa. Si no cuenta con alguno de estos, puede instalarlos remitiéndose a <a href=https://www.python.org/downloads/>la documentación oficial de python</a> para instalar <code>python3</code>, con lo que se instalará una distribuión de <code>pip</code></li>
<li> Corra el archivo <code>./run.sh</code>. En caso de que le salga el error <i>Permission denied</i> ejecute alguno de los comandos mostrados a continuación.
  <ul>
    <li><code>sudo ./run.sh</code></li>
    <li><code>chmod 777 ./run.sh</code></li>
  </ul>
  Lo cual dará los permisos de ejecución necesarios para correr el programa.
</li>
<li>Una vez corrido el programa, se le mostrarán las opciones disponibles:
    <ol>
    <li>Instalar las dependencias y librerías del programa.</li>
    <li>Correr la parte 1 del proyecto.</li>
    <li>Correr la parte 2 del proyecto.</li>
  </ol>
  <i>NOTA: Si es la primera vez que corre el programa, seleccione la opción 1.</i><br/>
  Otra forma de instalar las dependencias es corriendo el comando <code>pip install -r requirements.txt</code>
</li>
<li><b>Correr la parte 1 del proyecto: </b>
  Si desea correr la primera parte del proyecto, seleccione la segunda opción del archivo <code>./run.sh</code>. Aquí, se le solicitarán algunos datos con el fin de correr la simulación. 
  <ol>
    <li> Primero, deberá ingresar el número de partículas que desea simular. </li>
    <li> Después, deberá ingresar la velocidad máxima, en m/s, que una partícula debe tener. Esta velocidad se multiplica por un número aleatorio entre 0 y 1 con el fin de generar partículas con diferentes velocidades (y momentos) iniciales. </li>
    <li> Más adelante, deberá ingresar la magnitud del campo magnético B, en Tesla, que existirá en el espectrómetro de momentos. </li>
    <li> Finalmente, deberá ingresar el paso temporal con el que desea realizar la simulación. Se recomiendan pasos temporales menores a <i>0.0001 s</i> con el fin de tener resultados precisos.  
  </ol>
  Si es la primera vez que se corre la simulación, se genera la carpeta <code>datos</code>, donde, por cada vez que se ejecuta el programa, se almacenan los datos de la simulación en una carpeta con la fecha en que se inició la simulación. Por ejemplo: <code>2020-11-05 16:56:29.880790</code> es una simulación que se inició el 5 de noviembre a las 16:56 horas. Dentro de cada carpeta, se pueden encontrar los siguientes archivos y carpetas:
  <ul>
    <li>Carpeta <code>trayectorias</code>: Almacena, en un archivo por partícula, las posiciones x,y,z, en cada momento del tiempo, de cada una de las partículas simuladas. <br/> Se generan tantos archivos como partículas se hayan simulado. <br/> El formato del archivo es: <code>x,y,z</code> y se almacena como <code>i.dat</code> donde <code>i</code> es el número de la partícula simulada.</li>
    <li>Archivo <code>x_finales.dat</code>: Almacena las posiciones finales, en x, de cada una de las partículas. <br/> El formato del archivo es: <code>id_particula,x_final</code></li>
    <li>Archivo <code>momentos.dat</code>: Almacena el momento inicial y final de cada partícula, calculados como p = qv y p = qBR, respectivamente. <br/> El formato del archivo es: <code>id_particula,x_inicial_x_final</code></li>
    <li>Imagen <code>trayectorias.png</code>: Muestra gráficamente las trayectorias de cada una de las partículas simuladas en el espectrómetro de momentos. Una imagen ejemplo generada se muestra a continuación,
    </li>
    <li>Imagen <code>momentos.png</code>: Muestra el momento final de una partícula en función de su momento inicial y realiza un ajuste lineal entre ambas cantidades. Una imagen ejemplo generada se muestra a continuación,
    </li>
    <li>Imagen <code>error_momento.png</code>: Muestra el error en el momento (calculado como |p_final - p_inicial|) en función del momento inicial de las partículas. Entre más grande sea el paso temporal y/o la velocidad de las partículas, se espera un mayor error. Una imagen ejemplo generada se muestra a continuación,
</li>
</ol>
