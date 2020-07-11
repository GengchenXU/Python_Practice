'''
@Description: 
@Sample Intput: 
@Output: 
@Autor: GengchenXu
@Date: 2020-06-09 14:23:20
@LastEditTime: 2020-06-09 17:42:08
'''

from pyecharts import Bar

columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

bar = Bar("柱状图", "一年的降水量与蒸发量")

bar.add("降水量", columns, data1, mark_line=["average"], mark_point=["max", "min"])
bar.add("蒸发量", columns, data2, mark_line=["average"], mark_point=["max", "min"])

bar.render()
bar