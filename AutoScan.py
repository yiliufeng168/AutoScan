import argparse
import os

from config import RECEIVERS
from util import send_mail


def main(host):
    os.system('nmap -sP %s' % host)
    for receiver in RECEIVERS:
        send_mail(receiver, '主机扫描结果', "扫描完成")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scan hosts in LAN')
    parser.add_argument('--host', type=str, default='', help='Host to scan')
    args = parser.parse_args()
    main(args.host)
