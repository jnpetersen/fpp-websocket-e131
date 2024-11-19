def parse_e131(packet):
    # Extract DMX data starting from byte 126
    dmx_data = packet[126:]
    return [dmx_data[i:i+3] for i in range(0, len(dmx_data), 3)]  # RGB triplets
