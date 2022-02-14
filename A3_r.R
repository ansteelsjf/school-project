

muRange  <- seq(51, 55, by = 0.02)
n = 20
N = 10000
mu0 = 53.0
powerT <- list()
powerU <- list()
for (muActual in muRange){
  dist = rnorm(20,muActual,1.2)
  rejectT=0
  rejectU=0
  set.seed(1)
  for (q in 1:N){
    data = rnorm(20,muActual,1.2)
    xBar=mean(data)
    stdDev=sd(data)
    
    tStatT = (xBar - mu0)/(stdDev/sqrt(n))
    pValT = 2*(1 - pt(abs(tStatT), df = 19))
    xPositive =sum(data>53)
    uStat = max(xPositive, n-xPositive)
    pValSign = 2*(1-pbinom(uStat,n,0.5))
    rejectT = rejectT+(pValT < 0.05)
    rejectU = rejectU+(pValSign < 0.05)
  }
 
  powerT <- append(powerT, rejectT/N)
  powerU <- append(powerU, rejectU/N)
}
plot(muRange, powerT, type = "b", frame = FALSE, pch = 19, 
     col = "blue", xlab = "x", ylab = "y")
# Add a second line
lines(muRange, powerU, pch = 18, col = "red", type = "b", lty = 2)
# Add a legend to the plot
legend("topleft", legend=c("t test", "sign test"),
       col=c("blue", "red"), lty = 1:2, cex=0.8)



