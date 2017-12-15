# -*- coding: utf-8 -*-

# Author: Hongyang Liu
# Time: 2017/11/05
# 
#Input are c,v,f,n,y
#Output is pv
#
# c is coupon rate
# v is face value
# f is payment frequency
# n is the time from now to the due day of the coupon
# index is the index of the 2D array
# i is the array of the time from now to every interest are distributed
# y is the array of the corresponding yield when time is i
# 
# pv is the presnt value


def CleanPriceCalc(c,v,f,n,y):
    AccuInterest = 0

    len_y = len(y)

    for j in xrange(0,len_y-1):
        AccuInterest =++ 1/(1 + y[j]/f)**(j+1)

    pv = c*v*AccuInterest/f + v/(1+y[len_y-1]/f)**(len_y+1)

    return pv



if __name__ == '__main__':
    x=CleanPriceCalc(0.1,100,2,6,[0.0666,0.0555,0.0444,0.0333,0.0222,0.0111])
    print "Present Value is %f" % x

