from machine import UART, Pin, PWM, I2C
from servo import Servo
import utime 
import _thread
#khoi tao uart
uart0= UART(0, 9600)
#khoi tao dong co servo
#dong co phan loại
motor1=Servo(16)
motor2=Servo(17)
#Nut nhan de nhan san pham vao

#cho ca 2 servo ve 0
motor1.move(-90)
motor2.move(-90)

#dieu khien dong co bang tai
pwmbt = PWM(Pin(2))
pwmbt.freq(3000)
adc_value = machine.ADC(2)

#Ham goi de chay da luong
def adc_pwm():
    while 1:
        pwmbt.duty_u16(adc_value.read_u16())
        utime.sleep(0.001)        
#chay da luong        
_thread.start_new_thread(adc_pwm, ())

#quay ve ham main
while 1:
    msg0 = uart0.readline()
    utime.sleep(1)
    if msg0 != None:
        if "M" in msg0 and sen1.value()==1:
            motor1.move(-30)
            utime.sleep(0.5)
            motor2.move(-90)
            print("position 1")         
        elif "H" in msg0 and sen2.value()==1:
            motor1.move(-90)
            utime.sleep(0.5)
            motor2.move(-30)              
            print("position 2")
        elif "B" in msg0 and sen3.value()==1:
            motor1.move(-90)
            motor2.move(-90)
            utime.sleep(0.5)
            print("position 3") 
    
        
        
      
    
