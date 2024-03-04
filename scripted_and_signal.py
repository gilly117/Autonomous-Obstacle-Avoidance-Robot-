#GILBERT NYAME
#ENGR 010
#Lab 6
#GIN226
from gpiozero import CamJamKitRobot
from gpiozero import LED
from time import sleep
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
def Back (Lspeed, Rspeed, duration):
	print("Going back")
	robot.value=(-Lspeed,-Rspeed)
	sleep(duration)
def TurnRight (Lspeed, Rspeed, duration):
	print("Turning Right")
	LED1.on() 
	Rspeed=0
	robot.value=(Lspeed, Rspeed)
	sleep(duration)
	LED1.off()
def TurnLeft (Lspeed, Rspeed, duration):
	print("Turning Left")
	LED2.on()
	Lspeed=0
	robot.value= (Lspeed, Rspeed)
	sleep(duration)
	LED2.off()
def SpinLeft (Lspeed, Rspeed, duration):
	print("Spining Left")
	LED2.on()
	robot.value=(-Lspeed, Rspeed)
	sleep(duration)
	LED2.off()
def SpinRight (Lspeed, Rspeed, duration):
	print("Spining Right")
	LED1.on()
	robot.value=(Lspeed, -Rspeed)
	sleep(duration)
	LED1.off()
def Stop (duration):
	print(f"Stopping for {duration} seconds")
	Rspeed=0
	Lspeed=0
	robot.value=(Lspeed, Rspeed)
	sleep(duration)
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
for i in movementlist:
	organizing(i[0],i[1],i[2],i[3])

