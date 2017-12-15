# -*- coding: utf-8 -*-
# 时间输入程序 不考虑闰年的情况 每年都是365天计算

from newton import gznewton

mm = (0,31,28,31,30,31,30,31,31,30,31,30,31)

def time_input(m, c, timeStart, timeEnd, timeCurrent, p0, frequency):
    yearStart = int(timeStart[0:4])
    yearEnd = int(timeEnd[0:4])
    yearCurrent = int(timeCurrent[0:4])
    mouthSE = int(timeStart[5:7])
    daySE = int(timeStart[8:10])
    mouthCurrent = int(timeCurrent[5:7])
    dayCurrent = int(timeCurrent[8:10])
    #计算债券的总年份
    year = yearEnd-yearStart 
    #计算剩余年份
    if(mouthSE > mouthCurrent):
        year_rest = yearEnd - yearCurrent + 1
    elif(mouthSE < mouthCurrent):
        year_rest = yearEnd - yearCurrent
    elif(daySE > dayCurrent): #月份相等时比较天数
        year_rest = yearEnd - yearCurrent + 1 
    else:
        year_rest = yearEnd - yearCurrent
    #计算出售日到下次整年付息日的天数
    if(mouthSE > mouthCurrent):
        day = mm[mouthSE]- dayCurrent
        day += daySE
        i = mouthCurrent + 1
        while(i!= mouthSE):
            day += mm[i]
            i += 1 
    elif(mouthSE < mouthCurrent):
        day = mm[mouthCurrent]- daySE
        day += dayCurrent
        i = mouthSE + 1
        while(i!= mouthCurrent):
            day += mm[i]
            i += 1
        day = 365 - day
    elif(daySE > dayCurrent): #月份相等时比较天数
        day = daySE - dayCurrent
    else:
        day = 365 + daySE - dayCurrent
    #计算还有几次付息
    num_interest = year_rest*frequency + (day*frequency)/365
    #计算距离下次付息日的天数/两次付息间隔
    t = float(day*frequency)/float(365) - (day*frequency)/365
    return p0,m,c,num_interest,t

if __name__ == '__main__':
    m = input("请输入债券本金:\n")
    c = input("请输入债券每次利息:\n")
    timeStart = raw_input("请输入债券发行日期(格式：XXXX\XX\XX):\n")
    timeEnd = raw_input("请输入债券结算日期(格式：XXXX\XX\XX):\n")
    timeCurrent = raw_input("请输入债券出售日期(格式：XXXX\XX\XX):\n")
    p0 = input("请输入债券出售价格:\n")
    frequency = input("请输入债券付息频率:\n") #n可取1,2,3,4,6,12
    p0,m,c,n,t = time_input(m, c, timeStart, timeEnd, timeCurrent, p0, frequency)
    x=gznewton(p0,c,m,n,t,1.1,0.00001)-1
    print "yield：%f" % x
