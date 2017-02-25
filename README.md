![piBox](/doc/pibox.png)

# Raspberry Pi Birdbox
A wooden birdbox with some extra gadgets courtesy of the Raspberry Pi.

## Gathering the neccesary items
### You Need
* A Raspberry Pi (we're using the Pi 1 Model B, but it will work on any Pi)
* A weight sensitive resistor (specifically https://goo.gl/8EGmAL)
* 6 Infared LEDS (we are using 850nm specifically ..., but use whatever ones you would like)
* 2 NPN transistors
* A Raspberry Pi Camera (https://shop.pimoroni.com/products/raspberry-pi-camera-module-v2-1-with-mount, IT HAS TO BE THE NoIR ONE otherwise it can't see infa-red)
* A lot of strip board (maybe bought here --> http://bright-components.co.uk/epages/950004269.sf/en_GB/?ObjectPath=/Shops/950004269/Categories/Prototyping/Strip_Board)
* A lot of wire

## Setting up the raspberry pi
Get the software here - https://www.raspberrypi.org/downloads/raspbian/
After it is downloaded, read this (https://www.raspberrypi.org/documentation/installation/installing-images/README.md) to learn how to put it onto your PI.
Now do type these commands into the PI's terminal window

```console
pi@pibox:~ $ git clone https://github.com/LazyAssassin445/pi-box.git
pi@pibox:~ $ pip3 install smbus2
```


## Cutting the wood
### Getting the dimensions
Now you have cloned the repository onto your raspberry pi, do this:

```console
pi@pibox:~ $ cd pibox
pi@pibox:~/pibox $ python3 dimensions.py
```

You have to input the thickness of the wood and the amount of overhang you would like, After that the program will print out the dimensions of the wood you need to cut and a diagram of how to cut the side panels.
You might have to scroll up to see all of the dimensions. Now cut the wood. Look at the OpenScad files to see how it fits together.

## Software
### Files you might want to look at
* https://cdn-learn.adafruit.com/downloads/pdf/adafruit-hdc1008-temperature-and-humidity-sensor-breakout.pdf
* https://cdn-shop.adafruit.com/datasheets/hdc1008.pdf

### Software you might want to download
* OpenSCAD (Used for the computer design of the birdbox) http://www.openscad.org/downloads.html
* Fritzing (Used for the computer design of the circuit boards) http://fritzing.org/download/
