#Gilbert Nyame
#ENGR 010
#Lab 6
#GIN226
from gpiozero import CamJamKitRobot
from gpiozero import LED, DistanceSensor
from time import sleep
sensor=DistanceSensor(echo=18, trigger=17, max_distance=1)
robot= CamJamKitRobot()
LED1=LED(22)
LED2=LED(23)
movementlist=[]
def organizing (command, Lspeed, Rspeed, duration):
	if command=='Forward':
		Forward(Lspeed, Rspeed, duration)
	if command=='Back':
		Back(Lspeed, Rspeed, duration)
	if command=="TurnRight":
		LED1.on()
		TurnRight(Lspeed, Rspeed, duration)
	if command=="TurnLeft":
		LED2.on()
		TurnLeft(Lspeed, Rspeed, duration)
	if command=="SpinRight":
		LED1.on()
		SpinRight(Lspeed, Rspeed, duration)
	if command=='SpinLeft':
		LED2.on()
		SpinLeft(Lspeed, Rspeed, duration)
	if command=='Stop':
		Stop(duration)

def Forward (Lspeed, Rspeed, duration):
	print("Going Forward")
	robot.value=(Lspeed,Rspeed)
	sleep(duration)
	for i in range (int(duration*10)):
		sleep(0.1)
def Back (Lspeed, Rspeed, duration):
	print("Going back")
	robot.value=(-Lspeed,-Rspeed)
	sleep(duration)
	for i in range (int(duration*10)):
		sleep(0.1)
def TurnRight (Lspeed, Rspeed, duration):
	print("Turning Right")
	LED1.on() 
	Rspeed=0
	robot.value=(Lspeed, Rspeed)
	sleep(duration)
	LED1.off()
	for i in range(int(duration*10)):
		sleep(0.1)
def TurnLeft (Lspeed, Rspeed, duration):
	print("Turning Left")
	LED2.on()
	Lspeed=0
	robot.value= (Lspeed, Rspeed)
	sleep(duration)
	LED2.off()
	for i in range(int(duration*10)):
		sleep(0.1)
def SpinLeft (Lspeed, Rspeed, duration):
	print("Spining Left")
	LED2.on()
	robot.value=(-Lspeed, Rspeed)
	sleep(duration)
	LED2.off()
	for i in range(int(duration*10)):
		sleep(0.1)
def SpinRight (Lspeed, Rspeed, duration):
	print("Spining Right")
	LED1.on()
	robot.value=(Lspeed, -Rspeed)
	sleep(duration)
	LED1.off()
	for i in range(int(duration*10)):
		sleep(0.1)
def Stop (duration):
	print(f"Stopping for {duration} seconds")
	Rspeed=0
	Lspeed=0
	robot.value=(Lspeed, Rspeed)
	sleep(duration)
	for i in range(int(duration*10)):
		sleep(0.1)
def organizing(command, Lspeed, Rspeed, duration):
	if command=='Forward':
		Forward(Lspeed, Rspeed, duration)
	if command=='Back':
		Back(Lspeed, Rspeed, duration)
	if command=='TurnRight':
		LED1.on()
		TurnRight(Lspeed, Rspeed, duration)
	if command=='TurnLeft':
		LED2.on()
		TurnLeft(Lspeed, Rspeed, duration)
	if command=='SpinRight':
		LED1.on()
		SpinRight(Lspeed, Rspeed, duration)
	if command=='SpinLeft':
		LED2.on()
		SpinLeft(Lspeed, Rspeed, duration)
	if command=='Stop':
		Stop(duration)
	else:
		LED1.off()
		LED2.off()

with open ("scripted_commands.txt", "r") as fh:
	for i in fh:
		nocommas=i.strip('\n').split(',')
		movementlist.append(nocommas)
for i in movementlist:
	i[1]=float(i[1])
	i[2]=float(i[2])
	i[3]=float(i[3])
alternated_movement_list=[]
with open("alternated_scripted_commands.txt","r") as fh2:
	for i in fh2:
		nocommas2=i.strip('\n').split(',')
		alternated_movement_list.append(nocommas2)
for i in alternated_movement_list:
	i[1]=float(i[1])
	i[2]=float(i[2])
	i[3]=float(i[3])

while True:
	while sensor.distance>0.10:
		for i in movementlist:
			organizing(i[0],i[1],i[2],i[3])
			if sensor.distance<0.10:
				print("Something is near")
				for i in alternated_movement_list:
					organizing(i[0],i[1],i[2],i[3])
					sleep(0.1)
