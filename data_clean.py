import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel(r"D:\project\dataset_project\superstore.xls")


#Describe info about dataset
print(df.shape)
print(df.info())
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())



#Renaming the column name
df.rename(columns={'Row ID':'row_id','Order ID':'order_id','Order Date':'order_date','Ship Date':'ship_date','Ship Mode':'ship_mode',
'Customer ID':'customer_id','Customer Name':'customer_name','Segment':'segment','Postal Code':'postal_code','Product ID':'product_id',
'Sub-Category':'sub_category','Product Name':'product_name'},inplace=True)

print(df.rename)

print(df['customer_id'].unique())


print(df.isnull().sum())


min_sales=min(df['Sales'])
print(f"The minimum sales :{min_sales}")

max_sales=min(df['Sales'])
print(f"The minimum sales :{max_sales}")


print(df['Sales'].describe())

print(df['Profit'].describe())

print(df.fillna(0, inplace=True))


Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Sales"] < lower) | (df["Sales"] > upper)]

print(outliers.shape)


plt.boxplot(df["Sales"])
plt.title("Sales Outliers")
plt.show()


# Convert Date Column
df['order_date']=pd.to_datetime(df['order_date'])
print(df['order_date'])

# # #EDA Analysis 
print("The total sales:",df['Sales'].sum())
print("The total profit:",df['Profit'].sum())
print("The avg profit:",df['Profit'].mean())


# #TOP PRODCUTS
top_products=df.groupby('product_name')['Sales'].sum() \
.sort_values(ascending=True) \
    .head(10)

print(top_products)


profit_products=df.groupby('product_name')['Profit'].sum()\
.sort_values(ascending=True) \
    .head(10)
print(profit_products)


# sale by region

sale_region=df.groupby('Region')['Sales'].sum()
print(f"Region wise sales: {sale_region}")


#Category wise sales

category_sale=df.groupby('Category')['Sales'].sum()
print(f"Category wise sales: {category_sale}")


#Month wise Sales
df['Month']=df['order_date'].dt.to_period('M')
Monthly_sales=df.groupby('Month')['Sales'].sum()
print(f"Monthly sales: {Monthly_sales}")


Monthly_sales.index = Monthly_sales.index.to_timestamp()

plt.figure(figsize=(10,5))
plt.plot(Monthly_sales.index,Monthly_sales.values)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()



# Category-wise Profit
category_profit = df.groupby("Category")["Profit"].sum()

print(category_profit)

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(category_profit.index, category_profit.values)

plt.title("Category-wise Profit")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.show()


# Save cleaned dataset
df.to_csv("Superstore_Cleaned.csv", index=False)

print("Cleaned dataset saved!")


print(len(df))

import pandas as pd

df = pd.read_csv("Superstore_Cleaned.csv")

print("Rows:", len(df))
print("Duplicates:", df.duplicated().sum())