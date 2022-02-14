 b=1;
 y_prob = []
 y = []
 x = 1:365
for i = 1:365
  p = (365 - i) / 365;  
  b = b * p;
  c = 1 - b;
  y = [y;c]
  fprintf('value of c: %f\n', c);
  end
plot(x, y)