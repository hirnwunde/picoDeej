# picoDeej
Control your volume with potentiometers

---

The picoDeej is a device to control volume of different programs for Linux and Windows using [deej](https://github.com/omriharel/deej).
Unlike the original I don't use an Arduino but a RaspberryPi Pico to feed deej with data.


Assambling is quite straightforward.
Just note that the potentiometers have to be connected to AGND (Pin 33 on the Pico) and not to the 9 other GND pins. Took me a while to figure out why I don't get consistent analog readings.

Hardware needed:

    - a lot of jumper-wires
    - 3 Potentiometers (with knobs)
    - RaspberryPi Pico
    - USB-UART-Board

Limitations:

    - only three analog inputs
    - aditional USB-UART (Pico's USB is blocked by MicroPython's REPL)

Gerber files added but PCBs are stil in production.
When they arrive I will update this repo with new housing.
