import time
import pygame
from pygame.locals import *

pygame.init()
pygame.joystick.init()
joystick_num = pygame.joystick.get_count()

print('{} joysticks is available'.format(joystick_num))

mystick:pygame.joystick.Joystick

for i in range(0,joystick_num):
    stick = pygame.joystick.Joystick(i)
    if stick.get_guid()=="030000005e0400008e02000000007200":
        mystick = stick
        print("device {} is found and id is {}".format(mystick.get_name(),mystick.get_id()))
        break

# mystick = pygame.joystick.Joystick(0)
# print("device {} is found and id is {}".format(mystick.get_name(),mystick.get_id()))

mystick.init()
print('{} axis exist'.format(mystick.get_numaxes()))



# axis=5 forward range from -1(full stop)~1(full acc)
# axis=0 left or right from -1(full left)~0(whell stay)~1(full right)




print('move the vJoy feeder')
for i in range(0,4):
    print(i)
    time.sleep(1)


# read the data
series=[]
for i in range(0,100000):
    pygame.event.pump()
    # time.sleep(2)
    vec=[]
    vec.append(mystick.get_axis(5))
    vec.append(mystick.get_axis(0))
    vec.append(mystick.get_button(5))
    print(vec)
    series.append(vec)


print('please close the vJoy Feeder to avoid the confict')
for i in range(0,4):
    time.sleep(1)
    print(i)

# feed the VJoy
from vjoy import *
vj.open()
for i in range(0,len(series)):
    x=series[i][0]
    y=series[i][1]
    z=series[i][2]
    setJoy(x,y)
    vj.setButton(1,z)
    time.sleep( 0.0001 )
vj.close()
