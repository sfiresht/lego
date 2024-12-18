#import pybricks
from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.tools import wait


# Initialize the Move Hub
hub = MoveHub()
#print("current battery voltage: {0}".format(battery.voltage()))
# Initialize motors on ports A and B
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)
motor_d = Motor(Port.D)
sensor = ColorDistanceSensor(Port.C)

# Run both motors for 2 seconds
motor_a.run_time(500, 2000, then=Stop.HOLD,wait=False)
motor_b.run_time(-500, 2000, then=Stop.HOLD)
#print(motor_d.angle())
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