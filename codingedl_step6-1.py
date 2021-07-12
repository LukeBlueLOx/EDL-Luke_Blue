from components import Button
button = Button("D7")

while True:
    if button.is_pressed:
        buzzer.on()
    else:
        buzzer.off()