from machine import Pin, ADC, UART
from utime import sleep
from scalenum import scale_number

# different from the normal micropython UART needs no init()
uart = UART(0, 9600, parity=None, stop=1, bits=8)

adc0=ADC(Pin(26))
adc1=ADC(Pin(27))
adc2=ADC(Pin(28))

while True:
  # Pico's ADC returns values between 0 and 65535
  # deej expect values between 0 and 1023 (or 1024?)
  # the lowest value my potentiometers provide are 176
  # this function will remap the values 176-65535 to 0-1023
  val0 = scale_number(adc0.read_u16(), 0, 1023, 176, 65535)
  val1 = scale_number(adc1.read_u16(), 0, 1023, 176, 65535)
  val2 = scale_number(adc2.read_u16(), 0, 1023, 176, 65535)

  outstr = str(int(val0)) + '|' + str(int(val1)) + '|' + str(int(val2))

  print(outstr)
  uart.write(outstr + '\r\n')

  sleep(0.1)
