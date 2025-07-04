#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import pi


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Motores
motorC = Motor(Port.A)
motorL = Motor(Port.B)
motorR = Motor(Port.C)


# Sensores
sensorCorR = ColorSensor(Port.S1)
sensorCorL = ColorSensor(Port.S2)
# SensorUltrassom = UltrasonicSensor(Port.S3)

# controle dos motor
ganho = 2.0
potencia = 100
potencia_min = 50   
potencia_max = 200

# Função seguir linha
def seguir_linha():
    while True:
        refL = sensorCorL.reflection()
        refR = sensorCorR.reflection()

        if refL is None or refR is None:
            ev3.speaker.beep()
            continue

        print("Reflexão Esquerdo: " + str(refL))
        print("Reflexão Direito:" + str(refR))

        if refL > 20 and refR > 20:
            motorL.run(potencia_max)
            motorR.run(potencia_max)
            motorC.stop()
        
        if refL < 8:
            motorL.run(-potencia_max)
            motorR.run(potencia_max)
            motorC.run(potencia_max)
        
        if refR < 8:
            motorL.run(potencia_max)
            motorR.run(-potencia_max)
            motorC.run(-potencia_max)

seguir_linha()
