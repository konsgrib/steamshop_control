import os
import glob
import time
 
import board
import busio
import digitalio
import adafruit_max31855
import RPi.GPIO as GPIO



base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]


def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def get_list_of_ds18b20():
    base_dir = '/sys/bus/w1/devices/'
    items = os.listdir(base_dir)
    filtered_items = [os.path.join(base_dir,item,'w1_slave') for item in items if item.startswith('28-')]
    return filtered_items

# ['35 01 4b 46 7f ff 0c 10 5f : crc=5f YES\n', '35 01 4b 46 7f ff 0c 10 5f t=19312\n']
def parse_temp_raw(temp_raw):
    temp_val = temp_raw[1]
    temp = temp_val.split('t=')[1]
    temp_c = float(temp) / 1000.0
    return temp_c


def main():
    sensors = get_list_of_ds18b20()
    for sensor in sensors:
        temp_raw = read_temp_raw(sensor)
        temp = parse_temp_raw(temp_raw)
        print(sensor,': ',temp)




if __name__=="__main__":
    main()


