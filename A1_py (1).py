import math  
import matplotlib.pyplot as plt 

def birthday_paradox(size): 
    b=1;
    if size > 0:
        x_size = [i+1 for i in range(size)]
        y_prob = []
        
        
        for i in range(size):
            p = (365 - i) / 365;            
            b = b * p;
            c = 1 - b;
            y_prob.append(c)
            print(c);

    plt.figure(figsize=(10,5))
    plt.plot(x_size, y_prob, linewidth=2.5, label='prob(n)', color='blue')
    plt.legend()
    plt.title('Visualization of Birthday problem', fontsize=16);
    plt.xlabel('Peolple', fontsize=12)
    plt.ylabel('prob', fontsize=12)
    
birthday_paradox(365)  
