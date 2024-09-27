import pigpio  
import time  

# Khởi tạo pigpio  
pi = pigpio.pi()  

# Đặt GPIO pin của servo (thay đổi theo pin bạn đã chọn)  
servo_pin = 18  

# Hàm để điều khiển servo  
def set_servo_angle(angle):  
    pulse_width = (angle * 1000 / 180) + 500  # Tính toán độ rộng xung  
    pi.set_servo_pulsewidth(servo_pin, pulse_width)  

try:  
    while True:  
        for angle in range(0, 181, 5):  # Quay từ 0 độ đến 180 độ  
            set_servo_angle(angle)  
            time.sleep(0.1)  
        for angle in range(180, -1, -5):  # Quay từ 180 độ về 0 độ  
            set_servo_angle(angle)  
            time.sleep(0.1)  
except KeyboardInterrupt:  
    print("Dừng điều khiển servo")  
    pi.set_servo_pulsewidth(servo_pin, 0)  # Dừng servo  
finally:  
    pi.stop()  # Ngắt kết nối pigpio