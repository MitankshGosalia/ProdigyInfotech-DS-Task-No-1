import matplotlib.pyplot as plt
import pandas as pd
import os

# Function to load tyre sales data from a CSV file
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied for file at {file_path}.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Loop until a valid file path is provided
df = None
while df is None:
    file_path = input("Enter the path to your tyre sales CSV file: ").strip()
    if not os.path.isfile(file_path):
        print(f"Error: The path {file_path} is not a valid file. Please try again.")
    else:
        df = load_data(file_path)
        if df is None:
            print("Please provide a valid file path.")

# Define the number of bins for the histograms
sales_bins = int(input("Enter the number of bins for the sales histogram: "))
price_bins = int(input("Enter the number of bins for the price histogram: "))

# Bar chart for seasons
plt.figure(figsize=(8, 6))
plt.bar(df['season'].value_counts().index, df['season'].value_counts().values, color='skyblue')
plt.xlabel('Season')
plt.ylabel('Count')
plt.title('Distribution of Seasons')
plt.tight_layout()
plt.show()

# Histogram for sales
plt.figure(figsize=(8, 6))
plt.hist(df['Sales'], bins=sales_bins, edgecolor='black', color='lightgreen')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.title('Distribution of Sales')
plt.tight_layout()
plt.show()

# Histogram for prices
plt.figure(figsize=(8, 6))
plt.hist(df['Price'], bins=price_bins, edgecolor='black', color='lightcoral')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of Prices')
plt.tight_layout()
plt.show()

# Combined bar chart for Sales and Prices by season
plt.figure(figsize=(10, 8))
bar_width = 0.4
index = range(len(df['season'].value_counts().index))
plt.bar(index, df.groupby('season')['Sales'].sum(), bar_width, label='Sales', color='dodgerblue')
plt.bar([i + bar_width for i in index], df.groupby('season')['Price'].mean(), bar_width, label='Average Price', color='orange')
plt.xlabel('Season')
plt.ylabel('Value')
plt.title('Sales and Average Price by Season')
plt.xticks([i + bar_width / 2 for i in index], df['season'].value_counts().index)
plt.legend()
plt.tight_layout()
plt.show()

# Bar chart for Sales by Company
plt.figure(figsize=(10, 6))
company_sales = df.groupby('Company')['Sales'].sum()
plt.bar(company_sales.index, company_sales.values, color='mediumseagreen')
plt.xlabel('Company')
plt.ylabel('Total Sales')
plt.title('Total Sales by Company')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar chart for Sales by Vehicle Type
plt.figure(figsize=(10, 6))
vehicle_sales = df.groupby('Vehicle Type')['Sales'].sum()
plt.bar(vehicle_sales.index, vehicle_sales.values, color='coral')
plt.xlabel('Vehicle Type')
plt.ylabel('Total Sales')
plt.title('Total Sales by Vehicle Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie chart for the distribution of seasons
plt.figure(figsize=(8, 6))
plt.pie(df['season'].value_counts().values, labels=df['season'].value_counts().index, autopct='%1.1f%%')
plt.title('Distribution of Seasons (Pie Chart)')
plt.tight_layout()
plt.show()
