import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Chọn chân GPIO 17 để phát hiện ngắt
channel = 17
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Hàm callback khi phát hiện ngắt
def my_callback(channel):
    print("Có sự thay đổi trạng thái!")

# Thêm phát hiện ngắt (both - phát hiện cả rising và falling edge)
GPIO.add_event_detect(channel, GPIO.BOTH, callback=my_callback, bouncetime=300)

# Chờ vô hạn để kiểm tra sự kiện
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
