import matplotlib.pyplot as plt
from adjustText import adjust_text
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False

# 杜甫生平重要地点 (按时间顺序)
places = {
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
fig, ax = plt.subplots(figsize=(16, 12))
ax.set_xlim(100, 120)
ax.set_ylim(20, 40)
ax.set_xlabel('经度', fontsize=14, color='white')
ax.set_ylabel('纬度', fontsize=14, color='white')
ax.set_title('杜甫生平漂泊路线图', fontsize=20, fontweight='bold', color='white')
ax.grid(True, alpha=0.2, color='white')

# 画连线 (用冷色调：青色)
lons = [p[0] for p in places.values()]
lats = [p[1] for p in places.values()]
ax.plot(lons, lats, color='#00CED1', linewidth=3, alpha=0.8, marker='o', markersize=12,
        markerfacecolor='#4169E1', markeredgecolor='white', markeredgewidth=1.5)

# 智能标注
texts = []
for name, (lon, lat) in places.items():
    texts.append(ax.text(lon, lat, name, fontsize=11, fontweight='bold', color='#00CED1',
                          bbox=dict(boxstyle='round,pad=0.4', facecolor='black', alpha=0.7,
                                    edgecolor='#00CED1', linewidth=1)))

adjust_text(texts, arrowprops=dict(arrowstyle='->', color='#00CED1', lw=1.2, alpha=0.7))
plt.tight_layout()
plt.savefig('杜甫游历路线图.png', dpi=200, bbox_inches='tight', facecolor='black')
print("图片已保存为 杜甫游历路线图.png")
plt.show()