import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#--------------------------------------

data = [1,2,5,5,7,2,3,4,2,4,1,9]
x_values = np.arange(len(data))
plt.figure(figsize=(13,6))
plt.plot(x_values, data, marker='o', linestyle='-', color='blue', label='Data')

#--------------------------------------
#### Mean
mean_value = np.mean(data)  
plt.axhline(mean_value, color='red', linestyle='dashed', linewidth=.5, label='Mean')
plt.text(x_values[-1] + 1, mean_value, f'Mean : {mean_value:.2f}', color='red', verticalalignment='center')
                 
#--------------------------------------
#### Median
median_value = np.median(data)  
plt.axhline(median_value, color='red', linestyle='dashed', linewidth=.5, label='Median')
plt.text(x_values[-1] + 1, median_value, f'Median : {median_value:.2f}', color='red', verticalalignment='center')
                              
#--------------------------------------
#### Mode
mode_value = stats.mode(data)[0] 
plt.axhline(mode_value, color='red', linestyle='dashed', linewidth=.5, label='Mode')
plt.text(x_values[-1] + 1, mode_value, f'Mode : {mode_value:.2f}', color='red', verticalalignment='center')
                          
#--------------------------------------
#### Variance
variance_value = np.var(data)  
plt.axhline(variance_value, color='red', linestyle='dashed', linewidth=.5, label='Variance')
plt.text(x_values[-1] + 1, variance_value, f'Variance : {variance_value:.2f}', color='red', verticalalignment='center')

#--------------------------------------
#### Standard Deviation
std_deviation_value = np.std(data)
plt.axhline(std_deviation_value, color='red', linestyle='dashed', linewidth=.5, label='Standard Deviation')
plt.text(x_values[-1] + 1, std_deviation_value, f'Standard Deviation : {std_deviation_value:.2f}', color='red', verticalalignment='center')
                 
#--------------------------------------
#### Range
data_range = np.ptp(data)  
plt.axhline(data_range, color='red', linestyle='dashed', linewidth=.5, label='Range')
plt.text(x_values[-1] + 1, data_range, f'Range : {data_range:.2f}', color='red', verticalalignment='center')
          
#--------------------------------------
#### Percentiles
percentiles = np.percentile(data,[10,40,70,90])
plt.axhline(percentiles[0], color='red', linestyle='dashed', linewidth=.5, label='Percentiles[0]')
plt.axhline(percentiles[1], color='purple', linestyle='dashed', linewidth=.5, label='Percentiles[1]')
plt.axhline(percentiles[2], color='blue', linestyle='dashed', linewidth=.5, label='Percentiles[2]')
plt.axhline(percentiles[3], color='green', linestyle='dashed', linewidth=.5, label='Percentiles[3]')
plt.text(x_values[-1] + 1, percentiles[0], f'Percentiles 10th : {percentiles[0]}', color='red', verticalalignment='center')
plt.text(x_values[-1] + 1, percentiles[1], f'Percentiles 40th : {percentiles[0]}', color='purple', verticalalignment='center')
plt.text(x_values[-1] + 1, percentiles[2], f'Percentiles 70th : {percentiles[0]}', color='blue', verticalalignment='center')
plt.text(x_values[-1] + 1, percentiles[3], f'Percentiles 90th : {percentiles[0]}', color='green', verticalalignment='center')
                 
#--------------------------------------
#### Quartils               
quartils = np.percentile(data,[25,50,75])
plt.axhline(quartils[0], color='pink', linestyle='dashed', linewidth=.5, label='Quartils[0]')
plt.axhline(quartils[1], color='orange', linestyle='dashed', linewidth=.5, label='Quartils[1]')
plt.axhline(quartils[2], color='brown', linestyle='dashed', linewidth=.5, label='Quartils[2]')
plt.text(x_values[-1] + 1, quartils[0], f'Quartils 25th : {quartils[0]}', color='pink', verticalalignment='center')
plt.text(x_values[-1] + 1, quartils[1], f'Quartils 50th : {quartils[0]}', color='orange', verticalalignment='center')
plt.text(x_values[-1] + 1, quartils[2], f'Quartils 75th : {quartils[0]}', color='brown', verticalalignment='center')
                        
#--------------------------------------
#### IQR 
q1 = np.percentile(data,25)
q3 = np.percentile(data,75)
iqr = q3 - q1
plt.axhline(iqr, color='pink', linestyle='dashed', linewidth=.5, label='IQR')
plt.text(x_values[-1] + 1, iqr, f'IQR : {iqr}', color='black', verticalalignment='center')        
                 
#--------------------------------------

plt.xticks(x_values)
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Line Plot Of Data')
plt.legend()
plt.tight_layout()
plt.show()