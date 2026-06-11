create database sales
use sales

select * from Superstore_Cleaned

-- total sale by region
select region,sum(Sales) from Superstore_Cleaned
group by region order by sum(Sales) asc

-- Top Selling products

select `Product Name`,sum(Sales) as total_sale 
from Superstore_Cleaned group by `Product Name` order by total_sale 
limit 15


-- Monthly Sales Trend
select month(STR_TO_DATE(`Order Date`, '%Y-%m-%d')) as month_num,
sum(Sales) as total
from Superstore_Cleaned
group by month_num
order by total desc


 -- Most Profitable Category
select Category,sum(Profit) as Total_Profit
from Superstore_Cleaned
group by Category
order by Total_Profit 


-- Sales by Customer Segment
select `Customer ID`,
       count(`Order ID`) AS Orders_Count
from Superstore_Cleaned
Group by `Customer ID`
having Orders_Count > 3

-- Profit by Shipping Mode
select`Ship Mode`,
       sum(Profit) AS Total_Profit
from Superstore_Cleaned
group by `Ship Mode`
order by Total_Profit desc


-- Loss-Making Products
select`Product Name`,
       sum(Profit) AS Total_Profit
from Superstore_Cleaned
group by `Product Name`
having SUM(Profit) < 0
order by Total_Profit;

-- Yearly Sales Growth
select year(`Order Date`) as year,
       sum(Sales) as Total_Sales
from Superstore_Cleaned
group by year(`Order Date`)
order by year

-- Profit vs Discount Impact
select Discount, SUM(Profit) as Total_Profit
from Superstore_Cleaned
group by Discount
order by Discount

-- Discount Impact on Profitability
select case 
           when Discount = 0 then 'No Discount'
           when Discount between 0.01 and 0.20 then 'Low Discount'
           when Discount between 0.21 and 0.50 then 'Medium Discount'
           else 'High Discount'
       end as Discount_Band,
       sum(Sales) as Total_Sales,
       sum(Profit) as Total_Profit
from Superstore_Cleaned
group by Discount_Band
order by Total_Profit desc;

