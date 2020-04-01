# portas.py
""" módulo que contém classes de portas logicas """
import numpy as np

class AndGate:
    def __init__ ( self, dlay: float = 2 ) -> None:
        self.delay = dlay * 1e-9 # atraso em nano segundos originalmente, convertidopara segundos
        
    def go( self, input_a: 'array' = 0, input_b: 'array' = 0 , sam_period = 1) -> 'array':
        shift = round(self.delay / sam_period)
        input_a = np.array(input_a)
        #input_a = np.roll(input_a, shift)
        #input_a[0:shift]=0
        input_b = np.array(input_b)
        #input_b = np.roll(input_b, shift)
        #input_b[0:shift]=0
        print(shift, input_a, input_b)
        self.output = np.roll(np.logical_and( input_a, input_b),shift)
        self.output[0:shift]=0
