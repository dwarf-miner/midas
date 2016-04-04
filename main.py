# -*- coding: UTF-8 -*-
import tushare as ts
import pandas as pd

df=ts.get_hist_data('601231',start='2015-04-01')
# 所有的结果汇图
df.plot()
# 只将stock最高值进行汇图
df.high.plot()
# 指定绘图的四个量，并指定线条颜色
with pd.plot_params.use('x_compat', True):
    df.open.plot(color='g')
    df.close.plot(color='y')
    df.high.plot(color='r')
    df.low.plot(color='b')
# 指定绘图的长宽尺度及背景网格
with pd.plot_params.use('x_compat', True):
    df.high.plot(color='r',figsize=(10,4),grid='on')
    df.low.plot(color='b',figsize=(10,4),grid='on')

