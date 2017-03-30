from sense_hat import SenseHat
import functools

sense = SenseHat()
sense.clear()
sense.set_rotation(270)

def tofahrenheit(celsius):
    return( (celsius/5*9)+32 )

colour = (255, 0, 255)
speed = (.04)

while True:
    temp = tofahrenheit(sense.get_temperature())
    temp = round(temp, 1)

    if temp < 70:
        colour = (0, 0, 255)
    elif temp < 80:
        colour = (255, 255, 0)
    else:
        colour = (255, 0, 0)

    my_show_message = functools.partial(sense.show_message, text_colour=colour, scroll_speed=speed)

    my_show_message("Temp is")
    my_show_message(str(temp))
    my_show_message("degrees!")
