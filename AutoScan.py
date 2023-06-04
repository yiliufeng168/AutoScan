import os
import sys

from config import RECEIVERS
from util import send_mail

if __name__ == '__main__':
    status = os.system("nmap " + " ".join(sys.argv[1:]))
    if status != 0:
        print("命令执行失败")
        sys.exit(1)
    for receiver in RECEIVERS:
        send_mail(receiver, '主机扫描结果', "扫描完成")
