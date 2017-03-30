from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)

x = 1
while True:
    sense.show_message("Dave Zirle is THE MAN!", scroll_speed=.04, text_colour=[255,0,255], back_colour=[0,0,0])
x += 1
