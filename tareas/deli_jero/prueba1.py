import polars as pl
import matplotlib.pyplot as plt

# Step 1: Create a DataFrame with Polars
data = {
    "product": ["A", "B", "C", "A", "B", "C"],
    "category": ["Electronics", "Furniture", "Groceries", "Electronics", "Furniture", "Groceries"],
    "sales": [150, 200, 300, 400, 500, 600],
}

df = pl.DataFrame(data)

# Step 2: Perform some data analysis
# Let's calculate the average sales by category
average_sales = df.groupby("category").agg(pl.col("sales").mean().alias("average_sales"))

# Step 3: Use Matplotlib to create a bar chart
categories = average_sales["category"].to_list()
avg_sales = average_sales["average_sales"].to_list()

plt.figure(figsize=(8, 6))
plt.bar(categories, avg_sales, color='skyblue')
plt.xlabel("Category")
plt.ylabel("Average Sales")
plt.title("Average Sales by Category")
plt.show()
