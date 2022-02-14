# Plot the sigmoid function
library(ggplot2)
qplot(-10:10, 1/(1 + exp(-(-10:10))), geom="line", xlab="z", ylab="sigmoid function")

# Download South African heart disease data
sa.heart <- read.table("http://www-stat.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data", sep=",",head=T,row.names=1)

# Pretty plot
#sa.heart2 <- t(sa.heart)
#sa.heart2[sa.heart2$famhist == 0,]$famhist <- "Absent"
#sa.heart2[sa.heart2$famhist == 1,]$famhist <- "Present"
sa.heart <- subset( sa.heart, select = -famhist )

pairs(sa.heart[1:9],pch=21,bg=c("red","green")[factor(sa.heart$chd)])

num.iterations <- 1000

# Download South African heart disease data
sa.heart <- read.table("http://www-stat.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data", sep=",",head=T,row.names=1)

x <- sa.heart$ldl
y <- sa.heart$chd
# plot(x, pch=21, bg=c("red","green")[factor(y)])

# Function to standardize input values
zscore <- function(x, mean.val=NA) {
  if(is.data.frame(x)) return(data.frame(apply(x, 2, zscore, mean.val=mean.val)))
  if(is.na(mean.val)) mean.val <- mean(x)
  standard.deviation <- sd(x)
  (x - mean.val) / standard.deviation 
}

# Standardize the features
x.scaled <- zscore(x)

sigmoid <- function(z){
  (1/(1+exp(-z)))
}

#cost function
cost <- function(theta, x, y){
  m <- length(y) # number of training examples
  h <- sigmoid(x %*% t(theta))
  J <- (t(-y)%*%log(h)-t(1-y)%*%log(1-h))/m
  J
}

# Gradient descent function
grad <- function(x, y, theta) {
  #gradient <- (1 / nrow(y)) * (t(x) %*% (1/(1 + exp(-x %*% t(theta))) - y))
  z <- (x %*% t(theta))
  m <- nrow(y) 
  gradient <- (1 / m) * (t(x) %*%((sigmoid(z)) - y))
  return(t(gradient))
}



gradient.descent <- function(x, y, alpha=0.1, num.iterations=500, threshold=1e-5, output.path=FALSE) {
  m <- NROW(x)
  if(is.vector(x) || (!all(x[,1] == 1))) x <- cbind(rep(1, m), x)
  if(is.vector(y)) y <- matrix(y)
  x <- apply(x, 2, as.numeric)
  num.features <- ncol(x)
  
  # Initialize the parameters
  theta <- matrix(rep(0, num.features), nrow=1)
  
  # Look at the values over each iteration
  theta.path <- theta
  for (i in 1:num.iterations) {
    theta <- theta - alpha * grad(x, y, theta)
    theta.path <- rbind(theta.path, theta)
    if(i > 2) if(all(abs(theta - theta.path[i-1,]) < threshold)) break 
  }
  
  if(output.path) return(theta.path) else return(theta.path[nrow(theta.path),])
}

unscaled.theta <- gradient.descent(x=x, y=y, num.iterations=num.iterations, output.path=TRUE)
scaled.theta <- gradient.descent(x=x.scaled, y=y, num.iterations=num.iterations, output.path=TRUE)

summary(glm(chd ~ age + ldl, family = binomial, data=sa.heart))

qplot(1:(nrow(scaled.theta)), scaled.theta[,1], geom=c("line"), xlab="iteration", ylab="theta_1")
qplot(1:(nrow(scaled.theta)), scaled.theta[,2], geom=c("line"), xlab="iteration", ylab="theta_2")

# Look at output for various different alpha values
vary.alpha <- lapply(c(1e-12, 1e-9, 1e-7, 1e-3, 0.1, 0.9), function(alpha) gradient.descent(x=x.scaled, y=y, alpha=alpha, num.iterations=num.iterations, output.path=TRUE))

par(mfrow = c(2, 3))
for (j in 1:6) {
  plot(vary.alpha[[j]][,2], ylab="area (alpha=1e-9)", xlab="iteration", type="l")
}
#this not going to work simply because sa.heart is not a model 
# Use stepwise logistic regression to reduce the dimensions 
# library(MASS)
# sa.heart.step <- stepAIC(sa.heart)
# summary(sa.heart.step)

# Apply logistic regression to South African heart data from ESL
# build in algorithm just for comparing the results 
sa.heart.fit <- glm(chd ~ sbp + tobacco + ldl + famhist + obesity + alcohol + age , family = binomial, data=sa.heart)
summary(sa.heart.fit)