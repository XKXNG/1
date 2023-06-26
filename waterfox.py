import os
import time
print("Is Waterfox Installed?")
water = input("y/n: ")
if water == "n":
	os.system('wget https://cdn1.waterfox.net/waterfox/releases/G5.1.8/Linux_x86_64/waterfox-G5.1.8.tar.bz2')
	time.sleep(5)
	os.system('tar -xvf waterfox-G5.1.8.tar.bz2')
else:
	os.system('cd Downloads && cd waterfox && ./waterfox')
