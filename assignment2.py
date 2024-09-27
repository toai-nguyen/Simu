import time
import pygame
from DHT22 import readSensor
from pnhLCD1602 import LCD1602

DHT_PIN = 4
MAX_TEMP = 30
ALARM_DURATION = 5000 

lcd = LCD1602()

max_temp = MAX_TEMP
alarm_active = False
alarm_start_time = 0

def display_temp_humidity(temp, humidity):
    lcd.clear()
    lcd.write_string(f"Temp: {temp:.1f}C")
    lcd.set_cursor(1, 0)
    lcd.write_string(f"Humidity: {humidity:.1f}%")

def display_max_temp():
    lcd.clear()
    lcd.write_string(f"Max Temp: {max_temp}C")
    lcd.set_cursor(1, 0)
    lcd.write_string("Press to adjust")

def handle_button_press(button):
    global max_temp, alarm_active
    if button == pygame.K_UP:
        max_temp += 1
    elif button == pygame.K_DOWN:
        max_temp -= 1
    
    display_max_temp()
    pygame.time.delay(500) 
    
    if alarm_active:
        stop_alarm()

def start_alarm():
    global alarm_active, alarm_start_time
    alarm_active = True
    alarm_start_time = pygame.time.get_ticks()
    lcd.clear()
    lcd.write_string("alarm!")
    print("Some sound is playing")

def stop_alarm():
    global alarm_active
    alarm_active = False
    print("Alarm stopped")

try:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    handle_button_press(event.key)
                elif alarm_active:
                    stop_alarm()
        
        temp, humidity = readSensor(DHT_PIN)
        
        if not alarm_active:
            display_temp_humidity(temp, humidity)
        
        if temp > max_temp and not alarm_active:
            start_alarm()
        
        if alarm_active and (pygame.time.get_ticks() - alarm_start_time > ALARM_DURATION):
            stop_alarm()
        
        pygame.time.delay(1000)

except KeyboardInterrupt:
    pass

finally:
    lcd.close()
    pygame.quit()