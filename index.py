import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Order_ID": np.arange(1001, 1021),
    "Product": ["Laptop", "Headphones", "Smartphone", "Tablet", "Camera"] * 4,
    "Category": ["Electronics"] * 20,
    "Quantity": np.random.randint(1, 5, 20),
    "Unit_Price": np.random.randint(100, 1500, 20),
    "Discount": np.random.uniform(0.05, 0.3, 20),
    "Order_Date": pd.date_range(start="2024-01-01", periods=20, freq="D"),
    "Region": ["North", "East", "West", "South"] * 5
}
sales_df = pd.DataFrame(data)
sales_df["Total_Sales"] = sales_df["Quantity"] * sales_df["Unit_Price"] * (1 - sales_df["Discount"])
print("First 5 rows of the dataset:")
print(sales_df.head())
print("\nBasic Info:")
print(sales_df.info())
print("\nSummary Statistics:")
print(sales_df.describe())
print("\nTotal Sales by Region:")
print(sales_df.groupby("Region")["Total_Sales"].sum())
sales_by_product = sales_df.groupby("Product")["Total_Sales"].sum().reset_index()
sales_by_region = sales_df.groupby("Region")["Total_Sales"].sum().reset_index()
daily_sales = sales_df.groupby("Order_Date")["Total_Sales"].sum().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(x="Product", y="Total_Sales", data=sales_by_product, palette="viridis")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales (USD)")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(8, 5))
sns.barplot(x="Region", y="Total_Sales", data=sales_by_region, palette="coolwarm")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales (USD)")
plt.show()
plt.figure(figsize=(10, 5))
sns.lineplot(x="Order_Date", y="Total_Sales", data=daily_sales, marker="o", color="green")
plt.title("Daily Sales Trend")
plt.xlabel("Order Date")
plt.ylabel("Total Sales (USD)")
plt.grid()
plt.show()
print("\nKey Insights:")
print(f"Total Revenue: ${sales_df['Total_Sales'].sum():.2f}")
print("Top 3 Products by Sales:")
print(sales_by_product.sort_values(by='Total_Sales', ascending=False).head(3))

print("\nSales Performance by Region:")
print(sales_by_region.sort_values(by='Total_Sales', ascending=False))
