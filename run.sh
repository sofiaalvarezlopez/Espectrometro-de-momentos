#!/bin/bash
echo ----------------------------------------------------------------
echo Simulacion de trayectorias de particulas bajo un campo magnetico
echo ---------Juan Daniel Castrellon y Maria Sofia Alvarez ----------
echo ----------------------------------------------------------------
echo Escriba el numero de la opcion que desea correr [e.g. 1]
echo 1. Instalar las dependencias del programa
echo 2. Correr la simulacion para particulas que inciden perpendicular al campo.
echo 3. Correr la simulacion para particulas que inciden a un angulo theta0.

read line;
    if [ "$line" -eq 1 ];
        then pip install -r requirements.txt;
    elif [ "$line" -eq 2 ]; 
        then cd parte1 && python3 ./parte1.py;
    elif [ "$line" -eq 3 ]; 
        then cd parte2 && python3 ./parte2.py;
    else
        echo Opcion no disponible;
    fi
