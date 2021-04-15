from RpiMotorLib import RpiMotorLib
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO pinleri
GPIO_pins = (14, 15, 18) # MS1-MS3
direction = 20 # Yon Pin, 
step = 21 # Step Pin
degree = 25 # 1.8 x 25 = 45 derece
TRIG = 19
ECHO = 26
MOTOR1A = 2
MOTOR1B = 3
MOTOR2A = 17
MOTOR2B = 27

stepMotor = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(MOTOR1A, GPIO.OUT)
GPIO.setup(MOTOR1B, GPIO.OUT)
GPIO.setup(MOTOR2A, GPIO.OUT)
GPIO.setup(MOTOR2B, GPIO.OUT)

def rangeFinder():
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(TRIG, GPIO.LOW)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print("Mesafe:", distance - 0.5, "cm")
    time.sleep(0.01)
    if distance - 0.5 < 30:
        return True
    else:
        return False
    
def motorGo(x):
    stepMotor.motor_go(x, "Full", 1, 0.01, False, 0)
    
def motorDirection(yon):
    if yon == 1: # ileri
        GPIO.output(MOTOR1A, GPIO.HIGH)
        GPIO.output(MOTOR1B, GPIO.LOW)
        GPIO.output(MOTOR2A, GPIO.LOW)
        GPIO.output(MOTOR2B, GPIO.HIGH)
    elif yon == 2: # sag
        GPIO.output(MOTOR1A, GPIO.LOW)
        GPIO.output(MOTOR2A, GPIO.HIGH)
        GPIO.output(MOTOR1B, GPIO.LOW)
        GPIO.output(MOTOR2B, GPIO.HIGH)
    elif yon == 3: # sol
        GPIO.output(MOTOR1A, GPIO.HIGH)
        GPIO.output(MOTOR2A, GPIO.LOW)
        GPIO.output(MOTOR1B, GPIO.HIGH)
        GPIO.output(MOTOR2B, GPIO.LOW)
    else:
        GPIO.output(MOTOR1A, GPIO.LOW)
        GPIO.output(MOTOR2A, GPIO.LOW)
        GPIO.output(MOTOR1B, GPIO.LOW)
        GPIO.output(MOTOR2B, GPIO.LOW)

i = 0
while True:
    i = i + 1
#     ilk sola don
    if i == 1:
        j = 0
        while j < degree:
            motorGo(False)
            temp = rangeFinder()
            j += 1;
            if temp:
                motorDirection(2) # saga don
            else:
                motorDirection(1)
#     saga don
    elif i % 2 == 1:
        j = 0
        while j < 2 * degree:
            motorGo(False)
            temp = rangeFinder()
            j += 1;
            if temp:
                motorDirection(3) # saga don
            else:
                motorDirection(1)
#     tekrar sola don
    else:
        j = 0
        while j < 2 * degree:
            motorGo(True)
            temp = rangeFinder()
            j += 1;
            if temp:
                motorDirection(2) # saga don
            else:
                motorDirection(1)
    #time.sleep(0.01)

