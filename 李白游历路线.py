import matplotlib.pyplot as plt
from adjustText import adjust_text
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False

# 李白生平重要地点
places = {
    '碎叶城(出生)': (75.3, 42.8),
    '四川江油(少年)': (104.7, 31.8),
    '峨眉山(游历)': (103.5, 29.6),
    '长安(求仕)': (108.9, 34.3),
    '洛阳(交友)': (112.4, 34.7),
    '开封(游历)': (114.3, 34.8),
    '襄阳(访孟浩然)': (112.1, 32.0),
    '黄鹤楼(送别)': (114.3, 30.5),
    '庐山(隐居)': (116.0, 29.5),
    '金陵(游历)': (118.8, 32.0),
    '当涂(终老)': (118.5, 31.5)
}

# 设置深色背景
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(16, 12))
ax.set_xlim(70, 130)
ax.set_ylim(15, 55)
ax.set_xlabel('经度', fontsize=14, color='white')
ax.set_ylabel('纬度', fontsize=14, color='white')
ax.set_title('李白生平游历路线图', fontsize=20, fontweight='bold', color='white')
ax.grid(True, alpha=0.2, color='white')

# 画连线 (用金色渐变效果)
lons = [p[0] for p in places.values()]
lats = [p[1] for p in places.values()]
ax.plot(lons, lats, color='#FFD700', linewidth=3, alpha=0.8, marker='o', markersize=12, 
        markerfacecolor='#FF6B6B', markeredgecolor='white', markeredgewidth=1.5)

# 智能标注 (金色字体，半透明黑底)
texts = []
for name, (lon, lat) in places.items():
    texts.append(ax.text(lon, lat, name, fontsize=11, fontweight='bold', color='#FFD700',
                          bbox=dict(boxstyle='round,pad=0.4', facecolor='black', alpha=0.7, edgecolor='#FFD700', linewidth=1)))

adjust_text(texts, arrowprops=dict(arrowstyle='->', color='#FFD700', lw=1.2, alpha=0.7))
plt.tight_layout()
plt.savefig('李白游历路线图.png', dpi=200, bbox_inches='tight', facecolor='black')
print("图片已保存为 李白游历路线图.png")
plt.show()