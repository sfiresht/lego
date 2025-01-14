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

# Run both motors for 2 seconds
# the wait=false flag tells the code not to wait to this line to finish, instead just ove on, that way the next motor will be running as wel at the same time

#move forward
motor_a.run_time(-500, 3000, then=Stop.HOLD,wait=False)  
motor_b.run_time(500, 3000, then=Stop.HOLD)

#turn right
motor_a.run_time(-500, 760, then=Stop.HOLD,wait=False)
motor_b.run_time(-500, 760, then=Stop.HOLD)


def rect():
    #move forward
    motor_a.run_time(-500, 3000, then=Stop.HOLD,wait=False)  
    motor_b.run_time(500, 3000, then=Stop.HOLD)

    #turn right
    motor_a.run_time(-500, 800, then=Stop.HOLD,wait=False)
    motor_b.run_time(-500, 800, then=Stop.HOLD)
    #move motor d for an angle
    #print(motor_d.angle())


#move your head
motor_d.run_angle(30,30, then=Stop.HOLD)
wait(2000)
motor_d.run_angle(60,-60, then=Stop.HOLD)
motor_d.run_angle(30,30, then=Stop.HOLD)
print("back on track")



print(Color.RED)
sensor.light.on(Color.RED)
wait(5000)
sensor.light.off()

# Say goodbye and give some time to send it.
print("Goodbye!")
wait(100)


# Shut the hub down.
hub.system.shutdown()

# Change LED color to red
#hub.light.on((100, 0, 0))  # RGB: Red <<<<< doesn't work