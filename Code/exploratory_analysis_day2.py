#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
#%%
# Load the data
data = pd.read_csv(r'/Users/priya/Documents/Comp_Bio/GitHub/Module-2-Epidemics-SIR-Modeling/Data/mystery_virus_daily_active_counts_RELEASE#1.csv', parse_dates=['date'], header=0, index_col=None)
#%%
# We have day number, date, and active cases. We can use the day number and active cases to fit an exponential growth curve to estimate R0.
# Let's define the exponential growth function
def exponential_growth(t, r):
    return np.exp(r * t)

# Fit the exponential growth model to the data. 
# We'll use a handy function from scipy called CURVE_FIT that allows us to fit any given function to our data. 
# We will fit the exponential growth function to the active cases data. HINT: Look up the documentation for curve_fit to see how to use it.
#define data 
x_values = data['day']
y_values = data['active reported daily cases']
popt, pcov = curve_fit(exponential_growth, x_values, y_values) 

# Approximate R0 using this fit
r = popt[0]
D= 2
R0 = np.exp(r * D)
print(f"Estimated growth rate (r): {r}")
print(f"Estimated R0: {R0}")
# Add the fit as a line on top of your scatterplot.
plt.plot(x_values, exponential_growth(x_values, popt), 'r-', label='Fitted curve')
plt.plot(x_values, y_values, marker='o')
plt.title('Active Cases of Mystery Virus Over Time') 
plt.xlabel('Day') 
plt.ylabel('Number of Active Cases') 
plt.ylim(0, 300)
plt.show() 

'''
r = 0.12144
R0 = 1.274
What viruses have a similar R0? Use the viruses.html file to find a virus or 2 with a similar R0 and give a 1-2 sentence background of the diseases.
Influenza - seasonal with an R0 of 1.3
How accurate do you think your R0 estimate is?
This estimate is pretty accurate given the r value is 0.12144, which is close to 0. 
'''
