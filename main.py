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

class Robo():
    def __init__(self):
        self.motor_central = Motor(Port.A)
        self.motor_esquerdo = Motor(Port.C)
        self.motor_direito = Motor(Port.B)
        self.sensor_cor_esquerdo = ColorSensor(Port.S1)
        self.sensor_cor_direito = ColorSensor(Port.S2)
        
        self.potencia = POTENCIA = 100
        self.potencia_min = POTENCIA_MIN = 50
        self.potencia_max = POTENCIA_MAX = 200
            
    def andar_cm(self, distancia_cm, velocidade=200):
        """
        Versão com compensação de peso (ajuste empírico).
        peso_kg: Peso aproximado do robô em quilogramas.
        """
        diametro_roda = 4.8  # cm
        circunferencia = pi * diametro_roda
        rotacoes = distancia_cm / circunferencia
        
        angulo = rotacoes * 360
        
        self.motor_direito.reset_angle(0)
        self.motor_esquerdo.reset_angle(0)
    
        self.motor_esquerdo.run_angle(velocidade, angulo, wait=False)
        self.motor_direito.run_angle(velocidade, angulo, wait=True)
        
        self.motor_esquerdo.hold()
        self.motor_direito.hold()
    
    def girar_graus(self, angulo, velocidade=200):
        """
        Gira o robô em torno do seu eixo vertical.
        angulo: Ângulo em graus para girar (positivo para direita, negativo para esquerda).
        velocidade: Velocidade de rotação dos motores.
        """
        self.motor_direito.reset_angle(0)
        self.motor_esquerdo.reset_angle(0)
        self.motor_central.reset_angle(0)
    
        # Usa o valor absoluto do ângulo para cálculo
        angulo_abs = abs(angulo) * pi
        
        if angulo > 0:  # Direita (horário)
            print("Girando para a direita")
            self.motor_esquerdo.run_angle(velocidade, angulo_abs, wait=False)
            self.motor_direito.run_angle(velocidade, -angulo_abs, wait=False)
            self.motor_central.run_angle(velocidade, -angulo_abs, wait=True)
        else:  # Esquerda (anti-horário)
            print("Girando para a esquerda")
            self.motor_esquerdo.run_angle(velocidade, -angulo_abs, wait=False)
            self.motor_direito.run_angle(velocidade, angulo_abs, wait=False)
            self.motor_central.run_angle(velocidade, angulo_abs, wait=True)
        
        self.motor_esquerdo.hold()
        self.motor_direito.hold()
        self.motor_central.hold()


robo = Robo()

robo.andar_cm(15, velocidade=700)
robo.girar_graus(90, velocidade=700)
robo.girar_graus(-180, velocidade=700)
    