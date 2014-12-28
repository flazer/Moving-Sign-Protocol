#!/usr/local/bin/python

import package
import argparse
import serial
import time

def connect():
  ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
  )
  ser.open()
  ser.isOpen()
  return ser


parser = package.Parser.parse()
Commands = package.Commands
command = Commands.build(package, parser.parse_args())
ser = connect()
ser.write(command)

out = ''
time.sleep(1)
while ser.inWaiting() > 0:
  out += ser.read(1)
  if out != '':
    print ">>" + out

