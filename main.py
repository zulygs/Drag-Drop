import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import os


camara = cv2.VideoCapture(0)
camara.set(3, 1280)
camara.set(4, 720)

rastreador = HandDetector(detectionCon=0.8, maxHands=2)


class clsMoverImagen:
    def __init__(self, ruta, posicion, tipo):
        self.posicion = posicion
        self.tipo = tipo
        self.ruta = ruta

        if tipo == 'png':
            self.imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
        else:
            self.imagen = cv2.imread(ruta)

        self.dimensiones = self.imagen.shape[:2]  # Alto, ancho

    def mover(self, punto):
        x, y = self.posicion
        alto, ancho = self.dimensiones

        if x < punto[0] < x + ancho and y < punto[1] < y + alto:
            self.posicion = punto[0] - ancho // 2, punto[1] - alto // 2


carpeta_imagenes = "img"
nombres_archivos = os.listdir(carpeta_imagenes)

imagenes = []
for indice, nombre_archivo in enumerate(nombres_archivos):
    extension = 'png' if 'png' in nombre_archivo else 'jpg'
    ruta_completa = f'{carpeta_imagenes}/{nombre_archivo}'
    posicion_inicial = [50 + indice * 300, 50]
    imagenes.append(clsMoverImagen(ruta_completa, posicion_inicial, extension))


while True:
    exito, fotograma = camara.read()
    fotograma = cv2.flip(fotograma, 1)

    
    manos_detectadas, fotograma = rastreador.findHands(fotograma, flipType=False, draw=False)

    if manos_detectadas:
        for mano in manos_detectadas:
            puntos = mano['lmList']
            tipo_mano = mano['type'] 


            nombre_mano = "Izquierda" if tipo_mano == 'Left' else "Derecha"
            cx, cy = mano['center']

         
            cv2.putText(fotograma, nombre_mano, (cx - 50, cy - 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

          
            distancia, _, fotograma = rastreador.findDistance(puntos[8][:2], puntos[12][:2], fotograma)
            if distancia < 60:
                posicion_cursor = puntos[8]
                for objeto in imagenes:
                    objeto.mover(posicion_cursor)

    
    try:
        for objeto in imagenes:
            alto, ancho = objeto.dimensiones
            x, y = objeto.posicion

            if objeto.tipo == "png":
                fotograma = cvzone.overlayPNG(fotograma, objeto.imagen, [x, y])
            else:
                fotograma[y:y + alto, x:x + ancho] = objeto.imagen
    except Exception as e:
        pass  

    # Mostrar el resultado
    cv2.imshow("Arrastrar y Soltar", fotograma)
    cv2.waitKey(1)
