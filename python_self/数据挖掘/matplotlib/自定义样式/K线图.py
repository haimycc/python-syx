import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#我们引入了ticker，允许我们修改图表底部的ticker信息。
import matplotlib.ticker as mticker
#然后我们从matplotlib.finance模块中引入candlestick_ohlc功能。
from matplotlib.finance import candlestick_ohlc
from matplotlib import style


import numpy as np
import urllib
import datetime as dt

plt.style.use('dark_background')

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))

    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1m/csv'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)


    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          converters={0: bytespdate2num('%Y%m%d')})

    #构建一个Python列表，其中每个元素都是数据。
    # 我们可以修改我们的loadtxt函数，使其不解构，
    # 但随后我们还是希望引用特定的数据点。
    # 我们可以解决这个问题，但是我们最后可能只拥有两个单独的数据集。
    x = 0
    y = len(date)
    ohlc = []

    while x < y:
        #把每一天的日期加入到ohlc列表中
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x+=1

    #K线图,设置上升颜色和下降颜色
    #candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')
    ax1.plot(date, closep)
    ax1.plot(date, openp)

    #设置x轴的刻度
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    #设置x轴日系形式
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    #将x标签设置为我们想要的数量
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)


    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('EBAY')
