# geradores.py
""" módulo que contém geradores de sinais """
import numpy as np

class SquareWave:
    def __init__( self, dcycle: float = 0.5, ttime: float = 10, fs: float = 1e3, freq: float = 1 ) -> None:
        self.duty_cycle = dcycle 
        self.total_time = ttime  
        self.sampling_frequency = fs
        self.time = np.arange(0, self.total_time, 1/self.sampling_frequency)
        self.frequency = freq
        self.period = 1/self.frequency
        rem = np.remainder(self.time,self.period)/self.period
        self.signal = rem > (1-self.duty_cycle)
