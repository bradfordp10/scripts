import pandas as pd
import speedtest
import time
from io import StringIO

s = speedtest.Speedtest()
header = pd.read_csv(StringIO(s.results.csv_header()), sep=',')
print(header)
header.to_csv('ARIAtest.csv', mode='a', index=False)

while True:
    try:
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        data = pd.read_csv(StringIO(s.results.csv()), sep=',')
        print(data)
        data.to_csv('ARIAtest.csv', mode='a')
    except Exception as exc:
        print("[!!!] {err}".format(err=exc))
        error = pd.read_csv(StringIO(",,,{date}Z,,,,,,".format(date=pd.Timestamp.now().isoformat())))
        error.to_csv('ARIAtest.csv', mode='a')
        time.sleep(15)