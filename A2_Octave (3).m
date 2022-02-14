%x=[-5:0.1:5];
%plot (x,normpdf(x,0,1));
pkg load statistics
pkg load symbolic
pkg load optim
x=[-5:0.1:5];
y=stdnormal_pdf (x)
plot (x,y);

f = @(x) normpdf(x,0,1);  
dx = deriv(f, x,1e-7)
dxx= deriv(f, x,1e-7,2,2)
plot (x,dxx,x,dx,x,y);
title ("Normal PDF");
xlabel ("x");
ylabel ("y");
print -dpng "-S400,400" normal.png




% this is just a formula to start with,  
% have fun and change it if you want to.  
