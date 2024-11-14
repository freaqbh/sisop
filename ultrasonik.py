import RPi.GPIO as GPIO
import time

# Pin setup
TRIG = 23  # Pin untuk trigger
ECHO = 24  # Pin untuk echo
LED = 18   # Pin untuk LED

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

# Function to measure distance
def get_distance():
    # Mengirimkan sinyal trigger selama 10µs
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Catat waktu saat sinyal dikirimkan dan diterima kembali
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Menghitung jarak berdasarkan waktu tempuh sinyal
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Konversi ke cm
    distance = round(distance, 2)
    return distance

try:
    while True:
        distance = get_distance()
        print(f"Jarak: {distance} cm")
        
        # Kondisi untuk menyalakan atau mematikan LED
        if distance < 20:
            GPIO.output(LED, True)
        else:
            GPIO.output(LED, False)
            
        time.sleep(1)  # Tunggu 1 detik sebelum pengukuran berikutnya
except KeyboardInterrupt:
    print("Program dihentikan")
    GPIO.cleanup()  # Mengatur ulang semua pin
