# importing modules
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import datetime
import os # added this to handle the csv files
import glob # added this to handle the csv files
import matplotlib
import seaborn as sns

#----------------------------------------- Using glob to read all csv files ----------------------------------- 
# Read the file name
print ("Give me the folder path (files in it must be CSV format) ")
path = '500 kV project/500 kV project tests antenna grounded/40 psi on top_pressure increasing'

#path = os.getcwd() This line was now asigned by reading the input
csv_files = glob.glob(os.path.join(path, "*.csv"))

# loop over the list of csv files
for f in csv_files:   
    # read the csv file
    df = pd.read_csv(f)
    # dropping the NaN rows 
    df.dropna()
    #display(df)
    
    # dropping passed columns 
    df.drop(["time", "Unix time"], axis = 1, inplace = True) 
    
    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])

    # Calculate the mean and standard deviation of the y data
    means = df.groupby('IGLGL01Preset_Volt').mean()
    y_std_1 = df.groupby('IGLGL01Preset_Volt').sem()
    y_std = y_std_1['IGLGL01HVIREAD']
            
    #print('MEANS and STD content:')
    #display(means)
    #display(y_std)
    
    #plot raw data
    #plt.plot(df['IGLGL01Preset_Volt'], df['IGLGL01HVIREAD'],"ob")
    
    # Rested index to plot the first col
    means = means.reset_index()
    means.dropna(inplace=True)
    
    #print('after reset index')
    #display(means)
    #plt.subplot(means['IGLGL01Preset_Volt'], means['IGLGL01HVIREAD'], marker='o') #, linestyle='none', label=f)
    
    # Clip the label
    #label_short = [f - 'C:\Users\gabrielp\Documents\500 kV project\Python\500 kV project\')
    
    #Plot the data with error bars
    #Define the size of the plot
    plt.rcParams["figure.figsize"] = [30, 20]
    plt.rcParams.update({'font.size': 25})
    plt.grid(True, alpha = 0.8) #Grid
    plt.errorbar(means['IGLGL01Preset_Volt'], means['IGLGL01HVIREAD'], yerr=y_std, fmt='o', ms = 15, label = f.split("\\")[-1], capsize = 4.0, linestyle = 'none')
    #Using seaborn to fit the data
    sns.regplot(means['IGLGL01Preset_Volt'], means['IGLGL01HVIREAD'], label = f.split("\\")[-1])
    plt.legend()
    plt.xlabel("Voltage [kV]") 
    plt.ylabel("IP current [mA]")
    plt.title('Folder name: ' + path) 
    plt.savefig(path.split("\\")[-1] + '_Fit.png') #save plot to png file

plt.show()

print('Done! ¯\_(ツ)_/¯')
#-----------------------------------------Data displays for troubleshooting------------------------------
# displays data for troubleshoot
#print('voltage data', voltage)
#print('decarad data', decarad)