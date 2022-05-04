This config works.
Includes sample FastAPI app and Nginx both are in docker containers starting by docker-compose

to start is use:
docker-compose up --build

to run as a daemon
docker-compose up --build -d


ds18b20: 
https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/
https://raspberryautomation.com/connect-multiple-ds18b20-temperature-sensors-to-a-raspberry-pi/


MAX6675K
https://forums.raspberrypi.com/viewtopic.php?t=145568
This works for me. First activate SPI interface in RPI Config, then install spidev.
Connect :(Chip -> Rpi) SCk -> SCLK, CS -> CE0, SO -> MISO


HC-SR04 sensor
https://www.anavi.org/article/209/
https://www.youtube.com/watch?v=ShnzQSFwVXQ
# steamshop_control
