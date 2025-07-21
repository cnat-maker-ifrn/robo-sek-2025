#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import pi
from random import randint

EV3 = EV3Brick()

MOTOR_CENTRAL = Motor(Port.A)
MOTOR_ESQUERDO = Motor(Port.C)
MOTOR_DIREITO = Motor(Port.B)

# SENSOR_COR_ESQUERDO = ColorSensor(Port.S1)
# SENSOR_COR_DIREITO = ColorSensor(Port.S2)

POTENCIA = 100
POTENCIA_MIN = 50   
POTENCIA_MAX = 200

def andar_cm(distancia_cm, velocidade=200):
    """
    Versão com compensação de peso (ajuste empírico).
    peso_kg: Peso aproximado do robô em quilogramas.
    """
    diametro_roda = 4.8  # cm
    circunferencia = pi * diametro_roda
    rotacoes = distancia_cm / circunferencia
    
    angulo = rotacoes * 360
    
    MOTOR_DIREITO.reset_angle(0)
    MOTOR_ESQUERDO.reset_angle(0)

    MOTOR_ESQUERDO.run_angle(velocidade, angulo, wait=False)
    MOTOR_DIREITO.run_angle(velocidade, angulo, wait=True)
    
    MOTOR_ESQUERDO.hold()
    MOTOR_DIREITO.hold()

def girar_graus(angulo, velocidade=200):
    """
    Gira o robô em torno do seu eixo vertical.
    angulo: Ângulo em graus para girar (positivo para direita, negativo para esquerda).
    velocidade: Velocidade de rotação dos motores.
    """
    MOTOR_CENTRAL.reset_angle(0)
    MOTOR_DIREITO.reset_angle(0)
    MOTOR_ESQUERDO.reset_angle(0)

    # Usa o valor absoluto do ângulo para cálculo
    angulo_abs = abs(angulo) * pi
    
    if angulo > 0:  # Direita (horário)
        print("Girando para a direita")
        MOTOR_ESQUERDO.run_angle(velocidade, angulo_abs, wait=False)
        MOTOR_DIREITO.run_angle(velocidade, -angulo_abs, wait=False)
        MOTOR_CENTRAL.run_angle(velocidade, -angulo_abs, wait=True)
    else:  # Esquerda (anti-horário)
        print("Girando para a esquerda")
        MOTOR_ESQUERDO.run_angle(velocidade, -angulo_abs, wait=False)
        MOTOR_DIREITO.run_angle(velocidade, angulo_abs, wait=False)
        MOTOR_CENTRAL.run_angle(velocidade, angulo_abs, wait=True)
    
    MOTOR_ESQUERDO.hold()
    MOTOR_DIREITO.hold()
    MOTOR_CENTRAL.hold()

andar_cm(15, velocidade=700)
girar_graus(90, velocidade=700)
girar_graus(-180, velocidade=700)
