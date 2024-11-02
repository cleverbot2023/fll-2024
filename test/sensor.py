from hub import light_matrix
import runloop
import color_sensor
from hub import port

async def main():
    # write your code here
    test = color_sensor.color(port.E)
    print(test)

runloop.run(main())

