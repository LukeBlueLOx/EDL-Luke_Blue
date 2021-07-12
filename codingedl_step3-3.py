red_led = LED("D2")
yellow_led = LED("D3")
green_led = LED("D4")

if distance < 10:
    red_led.on()
    yellow_led.on()
    green_led.on()
elif distance < 20:
    red_led.off()
    yellow_led.on()
    green_led.on()
else:
    red_led.off()
    yellow_led.off()
    green_led.on()