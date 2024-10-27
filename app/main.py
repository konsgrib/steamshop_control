import os
from temperature import SensorDS, SensorMAX
from distance import SensorSonar

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas.termo import TermoResponse, SensorList, Sensor

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/sensors")
def get_list_of_ds18b20():
    ds_device_dir = "/sys/bus/w1/devices/"
    items = os.listdir(ds_device_dir)
    filtered_items = [item for item in items if item.startswith("28-")]
    return filtered_items


@app.get("/status")
def main():
    ids = {
        "28-35b6d446f62b": "boiler",
        "28-0417301b9dff": "heat-out",
        "28-0214811929ff": "heat-in",
        "D5": "chmney",
        "18, 24": "pellet-level",
    }

    object_list = []
    ds_list = get_list_of_ds18b20()
    sensor_ds_objects = [SensorDS(sensor_id) for sensor_id in ds_list]
    try:
        temp_max = SensorMAX("D5")
        sensor_ds_objects.append(temp_max)
    except Exception as e:
        print("Failed to create MAX", str(e))
    try:
        dist_sens = SensorSonar(18, 24)
        sensor_ds_objects.append(dist_sens)
    except Exception as e:
        print("Failed to create Sonar", str(e))

    for item in sensor_ds_objects:
        object_list.append(
            {
                "sensor": ids.get(item.device_id),
                "value": item.get_data(),
                "device_id": item.device_id,
            }
        )

    return object_list


if __name__ == "__main__":
    main()
