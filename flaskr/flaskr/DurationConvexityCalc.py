# -*- coding: UTF-8 -*-

# c is coupon rate
# v is face value
# f is payment frequency
# n is the number of interest payments from now on
# i is the index
# y[i] is the corresponding yield when index is i
# pv is the presnt value

import matplotlib.pyplot as plt

#作用: 计算单个y的久期Duration
#Input: c,v,f,n,y,pv
#Output: D(y)
def DurationCalcwithY(c,v,f,n,y,pv):
    tmp = 0
    for idx in xrange(1,n+1):
        tmp = tmp + idx/((1+y/f)**(idx+1))
    return float(v)/(f*pv)*(float(c)/f*tmp+n/((1+y/f)**(n+1)))
    #return -float(v)/(f*pv)*(float(c)/f*tmp+n/((1+y/f)**(n+1))) #positive?

#作用: 计算单个y的凸性Convexity
#Input: c,v,f,n,y,pv
#Output: C(y)
def ConvexityCalcwithY(c,v,f,n,y,pv):
    tmp = 0
    for idx in xrange(1,n+1):
        tmp = tmp + idx*(idx+1)/((1+y/f)**(idx+2))
    return float(v)/(f*pv)*(float(c)/f*tmp+n*(n+1)/((1+y/f)**(n+2)))

#作用: 计算多个y的久期Duration
#Input: c,v,f,n,y1-yn,pv
#Output: D(y1)-D(yn)
def DurationCalcwithArrayY(c,v,f,n,y,pv):
    res = [DurationCalcwithY(c,v,f,n,y[j-1],pv) for j in xrange(1,n+1)];
    return res

#作用: 计算多个y的凸性Convexity
#Input: c,v,f,n,y1-yn,pv
#Output: C(y1)-C(yn)
def ConvexityCalcwithArrayY(c,v,f,n,y,pv):
    res = [ConvexityCalcwithY(c,v,f,n,y[j-1],pv) for j in xrange(1,n+1)];
    return res

#作用: 绘制D-y图像
#Input: c,v,f,n,y1-yn,pv
def ShowDurationYieldCurve(c,v,f,n,y,pv):
    D_Array = DurationCalcwithArrayY(c,v,f,n,y,pv)
    plt.figure(figsize=(8,4))
    plt.plot(y, D_Array, 'b*')
    plt.plot(y, D_Array, 'b')
    plt.xlabel("Yield")
    plt.ylabel("Duration")
    plt.title('Duration-Yield Curve')
    plt.legend()
    plt.show()

#作用: 绘制C-y图像
#Input: c,v,f,n,y1-yn,pv
def ShowConvexityYieldCurve(c,v,f,n,y,pv):
    C_Array = ConvexityCalcwithArrayY(c,v,f,n,y,pv)
    plt.figure(figsize=(8,4))
    plt.plot(y, C_Array, 'r*')
    plt.plot(y, C_Array, 'r')
    plt.xlabel("Yield")
    plt.ylabel("Convexity")
    plt.title('Convexity-Yield Curve')
    plt.legend()
    plt.show()


if __name__ == '__main__':

    #test for DurationCalcwithY&ConvexityCalcwithY
    y = 0.0666
    D = DurationCalcwithY(0.1, 100, 2, 6, y, 60)
    print "Duration：%f" % D
    C = ConvexityCalcwithY(0.1, 100, 2, 1, y, 60)
    print "Convexity：%f" % C

    #test for DurationCalcwithArrayY&ConvexityCalcwithArrayY
    y = [0.0666, 0.0555, 0.0444, 0.0333, 0.0222, 0.0111]
    D_Array = DurationCalcwithArrayY(0.1, 100, 2, 6, y, 60)
    print "Duration：", D_Array
    C_Array = ConvexityCalcwithArrayY(0.1, 100, 2, 6, y, 60)
    print "Convexity：", C_Array

    #test for ShowDurationYieldCurve
    ShowDurationYieldCurve(0.1, 100, 2, 6, y, 60)

    #test for ShowConvexityYieldCurve
    ShowConvexityYieldCurve(0.1, 100, 2, 6, y, 60)
