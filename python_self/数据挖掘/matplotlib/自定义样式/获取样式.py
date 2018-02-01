import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#我们引入了ticker，允许我们修改图表底部的ticker信息。
import matplotlib.ticker as mticker
#然后我们从matplotlib.finance模块中引入candlestick_ohlc功能。
from matplotlib.finance import candlestick_ohlc
from matplotlib import style

print(plt.style.available)
print(plt.__file__)
