from sense_hat import SenseHat
import functools

sense = SenseHat()
sense.clear()

def tofahrenheit(celsius):
    return( (celsius/5*9)+32 )

colour = (255, 0, 255)
speed = (.04)
my_show_message = functools.partial(sense.show_message, text_colour=colour, scroll_speed=speed)

while True:
    temp = tofahrenheit(sense.get_temperature())
    temp = round(temp, 1)

    sense.set_rotation(270)
    my_show_message("Temp is")
    my_show_message(str(temp))
    my_show_message("degrees.")
