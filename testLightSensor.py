import RPi.GPIO as GPIO
import time

# Thiết lập chân GPIO
LIGHT_SENSOR_PIN = 4  

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)

try:
    while True:
        # Đọc giá trị từ cảm biến ánh sáng
        if GPIO.input(LIGHT_SENSOR_PIN) == GPIO.LOW:
            print("Có ánh sáng")
        else:
            print("Không có ánh sáng")
        
        # Dừng một chút trước khi đọc lần tiếp theo
        time.sleep(1)

except KeyboardInterrupt:
    print("Dừng chương trình.")

finally:
    # Dọn dẹp GPIO sau khi kết thúc chương trình
    GPIO.cleanup()
