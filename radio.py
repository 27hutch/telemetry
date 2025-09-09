# radio.py

import board
import busio
import digitalio
import adafruit_rfm9x

from config import (
    LORA_FREQ_MHZ,
    LORA_TX_POWER,
)

def init_radio() -> adafruit_rfm9x.RFM9x:
    """Initialize SPI + RFM9x and return the radio object."""
    

    print(board)
    print(board.SCK)
    print(board.MOSI)
    print(board.MISO)
    # print(board.R
    # print(board.reset)

    spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    
    CS_PIN = board.D4
    RST_PIN = board.D23


    cs = digitalio.DigitalInOut(CS_PIN)
    reset = digitalio.DigitalInOut(RST_PIN)

    print(spi)
    print(cs)
    print(reset)
    
    radio = adafruit_rfm9x.RFM9x(spi, cs, reset, LORA_FREQ_MHZ)
    radio.tx_power = LORA_TX_POWER
    
    return radio
