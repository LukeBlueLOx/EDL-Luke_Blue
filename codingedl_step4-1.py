from components import Buzzer
buzzer = Buzzer("D5")
if distance < 10:
    red_led.on()
    yellow_led.on()
    green_led.on()
    buzzer.on()
elif distance < 20:
    red_led.off()
    yellow_led.on()
    green_led.on()
else:
    red_led.off()
    yellow_led.off()
    green_led.on()