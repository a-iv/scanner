import serial
import win32api

def run():
    source = serial.Serial(port='COM5', baudrate=9600)
    source.open()
    while True:
        while source.read(1) != 'B':
            pass
        value = ''
        while len(value) < 11:
            value += source.read(1)
        if source.read(2) == '\n\r':
            for char in value:
                win32api.keybd_event(ord(char), 0, 0, 0)
        else:
            print 'Incorrect suffix for value:', value
