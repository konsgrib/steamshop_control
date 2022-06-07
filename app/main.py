import os
from typing import Optional

from fastapi import FastAPI

from termo import read_temp, read_max

from sonar import get_distance

from schemas.termo import TermoResponse,SensorList,Sensor

app = FastAPI()


@app.get('/temperature',response_model=TermoResponse)
def get_temperature():
    return {
        'temperature': read_temp(),
        'chimney': read_max(),
        'distance': get_distance()
    }

def get_device_address(sensor_file):
    with open(sensor_file,'r') as f:
        line = f.readline().rstrip()
    return line.split(":")[0].strip()

def get_device_temperature(sensor_file):
    with open(sensor_file,'r') as f:
        line = f.readlines()[1].rstrip()
    return float(line.split("t=")[-1].strip()) /  1000

@app.get("/sensors",response_model=SensorList)
def get_sensors_list():
    lines = []
    sensors_path = "/sys/bus/w1/devices"
    master_file = "/sys/bus/w1/devices/w1_bus_master1/w1_master_slaves"
    with open(master_file,'r') as f:
        for line in f:
            sensor_file = os.path.join(sensors_path,
            line.strip(),
            'w1_slave')
            sensor = Sensor(
                id=line.strip(),
                name="",
                type="ds18d20",
                address= get_device_address(sensor_file),
                temperature=get_device_temperature(sensor_file))
            lines.append(sensor)
    return SensorList(sensors = lines)




if __name__ == "__main__":
    # get_temperature()
    print(read_temp())
    # print( read_max())
    print(get_distance())