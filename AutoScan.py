import argparse
import nmap
from config import RECEIVERS
from util import send_mail


def progress_callback(host, scan_data):
    print('------------------')
    print('Host:', host)
    print('State:', scan_data['nmap']['scanstats']['uphosts'])
    print('Open ports:', list(scan_data['scan'][host]['tcp'].keys()))


def main(host):
    nm = nmap.PortScannerAsync()
    nm.scan(hosts=host, arguments='-p- -sS -T4', callback=progress_callback)
    while nm.still_scanning():
        print('Waiting...')
        nm.wait(2)
    for receiver in RECEIVERS:
        send_mail(receiver, '主机扫描结果', nm.csv())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scan hosts in LAN')
    parser.add_argument('--host', type=str, default='', help='Host to scan')
    args = parser.parse_args()
    main(args.host)