from scapy.all import sniff, IP, TCP, UDP, ICMP

# Function to process and analyze each captured packet
def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        # Determine the protocol type
        if proto == 6:  # TCP
            protocol = "TCP"
        elif proto == 17:  # UDP
            protocol = "UDP"
        elif proto == 1:  # ICMP
            protocol = "ICMP"
        else:
            protocol = str(proto)

        print(f"[+] Packet: {ip_src} -> {ip_dst} (Protocol: {protocol})")

        # Print TCP/UDP payload data (if any)
        if protocol == "TCP" or protocol == "UDP":
            payload = bytes(packet[TCP].payload) if protocol == "TCP" else bytes(packet[UDP].payload)
            if payload:
                print(f"Payload: {payload}\n")

# Start sniffing packets (default interface)
print("Starting packet sniffer... Press Ctrl+C to stop.")
sniff(filter="ip", prn=packet_callback, store=0)
