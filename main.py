import machine
from utime import sleep
from scalenum import scale_number

uart = machine.UART(0, 9600, parity=None, stop=1, bits=8)

adc0=machine.ADC(machine.Pin(26))
adc1=machine.ADC(machine.Pin(27))
adc2=machine.ADC(machine.Pin(28))

while True:
  val0 = scale_number(adc0.read_u16(), 0, 1023, 176, 65535)
  val1 = scale_number(adc1.read_u16(), 0, 1023, 176, 65535)
  val2 = scale_number(adc2.read_u16(), 0, 1023, 176, 65535)

  outstr = str(int(val0)) + '|' + str(int(val1)) + '|' + str(int(val2))

  print(outstr)
  uart.write(outstr + '\r\n')

  sleep(0.1)
