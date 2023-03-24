import RPi.GPIO as GPIO
import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI
import time

LED = 11 

LIGHT = 1  # Channel number of Light Sensor for ADC
light_thresh = 100

SOUND = 0  # Channel of Sound Sensor
sound_thresh = 200

def init():
	GPIO.setmode(GPIO.BOARD)
	
	# LED Pin
	GPIO.setup(LED, GPIO.OUT)
	
	# Software SPI Configuration
	SPI_PORT   = 0
	SPI_DEVICE = 0
	mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
	return mcp
	
	

def blink_LED(n, interval):
	for i in range(0, n):
		GPIO.output(LED, 1)
		time.sleep(interval)
		GPIO.output(LED, 0)
		time.sleep(interval)

def read_light_sensor(mcp):
	t = 0
	while t <= 5:
		val = mcp.read_adc(LIGHT)
		
		if (val > light_thresh):
			print(val, "bright")
		else:
			print(val, "dark")
			
		# Wait 100ms
		time.sleep(0.1)
		t += 0.1
		
def read_sound_sensor(mcp):
	t = 0
	while t <= 5:
		val = mcp.read_adc(SOUND)
		print(val)
		
		if (val > sound_thresh):
			GPIO.output(LED, 1) # Turn on LED
			
		# Wait 100ms
		time.sleep(0.1)
		t += 0.1
			
		if (val > sound_thresh):
			GPIO.output(LED, 0) # Turn off LED
			
			

if __name__ == "__main__":
	mcp = init()
	
	while(True):
		blink_LED(5, 0.5)
		read_light_sensor(mcp)
		blink_LED(4, 0.2)
		read_sound_sensor(mcp)
	
	
	
	
