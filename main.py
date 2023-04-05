import machine
import utime

# Define los pines para el sensor ultrasónico y los LEDs
trig_pin = machine.Pin(17, machine.Pin.OUT)
echo_pin = machine.Pin(16, machine.Pin.IN)
rojo_pin = machine.Pin(18, machine.Pin.OUT)
amarillo_pin = machine.Pin(19, machine.Pin.OUT)
verde_pin = machine.Pin(20, machine.Pin.OUT)

# Función para medir la distancia utilizando el sensor ultrasónico
def medir_distancia():
    # Enviar un pulso de 10 microsegundos al pin trig para activar la medición
    # Utilizamos 10 porque es la duración mínima requerida para que el sensor detecte el pulso y comience a medir la distancia.
    trig_pin.off()
    utime.sleep_us(2)
    trig_pin.on()
    utime.sleep_us(10)
    trig_pin.off()

    # Esperar a que el pin echo se active
    while echo_pin.value() == 0:
        pass
    start_time = utime.ticks_us()

    # Esperar a que el pin echo se desactive
    while echo_pin.value() == 1:
        pass
    end_time = utime.ticks_us()

    # Calcular la duración del pulso de retorno y convertirlo en distancia
    # Una vez recibido el tiempo, lo traducimos a una distancia en centímetros dividiendo el valor
    # por una constante (para el sensor SR04 es 29 para la señal de ida, y la misma cantidad para la señal
    # de regreso, que en total dará 58).
    duracion = utime.ticks_diff(end_time, start_time)
    distancia = duracion / 58
    
    #La expresión {:.1f} indica que se mostrará un solo decimal en la distancia. 
    print("Distancia: {:.1f} cm".format(distancia))

    return distancia

# Función para encender el LED rojo
def encender_rojo():
    rojo_pin.on()
    amarillo_pin.off()
    verde_pin.off()

# Función para encender el LED amarillo
def encender_amarillo():
    rojo_pin.off()
    amarillo_pin.on()
    verde_pin.off()

# Función para encender el LED verde
def encender_verde():
    rojo_pin.off()
    amarillo_pin.off()
    verde_pin.on()

# Ciclo principal del programa
while True:
    # Medir la distancia del objeto
    distancia = medir_distancia()

    # Encender el LED rojo si el objeto está muy cerca en cm
    if distancia < 10:
        encender_rojo()
    # Encender el LED amarillo si el objeto está a una distancia intermedia en cm
    elif distancia < 20:
        encender_amarillo()
    # Encender el LED verde si el objeto está lejos
    else:
        encender_verde()

    # Esperar un momento antes de medir la distancia nuevamente
    utime.sleep(0.2)

