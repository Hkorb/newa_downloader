from datetime import datetime
from pathlib import Path

from newa_downloader import DataPoint, TimeSpan, download_mesoscale_timeseries

time_span = TimeSpan(datetime(2008, 1, 1), datetime(2008,1,2))
point = DataPoint(57.18, 18.3)
file = Path("visby_2008.nc")
variables = ["WS"]
heights = [50, 100]
download_mesoscale_timeseries(file, variables, point, time_span, heights)
