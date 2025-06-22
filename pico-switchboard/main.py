from machine import Pin
from time import sleep

input_pins = [0,1,2,3,4,5,6,7,8,9,10,11]
output_pins = [12,13,14,15,16,17,18,19,20,21]

def read_line():
    output.on()
    result = ""
    for input in inputs:
        if input.value():
            result += '1'
        else:
            result += '0'
    output.off()
    return result

"----------- SETUP PINS -------------"
outputs = []
for output_pin in output_pins:
    outputs.append(Pin(output_pin, Pin.OUT, value = 0))
    
inputs = []
for input_pin in input_pins:
    inputs.append(Pin(input_pin, Pin.IN, Pin.PULL_DOWN))

"----------- READ GRID -------------"
result = []
for output in outputs:
    line_read = read_line()
    result.append(line_read)

[print(line) for line in result]