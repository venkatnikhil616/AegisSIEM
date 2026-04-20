class PacketParser:
    def parse(self, packet):
        try:
            if isinstance(packet, dict):
                return packet
            return None
        except:
            return None
