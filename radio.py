# radio.py

import board
import busio
import digitalio
import adafruit_rfm9x

from config import (
    LORA_FREQ_MHZ,
    LORA_TX_POWER,
    # RFM9X_VIN,
    # RFM9X_GND,
    # RFM9X_MISO,
    # RFM9X_SCK,
    # RFM9X_MOSI,
    RFM9X_CS,
    RFM9X_RST
)

def init_radio() -> adafruit_rfm9x.RFM9x:
    """Initialize SPI + RFM9x and return the radio object."""
    
    spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    
    cs_pin = getattr(board, RFM9X_CS)
    reset_pin = getattr(board, RFM9X_RST)
    # vin_pin = getattr(board, RFM9X_VIN)
    # gnd_pin = getattr(board, RFM9X_GND)
    # miso_pin = getattr(board, RFM9X_MISO)
    # sck_pin = getattr(board, RFM9X_SCK)
    # mosi_pin = getattr(board, RFM9X_MOSI)

    cs = digitalio.DigitalInOut(cs_pin)
    reset = digitalio.DigitalInOut(reset_pin)
    # vin = digitalio.DigitalInOut(vin_pin)
    # gnd = digitalio.DigitalInOut(gnd_pin)
    # miso = digitalio.DigitalInOut(miso_pin)
    # sck = digitalio.DigitalInOut(sck_pin)
    # mosi = digitalio.DigitalInOut(mosi_pin)


    radio = adafruit_rfm9x.RFM9x(spi, cs, reset, LORA_FREQ_MHZ)
    radio.tx_power = LORA_TX_POWER
    
    return radio
