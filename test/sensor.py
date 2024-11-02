from hub import light_matrix
import runloop
import color_sensor
from hub import port

async def main():
    # write your code here
    test = color_sensor.color(port.E)
    print(test)
    if test == 0:
        print('black')
    if test == 7:
        print('yellow')
    if test == 4:
        print('blue')

runloop.run(main())


