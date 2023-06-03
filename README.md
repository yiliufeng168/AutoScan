# AutoScan

## 描述
这是一个基于nmap的自动扫描工具，可以自动扫描目标的开放端口，然后根据端口类型进行相应的扫描，最后将扫描结果保存到文件中。在扫描完成后，可以通知用户扫描完成。

## 使用
```shell
python3 AutoScan.py -h
usage: AutoScan.py [-h] [-t TARGET] [-p PORT] [-s SCAN] [-n NOTIFY]
```

