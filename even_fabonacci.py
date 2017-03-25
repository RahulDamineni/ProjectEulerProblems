# coding=utf-8
a,b = 1,1
print(a,b,end=',')
for i in range(1000):
    a,b = b,a+b
    # c = round(1*1.67**(i+1))
    print(b, end=' ')



