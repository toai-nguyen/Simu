import Adafruit_DHT
import time

# Thiết lập cảm biến và chân GPIO
SENSOR = Adafruit_DHT.DHT22  # Hoặc Adafruit_DHT.DHT11 nếu bạn sử dụng DHT11
PIN = 4  # GPIO4 (chân số 7 trên Raspberry Pi)

try:
    while True:
        # Đọc giá trị nhiệt độ và độ ẩm từ cảm biến
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)

        # Kiểm tra nếu đọc thành công
        if humidity is not None and temperature is not None:
            print(f'Nhiệt độ: {temperature:.1f}°C, Độ ẩm: {humidity:.1f}%')
        else:
            print('Không đọc được giá trị từ cảm biến, vui lòng kiểm tra kết nối.')

        # Dừng một chút trước khi đọc lần tiếp theo
        time.sleep(2)

except KeyboardInterrupt:
    print("Dừng chương trình.")
