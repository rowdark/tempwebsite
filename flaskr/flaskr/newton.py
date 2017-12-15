# -*- coding: utf-8 -*-
# wc:精度 c:每年利息  m:本金 n:还剩几次付息 t:到下一次付息的时间/两次付息间隔 p0:现在的价格 y0:是猜测值
def gznewton(p0,c,m,n,t,y0,wc):
    done = 0
    y = y0
    while (done==0):
        fy=p0*(y**(n+t))-c-m
        fy1=p0*(n+t)*(y**(n+t-1))
        for i in range(n):
            fy=fy-c*(y**(n-i))
            fy1=fy1-c*(n-i)*(y**(n-i-1))
        if fy1!=0:
            Newton = y -(fy/fy1)
            #print Newton
            if (abs(Newton-y)<wc):#估计值小于精度
                done = 1
            elif (abs(Newton-y0)>0.2):
                print "请重新估计" #防止进入无限循环
            else:
                y = Newton
        else:
            done=1
    return Newton


if __name__ == '__main__':
    x=gznewton(155.45,11.83,100.0,6,0.85,1.1,0.00001)-1
    print "yield：%f" % x
