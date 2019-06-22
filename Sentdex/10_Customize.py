import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates
from matplotlib import style
style.use("ggplot")


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):

    fig = plt.figure()
    # Subplot args: (shape), (starting_point), rowSpan, colSpan
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    """
    Getting the Data for our plot
    """
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          converters={0: bytespdate2num('%Y-%m-%d')})

    # Customizing individual subplot
    ax1.plot_date(date, closep,'-', label='Price')
    # gets all the ticklabels in x axis
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    # Adding a grid to our plot
    ax1.grid(True)  # color='g', linestyle='-', linewidth=5

    # Parameters for whole graph
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('TSLA')
