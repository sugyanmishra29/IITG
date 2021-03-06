# Q.1 Run your program for M = 1, 5, 10, 20, 50, 100, 200, 400 
# to get the initial option prices and tabulate them

# Pandas : pip install pandas 
# Matplotlib: pip install matplotlib 
# Numpy: pip install numpy 
# Ipython: pip install ipython


import math
import pandas as pd
from IPython.display import display

# Function to get Option Price for a given M
def getOptionPrice(M, u, d, p):
    callList = [0]*(M+1)
    putList = [0]*(M+1)
    
    for i in range(M+1):
        callList[i] = max(S0*(u**i)*(d**(M-i)) - K, 0)
        putList[i] = max(0, K - S0*(u**i)*(d**(M-i)))
        
    for i in range(M):
        for j in range(M-i):
            callList[j] = ((1-p)*callList[j] + p*callList[j+1])*math.exp(-r*T/M)
            putList[j] = ((1-p)*putList[j] + p*putList[j+1])*math.exp(-r*T/M)
    return callList[0], putList[0]

# Given data
S0=100
K=105
T=5
r=0.05
sig=0.3
MList=[1, 5, 10, 20, 50, 100, 200, 400]

# Lists to store the option prices
callPrices = []
putPrices = []


for M in MList:
    dt = T/M
    u = math.exp(sig*math.sqrt(dt)+(r-sig*sig/2)*dt)
    d = math.exp(-sig*math.sqrt(dt)+(r-sig*sig/2)*dt)
    p = (math.exp(r*dt)-d)/(u-d)
    
    # Check if No Arbitrage Principle has got violated
    if p < 0 or p > 1:
        print("No Arbitrage Principle has been Violated")
        CallPrices.append('-')
        PutPrices.append('-')
        continue
    
    call, put = getOptionPrice(M, u, d, p)
    callPrices.append(call)
    putPrices.append(put)

# Display the data using Pandas Dataframe
df = pd.DataFrame({'Step Size':MList,'Call Option Price': callPrices, 'Put Option Price': putPrices},)
display(df)
