pkg load statistics
pkg load symbolic
pkg load optim
pkg load control

n = 20
N = 1000
mu0 = 53.0
powerT=[]
powerU=[]
muRange = 51:0.02:55



for muActual = muRange
dist=normrnd(muActual, 1.2)
rejectT = 0.0
rejectU = 0.0
#rand ("seed", 1)
  for _ = N
    data = normrnd(muActual,1.2,1,20)
    
    rand("seed",1)
    xBar=mean(data)
    stdDev=std(data)
    tStatT = (xBar - mu0)/(stdDev/sqrt(n))
    pValT = 2*tcdf(abs(tStatT),19)
    #pValT = 2*tpdf((abs(tStatT)),19)
    xPositive=sum(data>53)
    uStat = max(xPositive, n-xPositive)

    pValSign = 2*(binopdf(uStat,n,0.5))
    rejectT += (pValT<0.05)
    rejectU += (pValSign<0.05) 
  endfor
a=rejectT
b=rejectU
powerT=[powerT,a]
powerU=[powerU,b]
endfor
plot(muRange,powerT)
plot(muRange,powerU)
print -dpng "-S400,400" normal.png