# Seamshop controll
Using Raspberry Pi as a host for sensots and API
- MAX6675K termocouple to measure chimney temperature
- DS16b20 sendors to measure boiler temperature and water temperature in the heating system and in the heating batteries 
- HC-SR04 sensor to measure level of the pellets inside the pellet bunker

to run as a daemon
docker-compose up --build -d

to run separately FASTAPI container:
uvicorn main:app  --reload --host 0.0.0.0 --port 8000


## Some hints
### ds18b20: 
https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/
https://raspberryautomation.com/connect-multiple-ds18b20-temperature-sensors-to-a-raspberry-pi/


### MAX6675K
https://forums.raspberrypi.com/viewtopic.php?t=145568
This works for me. First activate SPI interface in RPI Config, then install spidev.
Connect :(Chip -> Rpi) SCk -> SCLK, CS -> CE0, SO -> MISO


### HC-SR04 sensor
https://www.anavi.org/article/209/
https://www.youtube.com/watch?v=ShnzQSFwVXQ


