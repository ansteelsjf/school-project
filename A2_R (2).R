dx = function(x) dnorm(x,0,1)
d1 = function(x) {}
d2 = function(x) {}
body(d1) = D(body(dx), 'x')
body(d2) = D(body(d1), 'x')
plot(dx, -5, 5, ylim = c(-0.5, 0.5), col = 'blue')
plot(d1, -5, 5, add = T, col = 'orange')
plot(d2, -5, 5, add = T, col = 'green')