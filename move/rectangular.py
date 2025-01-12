#import pybricks
from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.tools import wait


# Initialize the Move Hub
hub = MoveHub()

#print("current battery voltage: {0}".format(battery.voltage()))
# Initialize motors on ports A and B (Builtin ports)
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)

motor_d = Motor(Port.D)
sensor = ColorDistanceSensor(Port.C)


def turn_90_deg(side):
    if side=='right':
        #turn right 90 degrees
        motor_a.run_time(-500, 850, then=Stop.HOLD,wait=False)
        motor_b.run_time(-500, 850, then=Stop.HOLD)
    elif side=='left':
        #turn left 90 degrees
        motor_a.run_time(500, 850, then=Stop.HOLD,wait=False)
        motor_b.run_time(500, 850, then=Stop.HOLD)

def rect():
    #each run of this function will get one side of the rectangular + turn right
    #move forward
    motor_a.run_time(-500, 3000, then=Stop.HOLD,wait=False)  
    motor_b.run_time(500, 3000, then=Stop.HOLD)
    turn_90_deg('right')





for i in range(4):
    rect()
    

print("back to step 1")
print(Color.RED)
sensor.light.on(Color.RED)
wait(2000)
sensor.light.off()

# Say goodbye and give some time to send it.
print("Goodbye!")
wait(100)


# Shut the hub down.
hub.system.shutdown()
