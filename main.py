from speedtest import Speedtest
import time
import pandas as pd
from datetime import datetime
from tqdm import tqdm


def convert_to_mbps(value):
    return round(value / 10**6)


st = Speedtest()
df = pd.DataFrame(columns=['Time', 'Download'])
for i in tqdm(range(5)):
    download = convert_to_mbps(st.download())
    df = df._append({'Time': datetime.now().strftime("%H-%M-%S"), 'Download': download}, ignore_index=True)
    time.sleep(120)

df.to_csv('speedtest.csv', index=False)
