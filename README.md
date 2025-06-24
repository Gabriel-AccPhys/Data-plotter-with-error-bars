# Data-plotter-with-error-bars
Data plotter with error bars
This script processes and visualizes multiple CSV datasets from a
user-specified directory to analyze the current response of a high-
voltage conditioning system. For each file, it reads the data using
pandas, removes unused time-related columns and NaN entries,
and computes the mean and standard error of the monitored cur-
rent (IGLGL01HVIREAD) grouped by preset voltage (IGLGL01Pre-
set_Volt). The script then generates a combined figure using mat-
plotlib and seaborn, where it plots error bars for each dataset along-
side a linear regression fit. Each dataset is labeled by its file name,
and the final plot is saved as a PNG file using the folder name as the
base. The script supports batch processing and visual correlation of
current vs. voltage trends across multiple experimental runs.
