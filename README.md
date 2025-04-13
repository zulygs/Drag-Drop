# Drag & Drop

Este proyecto permite la interacción con objetos, de forma que estos se puedan mover al detectar los diferenctes movimientos
establecidos de las manos como juntar los dedos para agarrar los objetos o separar los dedos para poder soltar los objetos. Todo esto se detecta por medio de la camara de la computadora y utilizando bibliotecas como OpenCV, Cvzone con Mediapipe etc.

## ¿Cómo funciona?

- Se utiliza la cámara web para capturar video en tiempo real.
- Se detecta la posición de la mano y sus puntos clave.
- Si los dedos índice y medio están juntos se considera como agarrar.
- Se puede mover el objeto al identificar el movimeinto.
- Se puede observar el identificador de la mano.

## 💻 Requisitos

- Python 3.7+
- OpenCV
- cvzone(usa mediapipe de forma encapsulada)
