import RPi.GPIO as GPIO

LED = 12

# SPI
CLK = 18
MISO = 23
MOSI = 24
CS = 25

LIGHT = 0 # Channel number of Light Sensor for ADC
light_thresh = 20

SOUND = 3 # Channel of Sound Sensor
sound_thresh = 20

def init():
	GPIO.setmode(GPIO.BOARD)
	
	# LED Pin
	GPIO.setup(LED, GPIO.OUT)
	
	# Software SPI Configuration
	mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
	return mcp
	
	

def blink_LED(n, interval):
	for i in range(0, n):
		GPIO.output(LED, 1)
		sleep(interval)
		GPIO.output(LED, 0)
		sleep(interval)

def read_light_sensor(mcp):
	t = 0
	while t <= 5:
		val = mcp.read_adc(LIGHT)
		
		if (val > light_thresh):
			print(val, "bright")
		else:
			print(val, "dark")
			
		# Wait 100ms
		sleep(0.1)
		t += 0.1
		
def read_sound_sensor(mcp):
	t = 0
	while t <= 5:
		val = mcp.read_adc(SOUND)
		print(val)
		
		if (val > sound_thresh):
			GPIO.output(LED, 1) # Turn on LED
			
		# Wait 100ms
		sleep(0.1)
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
	
	
	
	
