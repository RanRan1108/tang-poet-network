import matplotlib.pyplot as plt
from adjustText import adjust_text
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False

# 李白生平重要地点
libai_places = {
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

# 杜甫生平重要地点
dufu_places = {
    '河南巩义(出生)': (112.9, 34.8),
    '洛阳(少年游历)': (112.4, 34.7),
    '长安(求仕困居)': (108.9, 34.3),
    '奉先(探亲)': (109.5, 35.0),
    '羌村(避难)': (109.2, 36.0),
    '成都(草堂安居)': (104.0, 30.6),
    '夔州(寓居)': (109.5, 31.0),
    '岳阳(漂泊)': (113.1, 29.4),
    '长沙(潭州)': (112.9, 28.2),
    '耒阳(卒于舟中)': (112.9, 26.4)
}

# 深色背景学术风
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(18, 14))
ax.set_xlim(70, 125)
ax.set_ylim(22, 48)
ax.set_xlabel('经度', fontsize=14, color='white')
ax.set_ylabel('纬度', fontsize=14, color='white')
ax.set_title('李白与杜甫游历路线对比', fontsize=22, fontweight='bold', color='white')
ax.grid(True, alpha=0.2, color='white')

# 画李白路线 (金色)
lb_lons = [p[0] for p in libai_places.values()]
lb_lats = [p[1] for p in libai_places.values()]
ax.plot(lb_lons, lb_lats, color='#FFD700', linewidth=3, alpha=0.8, marker='o', markersize=10,
        markerfacecolor='#FF6B6B', markeredgecolor='white', markeredgewidth=1.5, label='李白')

# 画杜甫路线 (青色)
df_lons = [p[0] for p in dufu_places.values()]
df_lats = [p[1] for p in dufu_places.values()]
ax.plot(df_lons, df_lats, color='#00CED1', linewidth=3, alpha=0.8, marker='s', markersize=10,
        markerfacecolor='#4169E1', markeredgecolor='white', markeredgewidth=1.5, label='杜甫')

# 标注李白地点
texts_lb = []
for name, (lon, lat) in libai_places.items():
    texts_lb.append(ax.text(lon, lat, name, fontsize=10, fontweight='bold', color='#FFD700',
                              bbox=dict(boxstyle='round,pad=0.3', facecolor='black', alpha=0.7, edgecolor='#FFD700', linewidth=1)))

# 标注杜甫地点
texts_df = []
for name, (lon, lat) in dufu_places.items():
    texts_df.append(ax.text(lon, lat, name, fontsize=10, fontweight='bold', color='#00CED1',
                              bbox=dict(boxstyle='round,pad=0.3', facecolor='black', alpha=0.7, edgecolor='#00CED1', linewidth=1)))

# 合并所有标注，避免重叠
adjust_text(texts_lb + texts_df, arrowprops=dict(arrowstyle='->', color='gray', lw=1, alpha=0.7))

ax.legend(loc='upper right', fontsize=14)
plt.tight_layout()
plt.savefig('李杜路线对比图.png', dpi=200, bbox_inches='tight', facecolor='black')
print("图片已保存为 李杜路线对比图.png")
plt.show()