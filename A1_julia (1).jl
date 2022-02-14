using StatsBase
using Combinatorics
using Plots
matchExists(n) = 1 - prod([k/365 for k in 365:-1:365-n+1])
function bdEvent(n)
                     birthdays = rand(1:365,n)
                     dayCounts = counts(birthdays, 1:365)
                     return maximum(dayCounts) > 1
                     end
probEst(n) = sum([bdEvent(n) for _ in 1:N])/N
xGrid = 1:365
analyticSolution = [matchExists(n) for n in xGrid]
N = 10^3
mcEstimates = [probEst(n) for n in xGrid]
plot(xGrid, analyticSolution, c=:blue, label="Analytic solution")