#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
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
        
        # ===== Potencia Motores =====
        self.potencia = 100
        self.potencia_min = 50
        self.potencia_max = 200
        # ===== Sensor de cor  e velocidades dos Motores =====
        self.threshold = 10
        self.adjust_speed = 100
        self.adjust_angle = -15
        self.angle = 15  
        # ===== Diametro e Rotação dos motores ===== 
        
    def andar_cm(self, distancia_cm, velocidade=200):

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
    
    def alinhar(self):
        while True:
            refL = self.sensor_cor_esquerdo.reflection()
            refR = self.sensor_cor_direito.reflection()

            if refL is None or refR is None:
                self.ev3.speaker.beep()
                wait(200)
                continue

        # --- Lado Direito ---
            if refR < self.threshold:
                # Se vê preto: faz um único ajuste e para o motor
                self.motor_direitor.run_angle(self.adjust_speed, self.adjust_angle, then=Stop.HOLD, wait=True)
                self.motor_esquerdo.stop()  # garante parada completa
            else:
                # Se vê claro: faz um único ajuste e para o motor
                self.motor_direito.run_angle(self.adjust_speed, self.angle, then=Stop.HOLD, wait=True)
                self.motor_direito.stop()

            # --- Lado Esquerdo ---
            if refL < self.threshold:
                self.motor_esquerdo.run_angle(self.adjust_speed, self.adjust_angle, then=Stop.HOLD, wait=True)
                self.motor_esquerdo.stop()
            else:
                self.motor_esquerdo.run_angle(self.adjust_speed, self.angle, then=Stop.HOLD, wait=True)
                self.motor_esquerdo.stop()

            # --- Geral ---
            if refL < self.threshold and refR < self.threshold:
                self.motor_direito.hold()
                self.motor_esquerdo.hold(wait=True)
                
                self.motor_direito
                

            # Pequena pausa antes da próxima leitura
            wait(10)


robo = Robo()

robo.andar_cm(15, velocidade=700)
robo.girar_graus(90, velocidade=700)
robo.girar_graus(-180, velocidade=700)
robo.alinhar_linha()