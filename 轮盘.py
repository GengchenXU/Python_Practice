from random import random
from math import sin,cos,pi
from tkinter.messagebox import showinfo
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
plt.rcParams['font.sans-serif']=['SimHei']

data={'一等奖':0.08,'二等奖':0.22,'三等奖':0.7}
fig=plt.figure()#设置画布
ax1=plt.axes([0.1,0.15,0.8,0.8])
ax1.pie(data.values(),labels=data.keys(),radius=1)
ax1.plot([0,1],[0,0],lw=3,color='yellow')
def motion(event):
    buttonStart.set_active(False)  #禁用按钮，避免重复响应
    position=0
    step=random()*2
    ax1.lines.clear()
    ax1.plot([0,cos(position)],[0,sin(position)],lw=3,color='yellow')
    plt.draw_all(True)
    for i in range(150):
        if i%15==0:
            step=max(0,step-0.2)
        if step<1e-2:
            break
        position=position+step

        plt.pause(0.05)
        ax1.lines.clear()



        ax1.plot([0,cos(position)],[0,sin(position)],lw=3,color='yellow')
        #强制更新图形
        plt.draw_all(True)
        #启动按钮
    buttonStart.set_active(True)
    position=position%(2*pi)
    ratio=position/(2*pi)
    if ratio>data['一等奖'] + data['二等奖']:
        showinfo('恭喜','三等奖')
    elif ratio>data['一等奖']:
        showinfo('恭喜','二等奖')
    else:
        showinfo('恭喜','一等奖')
#创建子图，放置按钮
ax2=plt.axes([0.45,0.1,0.1,0.05])
buttonStart=Button(ax2,'Start',color='pink',hovercolor='white')
buttonStart.on_clicked(motion)
plt.show()
    
