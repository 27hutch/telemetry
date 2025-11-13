# rover_tx.py

import struct
import time

from config import (
    BEACON_HZ,
    LORA_NETWORK_ID,
    LORA_NODE_ID_ROVER,
)
from radio import init_radio

# Packet: [ net_id (1B) | src_id (1B) | seq (uint32, 4B) ]
PKT = struct.Struct(">BBI")

def build_packet(seq: int) -> bytes:
    return PKT.pack(LORA_NETWORK_ID, LORA_NODE_ID_ROVER, seq)

def main():
    radio = init_radio()
    period = 1.0 / BEACON_HZ
    seq = 0
    print(f"Rover TX: sending at {BEACON_HZ} Hz")

    try:
        while True:
            t0 = time.monotonic()

            try:
                radio.send(build_packet(seq))
                print(f"TX seq={seq}")
            except Exception as e:
                print(f"[WARN] radio send failed: {e}")

            seq = (seq + 1) & 0xFFFFFFFF

            dt = time.monotonic() - t0
            if (sleep := period - dt) > 0:
                time.sleep(sleep)
    except KeyboardInterrupt:
        print("Rover TX stopped")

if __name__ == "__main__":
    main()
