# 绘制直方图

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import random

my_font = fm.FontProperties(fname="C:\Windows\Fonts\simsun.ttc")
plt.figure(figsize=(50,30), dpi=80)

a = [137, 156, 117, 85, 100, 113, 156, 133, 85, 128, 75, 110, 101, 89, 84, 142, 98, 77, 102, 156, 75, 114, 86, 86, 146, 132, 73, 103, 130, 112, 149, 113, 96, 149, 87, 148, 85, 96, 81, 134, 106, 84, 121, 113, 97, 130, 79, 102, 144, 81, 105, 126, 119, 84, 103, 140, 98, 148, 134, 125, 104, 114, 132, 108, 158, 113, 149, 152, 157, 127, 130, 101, 125, 138, 114, 76, 91, 136, 113, 140, 84, 132, 97, 93, 84, 121, 122, 129, 79, 75, 137, 130, 107, 73, 79, 114, 75, 121, 154, 78, 73, 117, 78, 136, 99, 89, 101, 87, 121, 155, 130, 151, 140, 81, 91, 123, 150, 94, 100, 84, 103, 155, 112, 149, 127, 90, 144, 134, 127, 131, 88, 90, 147, 86, 127, 119, 97, 140, 154, 80, 93, 117, 74, 85, 115, 104, 80, 152, 83, 100, 115, 104, 86, 77, 80, 136, 75, 81, 102, 99, 124, 81, 79, 112, 79, 93, 142, 111, 105, 138, 84, 148, 108, 115, 96, 131, 109, 94, 75, 132, 81, 142, 147, 142, 102, 120, 140, 91, 85, 82, 134, 149, 158, 100, 124, 81, 79, 129, 138, 76, 99, 122, 94, 112, 87, 122, 108, 119, 81, 107, 130, 96, 103, 112, 96, 87, 93, 130, 135, 133, 130, 101, 129, 91, 89, 151, 149, 138, 123, 153, 147, 92, 157, 111, 131, 114, 148, 81, 153, 116, 157, 153, 104, 84, 126, 100, 94, 136, 88, 106]

# 组距
d = 5
# 计算组数
group = (max(a) - min(a)) // d
# 绘制
plt.hist(a,group,edgecolor='skyblue')
# 设置x轴刻度
plt.xticks(range(min(a),max(a)+d, d),fontsize=40)

plt.yticks(fontsize=40)

plt.grid(alpha=1)

plt.show()