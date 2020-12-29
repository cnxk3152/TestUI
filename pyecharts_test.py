# -*- coding:utf-8 -*-
#pyecharts可视化
from pyecharts.charts import Bar,Pie,Line,Scatter,EffectScatter,Grid
from pyecharts import options as opts
from pyecharts.faker import Faker

#matplotlib 最新版已有修正，老版本中的方法已修改或弃用
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
#下面两行可以显示中文 SimHei指的是黑体，KaiTi指的是楷体

# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType,SymbolType
'''
新细明体：PMingLiU
细明体：MingLiU
标楷体：DFKai-SB
黑体：SimHei
宋体：SimSun
新宋体：NSimSun
仿宋：FangSong
楷体：KaiTi
仿宋_GB2312：FangSong_GB2312
楷体_GB2312：KaiTi_GB2312
微软正黑体：Microsoft JhengHei
微软雅黑体：Micsoroft YaHei
'''
'''
plt.rcParams['font.sans-serif']=['SimHei'] #设置简黑字体
plt.rcParams['axes.unicode_minus'] = False #解决‘-’bug

#产生随机数
np.random.seed(19680801)

# 定义数据的分布特征
mu = 100
sigma = 15
x = mu + sigma * np.random.randn(437)

num_bins = 50

fig, ax = plt.subplots()

n, bins, patches = ax.hist(x, num_bins, density=1) #normed弃用 改为density

# 添加图表元素
y = norm.pdf(bins, mu, sigma)#malt.normpdf弃用，改用norm里scipy.stats
ax.plot(bins, y, '--')
ax.set_xlabel('柱状图')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# 图片展示与保存
fig.tight_layout()
plt.savefig("Histogram.png")
plt.show()
'''
#=====================pyecharts============================
'''
#1
bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()
'''
'''
#2
bar = (
    Bar()
    .add_xaxis(["PC", "手机", "笔记本", "XBox", "PS4", "SWitch"])
    .add_yaxis("商家B", [5, 20, 36, 10, 75, 90])
)
bar.render()
'''
'''
#V1 版本开始支持链式调用
# 你所看到的格式其实是 `black` 格式化以后的效果
# 可以执行 `pip install black` 下载使用
bar = (
    Bar()
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家C", [5, 20, 36, 10, 75, 90])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    # 或者直接使用字典参数
    # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
)
bar.render()
'''

#内置主题类型可查看 pyecharts.globals.ThemeType  以下pyecharts版本1.7.1
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .add_yaxis("商家C", [10, 2, 30, 75, 99, 50])
    .set_global_opts(title_opts=opts.TitleOpts(title="柱状图", subtitle="销量"),
                     legend_opts=opts.LegendOpts(pos_left="20%"))
)
#bar.render("aa.html")

attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
high_tem = [11, 11, 15, 13, 12, 13, 10]
low_tem = [1, -2, 2, 5, 3, 2, 0]
line = (
    Line()
    .add_xaxis(attr)
    .add_yaxis(series_name="最高气温",
               y_axis=high_tem,
               markpoint_opts=opts.MarkPointOpts(
                   data=[
                       opts.MarkPointItem(type_="max", name="最大值"),
                       opts.MarkPointItem(type_="min", name="最小值"),
                   ]
               ),
               markline_opts=opts.MarkLineOpts(
                   data=[opts.MarkLineItem(type_="average", name="平均值")]
               ),
               )

    .add_yaxis(
        series_name="最低气温",
        y_axis=low_tem,
        markpoint_opts=opts.MarkPointOpts(
          data=[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)]
        ),
        markline_opts=opts.MarkLineOpts(
          data=[
              opts.MarkLineItem(type_="average", name=""),
              opts.MarkLineItem(symbol="none", x="90%", y="max"),
              opts.MarkLineItem(symbol="circle", type_="max", name="最高点")
          ]
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="气温图", subtitle="虚构", pos_left="50%"),
                     tooltip_opts=opts.TooltipOpts(trigger="axis"),
                     toolbox_opts=opts.ToolboxOpts(is_show=True, pos_right="60%"),
                     xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,),
                     yaxis_opts=opts.AxisOpts(),
                     legend_opts=opts.LegendOpts(pos_left="65%"),
                     )
)
line.render("line.html")

v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]

scatter = (
    Scatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("aa", v1)
    .set_global_opts(title_opts=opts.TitleOpts(title="散点图", pos_top="50%"),
                     legend_opts=opts.LegendOpts(pos_top="50%", pos_left="20%"))
)
scatter.render("scatter.html")

v3 = [11,11,15,13,12,13,10]
v4 = [1,-2,2,5,3,2,0]

es = (
    EffectScatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("不同Symbol", Faker.values(), symbol=SymbolType.ARROW)
    .set_global_opts(title_opts=opts.TitleOpts(title="动态散点图", pos_top="50%", pos_left="50%"),
                     legend_opts=opts.LegendOpts(pos_top="50%", pos_left="70%"))
)
es.render("es.html")

grid = (
    Grid(init_opts=opts.InitOpts(width="1200px", height="720px"))
    .add(bar, grid_opts=opts.GridOpts(pos_right="60%", pos_bottom="60%"))
    .add(line, grid_opts=opts.GridOpts(pos_left="60%", pos_bottom="60%"))
    .add(scatter, grid_opts=opts.GridOpts(pos_right="60%", pos_top="60%"))
    .add(es, grid_opts=opts.GridOpts(pos_left="60%", pos_top="60%"))
)

grid.render("duotu.html")
