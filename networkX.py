"""from turtle import pd

import matplotlib
import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt, font_manager

import matplotlib.font_manager as fm
from matplotlib import rc

font_path = "C:\Windows\Fonts\malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


matplotlib.rcParams['axes.unicode_minus'] = False
#-*-coding:utf-8-*-
df = pd.DataFrame({'from': [ '모르핀','모르핀','모르핀','모르핀','모르핀','모르핀','모르핀','모르핀','모르핀','모르핀'],
                   'to': ['메스암페타민', '조인트', '암페타민', '적당량', '재배지', '청산가리','코카인', '파이프', '태양광', '프로포폴'],
                   'weight': [1, 2, 3, 4, 5, 6,7,8,9,10]})

g = nx.from_pandas_edgelist(df, 'from', 'to', create_using = nx.DiGraph())

matplotlib.rc('font',family=font)
nx.draw(g, with_labels=True)

plt.show()

"""