import RPi.GPIO as GPIO
import time

# Thiết lập GPIO
GPIO.setmode(GPIO.BCM)
channel = 17  # Sử dụng GPIO 17 cho ví dụ

GPIO.setup(channel, GPIO.IN)

def callback(channel):
    print("Phát hiện thay đổi trạng thái!")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
