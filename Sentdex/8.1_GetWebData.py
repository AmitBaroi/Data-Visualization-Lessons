import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


def bytespdate2num(fmt, encoding='utf-8'):
    """fmt = format"""
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):
    # Data for our Request to Stock API Server
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11, Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    }
    # Making the Request
    req = urllib.request.Request(stock_price_url, headers=headers)
    src_code = urllib.request.urlopen(req).read().decode()
    # ontainer for data
    stock_data = []
    # Separating lines of src code
    split_src = src_code.split("\n")
    for line in split_src[1:]:
        split_line = line.split(",")
        if(len(split_line)) == 7:
            if "values" not in line and 'labels' not in line:
                stock_data.append(line)
    """
    Converters:
    %Y = ful year       2015
    %y = partial year     15
    %m = number month
    %d = number day
    %H = hours
    %M = minutes
    %S = seconds
    """
    (date, closep, highp, lowp, openp, volume) = np.loadtxt(stock_data,
                                                           delimiter=",",
                                                           unpack=True,
                                                           converters={0: bytespdate2num("%Y-%m-%d")})

    plt.plot_date(date, closep, "-", label="Reading data using Numpy module!")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph!\nCheck it out!')
    plt.legend()
    plt.show()


graph_data('TSLA')
