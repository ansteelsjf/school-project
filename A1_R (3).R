n <- seq(5, 365, by = 1)
probs <- sapply(n , 
                function(t) {
                  obs <- seq(365, by = -1, length.out = t) / 365
                  prob <- 1 - prod(obs)
                  
                }
)
plot(n, probs, col = "red4")
