import pandas as pd
import speedtest
import time
from io import StringIO

s = speedtest.Speedtest()
s.get_best_server()
header = pd.read_csv(StringIO(s.results.csv_header() + ",Test Timestamp"), sep=',')
print(header)
header.to_csv('ARIAtest.csv', mode='a', index=False)

while True:
    try:
        speedtest.Speedtest()
        s.download()
        s.upload()
        data = pd.read_csv(StringIO(s.results.csv() + ",{date}".format(date=pd.Timestamp.now())), sep=',')
        print(data)
        data.to_csv('ARIAtest.csv', mode='a', index=False)
    except Exception as exc:
        print("[!!!] {err} {date}".format(err=exc,date=pd.Timestamp.now()))
        error = pd.read_csv(StringIO(",,,,,,,,,,{date}".format(date=pd.Timestamp.now())))
        error.to_csv('ARIAtest.csv', mode='a', index=False)
        time.sleep(15)