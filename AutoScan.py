import nmap
from config import RECEIVERS
from util import send_mail

nm = nmap.PortScanner()
nm.scan(hosts='192.168.0.1/24', arguments='-sS -T4')

while nm.still_scanning():
    progress = nm.progress
    print("Scan is", progress, "percent complete.")


for receiver in RECEIVERS:
    send_mail(receiver, '主机扫描结果', nm.csv())
