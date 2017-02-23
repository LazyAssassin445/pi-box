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
Follow this link to set it up ...
After you have done this type this command on it

```console
pi@pibox:~ $ git clone https://github.com/LazyAssassin445/pi-box.git
```


## Cutting the wood
### Getting the dimensions
Now you have cloned the repository onto your raspberry pi, do this:

```console
pi@pibox:~ $ cd pibox
pi@pibox:~/pibox $ python3 dimensions.py
```

You have to input the thickness of the wood and the amount of overhang you would like, After that the program will print out the dimensions of the wood you need to cut and a diagram of how to cut the side panels.
You might have to scroll up to see all of the dimensions.
