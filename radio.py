# radio.py

import board
import busio
import digitalio
import adafruit_rfm9x

from config import (
    LORA_FREQ_MHZ,
    LORA_TX_POWER_DBM,
    RFM9X_CS_PIN_NAME,
    RFM9X_RESET_PIN_NAME,
)

def init_radio() -> adafruit_rfm9x.RFM9x:
    """Initialize SPI + RFM9x and return the radio object."""
    spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

    cs_pin = getattr(board, RFM9X_CS_PIN_NAME)
    reset_pin = getattr(board, RFM9X_RESET_PIN_NAME)

    cs = digitalio.DigitalInOut(cs_pin)
    reset = digitalio.DigitalInOut(reset_pin)

    radio = adafruit_rfm9x.RFM9x(spi, cs, reset, LORA_FREQ_MHZ)
    radio.tx_power = LORA_TX_POWER_DBM

    # Optional tuning for range/robustness:
    # radio.signal_bandwidth = 125000   # Hz
    # radio.coding_rate = 5
    # radio.spreading_factor = 7

    return radio
