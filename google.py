
#IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#READ CSV FILE 
google_playstore_df = pd.read_csv('googleplaystore.csv')

def print_data():
    print(google_playstore_df)
    
# DATA CLEANING
google_playstore_df['Reviews'] = pd.to_numeric(google_playstore_df.Reviews,errors='coerce').fillna(0).astype(np.int64)

# Converting the Ratings column to Numeric int64, non numeric characters to 0.
google_playstore_df['Rating'] = pd.to_numeric(google_playstore_df.Rating,errors='coerce').fillna(0).astype(np.float64)

# removing +, , characters from Installs column and Converting to Numeric int64, non numeric characters to 0.
google_playstore_df['Installs'] = google_playstore_df['Installs'].str.replace('+','',regex=True)
google_playstore_df['Installs'] = google_playstore_df['Installs'].str.replace(',','',regex=True)
google_playstore_df['Installs'] = pd.to_numeric(google_playstore_df.Installs,errors='coerce').fillna(0).astype(np.int64)

# removing Dollar character from Price column and Converting to Numeric int64, non numeric characters to 0.
google_playstore_df['Price'] = google_playstore_df['Price'].str.replace('$','',regex=True)

#Replacing M with 000000 and k with 000 characters in Size column and Converting to Numeric int64, non numeric characters to 0
google_playstore_df['Size'] = google_playstore_df['Size'].str.replace('M','000000',regex=True)
google_playstore_df['Size'] = google_playstore_df['Size'].str.replace('k','000',regex=True)
google_playstore_df['Size'] = pd.to_numeric(google_playstore_df.Size,errors='coerce').fillna(0).astype(np.int64)

# EXPLORATORY DATA ANALYSIS AND VISUALIZATION

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (12, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

def top_10_apps():
    try:
        category_series = google_playstore_df['Category'].value_counts().head(10)
        plt.figure(figsize=(12,5))
        plt.title("Apps Category Wise")
        plt.ylabel('No.of Apps')
        plt.xlabel('Category')
        plt.xticks(rotation=60,fontsize=10)
        google_playstore_df['Category'].value_counts().head(10).plot(kind='bar')
        plt.show()
    
    except Exception as e:
            print("An error occurred while plotting :", e)  
    
def paid_and_free_apps():
    try:    
        free_or_paid_df=google_playstore_df.groupby('Type')[['App']].count()
        free_or_paid_df.plot.pie(subplots=True, figsize=(12, 6), wedgeprops={"edgecolor":"0",'linewidth': 2,
                    'linestyle': 'dashed', 'antialiased': True}, autopct='%1.0f%%')
        plt.title('Distribution of Apps based on Paid/Free',fontweight=600)
        plt.show()
        
    except Exception as e:
            print("An error occurred while plotting :", e)
    
def no_of_apps_each_version():
    try:
        plt.title('Distruibution according to the "Android Version" of the App',fontweight=600)
        plt.ylabel('Android Version')
        plt.xlabel('No. of Apps')
        google_playstore_df['Android Ver'].value_counts().head(10).plot(kind='barh')
        plt.show()
    
    except Exception as e:
            print("An error occurred while plotting :", e)
    
def heatmap():
    try:
        plt.title("No. of Apps rated in each Age Group")
        sns.heatmap(google_playstore_df.groupby('Content Rating')[['App']].count(),fmt="d", annot=True, cmap='Reds')
        plt.show()
    
    except Exception as e:
        print("An error occurred while plotting :", e)
    
def apps_in_each_category():
    try:
        plt.figure(figsize=(15,5))
        bar_plot_df = sns.barplot(x=google_playstore_df['Category'], y=google_playstore_df.Installs, data=google_playstore_df)
        bar_plot_df.set_xticklabels(bar_plot_df.get_xticklabels(), rotation=90, ha="right")
        plt.title('Category Wise Installs',fontsize=25)
        plt.show()  
        
    except Exception as e:
            print("An error occurred while plotting :", e)
    
def choose_function():
    print("Select a function to call:")
    print("1. Print Dataset ")
    print("2. Plot Top 10 apps")
    print("3. Plot Paid and Free apps ")
    print("4. Plot No of apps each version")
    print("5. Plot Heatmap")
    print("6. Plot Apps in each category")
    choice = int(input("Enter your choice (1-6): "))
    return choice

# Example usage:

while True:
    choice = choose_function()
    if choice == 1:
        print_data()
    elif choice == 2:
        top_10_apps()
    elif choice == 3:
        paid_and_free_apps()
    elif choice == 4:
        no_of_apps_each_version()
    elif choice == 5:
        heatmap()
    elif choice == 6:
        apps_in_each_category()
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
    cont = input("Do you want to continue (y/n)? ")
    if cont.lower() != 'y':
        break
    
        

 