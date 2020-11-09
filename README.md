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
