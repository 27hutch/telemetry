# config.py

# --- Radio / LoRa settings ---
LORA_FREQ_MHZ = 900.0        # or 900.0 / 868.0 depending on your module + region
LORA_TX_POWER = 20           # dBm, check allowed limits for your country

# LORA_NODE_ID_ROVER = 0x01
# LORA_NODE_ID_GROUND = 0x02

# Optional: simple "network" ID so you don't pick up random packets
LORA_NETWORK_ID = 0x42

# --- SPI / GPIO pin mappings (BCM numbering) ---
# SPI_BUS = 0
# SPI_DEVICE = 0

# RFM9x pins (adjust for your wiring)
RFM9X_VIN = 1
RFM9X_GND = 6
RFM9X_MISO = 21
RFM9X_SCK = 23
RFM9X_MOSI = 19
RFM9X_CS = 7
RFM9X_RST = None #Specify by choosing a digital pin
# RFM9X_RST 
# RFM9X_G0

# --- Telemetry settings ---
TELEMETRY_HZ = 5.0    # send data 5 times per second from rocket
