![piBox](/doc/pibox.png)

# Raspberry Pi Birdbox
A wooden birdbox with some extra gadgets courtesy of the Raspberry Pi.
# Sorry for all of the really messy code

## Setting up the raspberry pi
Now you have your Raspberry Pi you need to put software on it. Go the this link https://www.raspberrypi.org/downloads/raspbian/ to download the latest copy of Raspbian
After it has downloaded, follow this link (https://www.raspberrypi.org/documentation/installation/installing-images/README.md) to learn how to install it onto your Pi
When you first boot up your pi it will come up with a login window, your login details are as follows
Username: pi
Password: raspberry
When you are in, type these commands into the PI's terminal window.

```console
pi@pibox:~ $ git clone https://github.com/LazyAssassin445/pi-box.git
pi@pibox:~ $ pip3 install smbus2
```


## Building
### Wood
#### Getting the Dimensions
Now you have cloned the repository onto your raspberry pi, do this:

```console
pi@pibox:~ $ cd pibox
pi@pibox:~/pibox $ python3 dimensions.py
```
You have to input the thickness of the wood and the amount of overhang you would like on the lid over the front. After that the program will print out the dimensions of the wood you need to cut and a diagram of how to cut the side panels.
You might have to scroll up to see all of the dimensions. Now cut the wood. 

#### Assembling the birdbox

You can install OpenSCAD (http://www.openscad.org/downloads.html) to look at the digital version of how the wood fits together.

### Electronics
#### What You Need
#### Things that are shared between all of the boards
* Connector plugs
    - 5, 3 pin (http://bright-components.co.uk/epages/950004269.sf/en_GB/?ObjectPath=/Shops/950004269/Products/pcbconnectorkit3way)
    - 1, 4 pin (http://bright-components.co.uk/epages/950004269.sf/en_GB/?ObjectPath=/Shops/950004269/Products/pcbconnectorkit4way)
    - 1, 6 pin (http://bright-components.co.uk/epages/950004269.sf/en_GB/?ObjectPath=/Shops/950004269/Products/pcbconnectorkit6way)
    - 1, 2 pin (http://bright-components.co.uk/epages/950004269.sf/en_GB/?ObjectPath=/Shops/950004269/Products/pcbconnectorkit2way)
    - 1, 2 pin header (http://bright-components.co.uk)
* Wire

#### For the Ditribution Board You Need
* Strip Board (25 cols. x 20 rows)
* One Pi Cobbler (26 pins)
* If you have a newer Pi with 40 pins you will need a 40 pin to 26 pin ribbon cable
* If you have an older Pi with 26 pins you need a 26 pin ribbon cable

#### For the LED Boards You Need
* Strip Board
    -
* 6 850nm infared LED's
* 2 NPN Transistors
* 2 4.7k ohm resistors
* 2 1k ohm resistors

#### For the Force Sensing Board You Need
* Strip Board
    - 1 piece of 10 cols. x 13 rows 
    - 1 piece of 5 cols. x 5 rows
* Variable Resistor 100k (http://bright-components.co.uk/epages/950004269.sf/en_GB/?ObjectPath=/Shops/950004269/Products/3386_100K)
* Variable Resistor 10k (http://bright-components.co.uk/epages/950004269.sf/en_GB/?ObjectPath=/Shops/950004269/Products/3386_10K)
* A weight sensitive resistor (specifically https://goo.gl/8EGmAL)
* 1 16 pin IC socket
* 1 MCP 3008 ADC chip

#### Assembling
#### Assembling the Distribution Board
First cut all of the nessesary tracks like so ...
![distributionboardbreadboard](/doc/circuitboards/distributionboardbreadboard.png)
Then solder on the wires and the sockets (UART is the 3 pin header, not the plug), then the cobbler.
![distributionboard](/doc/circuitboards/distributionboard.png)

#### Assembling the Force Sensor Board
First cut all the tracks needed
![forceboardbreadboard](/doc/circuitboards/forceboardbreadboard.png)
Then solder on the wires, the IC socket, the variable resistor and the plugs (2 pin)
![forceboard](/doc/circuitboards/forceboard.png)

#### Assembling the LED Boards
First cut all the tracks needed
![ledboardbreadboard](/doc/circuitboards/ledboardbreadboard.png)
After that solder on the resistors, the connectors and the NPN transistor
### THEN SOLDER THE LEDS ON ON THE OTHER SIDE OF THE STRIP BOARD
![ledboard](/doc/circuitboards/ledboard.png)
(not 100% accurate)



## Software
### Testing
Now that you have all of your things connected to your Pi (shown in the picture of the distribution board), we can get on with testing.

#### Force Sensor Testing
```console
pi@pibox:~ $ cd ~/pi-box/testprograms
pi@pibox:~/pi-box/testprograms $ python3 weighttest
```
#### Temperature/Humidity Sensor Testing
```console
pi@pibox:~ $ cd ~/pi-box/testprograms
pi@pibox:~/pi-box/testprograms $ python3 temphumidtest
```
#### LED Testing
Answer the question depending on where you have your LED boards plugged in
```console
pi@pibox:~ $ cd ~/pi-box/testprograms
pi@pibox:~/pi-box/testprograms $ python3 ledtest

What GPIO port would you like to test? 

```
#### Camera Testing
Answer the question depending on where you want to save the picture
```console
pi@pibox:~ $ cd ~/pi-box/testprograms/camera
pi@pibox:~/pi-box/testprograms/camera $ python3 oneshot

Where would you like to save this image? 

```



### Files you might want to look at
* https://cdn-learn.adafruit.com/downloads/pdf/adafruit-hdc1008-temperature-and-humidity-sensor-breakout.pdf
* https://cdn-shop.adafruit.com/datasheets/hdc1008.pdf

### Software you might want to download
* OpenSCAD (Used for the computer design of the birdbox) http://www.openscad.org/downloads.html
* Fritzing (Used for the computer design of the circuit boards) http://fritzing.org/download/

