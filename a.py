import matplotlib.pyplot as plt
import networkx as nx

# 创建有向图
G = nx.DiGraph()

# 添加词语与文档ID的关系
inverted_index = {
    "brutus": [1, 2, 3, 11],
    "caesa": [1, 2, 3, 4, 5, 6],
    "calpurnia": [2, 3, 4, 5]
}

# 添加节点和边
for term, docs in inverted_index.items():
    for doc in docs:
        G.add_edge(term, f"Doc {doc}")

# 设置布局为横向
pos = nx.spring_layout(G, seed=42, k=2)  # 调整 k 参数让节点横向分布

# 绘制图表
plt.figure(figsize=(10, 5))
nx.draw(G, pos, with_labels=True, node_color="lightblue", font_size=10, node_size=3000, arrows=True, arrowstyle='->', arrowsize=20)
plt.title("Inverted Index Graph")
plt.show()
