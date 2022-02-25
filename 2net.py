
import matplotlib.pyplot as plt
import networkx
import numpy as np
import pandas as pd

import networkx as nx
from apyori import apriori


dataset = pd.read_csv('C:/keyword.csv')
""" ['엑스터시', '메스암페타민'],
 ['엑스터시', '탄산가스'],
 ['엑스터시', '암페타민'],
 ['엑스터시', '적당량'],
 ['엑스터시', '재배지'],
 ['엑스터시', '청산가리'],
 ['엑스터시', '코카인'],
 ['엑스터시', '칸나비디올'],
 ['엑스터시', '태양광'],
 ['엑스터시', '프로로폴'],

 ['모르핀', '메스암페타민'],
 ['모르핀', '조인트'],
 ['모르핀', '암페타민'],
 ['모르핀', '적당량'],
 ['모르핀', '재배지'],
 ['모르핀', '청산가리'],
 ['모르핀', '코카인'],
 ['모르핀', '파이프'],
 ['모르핀', '태양광'],
 ['모르핀', '프로로폴'],

 ['메스암페타민', '모르핀'],
 ['메스암페타민', '치사량'],
 ['메스암페타민', '암페타민'],
 ['메스암페타민', '적당량'],
 ['메스암페타민', '탄산가스'],
 ['메스암페타민', '코카인'],
 ['메스암페타민', '플라워'],
 ['메스암페타민', '플랜트'],
 ['메스암페타민', '태양광'],
 ['메스암페타민', '프로로폴'],

 ['암페타민', '코카인'],
 ['암페타민', '제조법'],
 ['암페타민', '암페타민'],
 ['암페타민', '적당량'],
 ['암페타민', '재배지'],
 ['암페타민', '청산가리'],
 ['암페타민', '패러독스'],
 ['암페타민', '펜토바르비탈'],
 ['암페타민', '헤로인'],
 ['암페타민', '환각제'],"""
G = nx.Graph()

for ind in range((len(np.where(dataset['freq']>=20000)[0]))):
   G.add_edge(dataset['title'][ind], dataset['keyword'][ind], weight=int(dataset['freq'][ind]))

dgr = nx.degree_centrality(G)
btw = nx.betweenness_centrality(G)
cls = nx.closeness_centrality(G)
egv = nx.eigenvector_centrality(G)
pgr = nx.pagerank_centrality(G)

pr = nx.pagerank(G)
nsize = np.array([v for v in pr.values()])
nsize = 100000*(nsize-min(nsize)/max(nsize)-min(nsize))

pos = nx.spring_layout(G)
plt.Figure(figsize=(16,12)); plt.axis('off')
nx.draw_networkx(G, font_family='Malgun Gothic', font_size=10, pos=pos, node_color=list(pr.values()), node_size=nsize, alpha=0.7, edge_color='.5', cmap=plt.cm.rainbow)
plt.rc('font', family='Malgun Gothic')
plt.show()