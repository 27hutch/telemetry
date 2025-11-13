# stationary_rx.py

import struct
import time
import csv
from pathlib import Path

from config import (
    LORA_NETWORK_ID,
    LORA_NODE_ID_ROVER,
)
from radio import init_radio

# Packet format must match rover_tx.py
PKT = struct.Struct(">BBI")  # net_id (1B), src_id (1B), seq (uint32)

def parse_packet(b: bytes):
    if len(b) != PKT.size:
        return None
    try:
        return PKT.unpack(b)  # (net_id, src_id, seq)
    except struct.error:
        return None

def main():
    radio = init_radio()
    print("Stationary RX: listening for rover beacons...")

    log_path = Path("rssi_log.csv")
    new_file = not log_path.exists()

    with log_path.open("a", newline="") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["timestamp_s", "seq", "rssi_dbm", "snr_db", "raw_hex"])

        try:
            while True:
                pkt = radio.receive(timeout=2.0)  # seconds
                if pkt is None:
                    continue

                t = time.monotonic()
                parsed = parse_packet(pkt)
                if not parsed:
                    print(f"[WARN] bad packet len={len(pkt)}: {pkt.hex()}")
                    continue

                net_id, src_id, seq = parsed
                if net_id != LORA_NETWORK_ID or src_id != LORA_NODE_ID_ROVER:
                    continue

                rssi_dbm = radio.rssi                     # e.g., -45
                snr_db = getattr(radio, "snr", None)       # may be None

                print(
                    f"[RX] t={t:.1f}s seq={seq} RSSI={rssi_dbm} dBm"
                    + (f" SNR={snr_db} dB" if snr_db is not None else "")
                )

                w.writerow([f"{t:.3f}", seq, rssi_dbm, snr_db if snr_db is not None else "", pkt.hex()])
                f.flush()
        except KeyboardInterrupt:
            print("Stationary RX stopped. Log saved to", log_path)

if __name__ == "__main__":
    main()
