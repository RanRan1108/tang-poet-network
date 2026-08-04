import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Heiti SC']
matplotlib.rcParams['axes.unicode_minus'] = False
# 1. 构建诗人关系数据集
data = {
    '诗人A': ['李白', '李白', '李白', '李白', '杜甫', '杜甫', '杜甫', '杜甫', '王维', '王维', '孟浩然', '孟浩然', '高适', '高适', '王昌龄', '岑参'],
    '诗人B': ['杜甫', '孟浩然', '王昌龄', '贺知章', '高适', '岑参', '严武', '王维', '孟浩然', '裴迪', '王维', '张九龄', '岑参', '杜甫', '李白', '杜甫'],
    '关系类型': ['挚友', '忘年交', '诗友', '忘年交', '诗友', '诗友', '布衣之交', '诗友', '忘年交', '至交', '忘年交', '举荐', '诗友', '诗友', '诗友', '诗友']
}

df = pd.DataFrame(data)

# 2. 创建网络图
G = nx.Graph()
for _, row in df.iterrows():
    G.add_edge(row['诗人A'], row['诗人B'], relationship=row['关系类型'])

# 3. 计算每个诗人的“中心度”（影响力）
centrality = nx.degree_centrality(G)

# 4. 画图
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, seed=42, k=0.3)
node_size = [v * 8000 for v in centrality.values()]
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=node_size, font_size=12, font_weight='bold', edge_color='gray')
edge_labels = {(u, v): d['relationship'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='darkred')
plt.title('唐代诗人社交网络与影响力分析', fontsize=18)
plt.axis('off')
plt.savefig('tang_poet_network.png', dpi=150, bbox_inches='tight')
print("图片已保存为 tang_poet_network.png，请去文件夹查看")
plt.savefig('tang_poet_network.png', dpi=150, bbox_inches='tight') 