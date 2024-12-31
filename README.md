Personal Data Analysis Project

1. Created two files DataCreation.ipynb and SteamlitConnection.py file

2. Data Creation file is used :-
      -To create csv files for each month about 200 records using faker library  and merging into a single csv.
      -This Merged single csv is moved to MySQL Workbench by establishing MySQL Connection for Performing Analysis over the data.
3.SteamlitConnection.py is used :-
      -To Perform EDA over the data generated and display the result using Steamlit application.
      -It displays the result for 20 SQL queries including 5 Visualization(2 in SQL Queries tab and 3 under Visualization tab)

Queries used:
use personalexpense;
select * from allexpense order by date;
1.select sum(amount) as total from allexpense;
2.SELECT MONTH(Date) AS Month, SUM(Amount) AS Total_Groceries_Amount FROM AllExpense WHERE Category = 'Groceries' GROUP BY MONTH(Date) ORDER BY Month;
3.SELECT SUM(Amount) AS Total_Amount_Transferred_using_Gpay FROM AllExpense WHERE Payment_modes = 'Gpay';
4.SELECT Category, sum(amount) as Total_Amount_in_each_category from AllExpense group by Category order by Total_Amount_in_each_category desc;
5.SELECT  DATE_FORMAT(date, '%Y-%m') AS month_year,SUM(Amount) AS Total_Fees_Amount ,Description FROM AllExpense WHERE Category = 'Fees' Group by month_year,Description order by month_year;
6.SELECT Category, sum(Amount) as Total_Amount_Spent from AllExpense group by Category order by sum(Amount) asc limit 1;
7.SELECT Description, sum(Amount) as Total_Amount_Spent from AllExpense where Description='LIC' group by Description;
8.SELECT Payment_modes,sum(Amount) as Total_Transferred_Amount from AllExpense where Payment_modes='Net Banking'and  date between '2024-03-01' and '2024-03-31' group by Payment_modes;
9.SELECT Payment_modes,sum(Amount) as Total_Transferred_Amount from AllExpense  group by Payment_modes;
10.SELECT MONTH(Date) AS Month,sum(cashback) as Total_Cashback_in_a_month from AllExpense group by Month order by Total_Cashback_in_a_month desc limit 1 ;
11.SELECT MONTH(Date) AS Month,count(Category) as Fuel_Trans_Count  from AllExpense where Category='Fuel' group by Month order by Month;
12.SELECT Payment_modes ,sum(Amount) as Total_Amount_Transferred from AllExpense group by Payment_modes order by Total_Amount_Transferred desc limit 1 ;
13.select Month(Date) as Month,max(Amount) as Maximum_Amonut_Paid from AllExpense where Description='Electricity Bill' group by Month order by Maximum_Amonut_Paid desc limit 1;
14.SELECT e1.Date AS Date1, e1.Category AS Category1, e1.Amount AS Amount1, e2.Date AS Date2, e2.Category AS Category2, e2.Amount AS Amount2 FROM AllExpense e1 INNER JOIN AllExpense e2 ON e1.Amount = e2.Amount AND e1.Category != e2.Category;
15.SELECT Date, Category, Description, Amount FROM AllExpense e1 WHERE Amount = (SELECT MAX(Amount) FROM AllExpense e2 WHERE e2.Category = e1.Category);
16.SELECT Date, Category, Description, Amount FROM AllExpense e1 WHERE Amount = (SELECT MAX(Amount) FROM AllExpense e2 WHERE e2.Category = e1.Category and e2.Description = e1.Description) order by category;
17.SELECT e1.Date, e1.Category, e1.Description, e1.Amount, e1.Cashback, e2.Date AS Matching_Cashback_Date, e2.Category as Matching_Category,e2.Description as Matching_Description,e2.Cashback AS Matching_Cashback_Amount FROM AllExpense e1 Inner JOIN AllExpense e2 ON e1.Category = e2.Category AND e1.Cashback = e2.Cashback AND e1.Date != e2.Date and e1.description=e2.description;
18.SELECT Description, count(Amount) as No_of_Times_Amount_Spent FROM AllExpense where Description='Diesel' Group by description;
19.SELECT Date, Category, Description, Amount FROM AllExpense e1 WHERE Amount > (SELECT AVG(Amount)FROM AllExpense e2 WHERE e2.Category = e1.Category);
20.SELECT Date, Category, Amount FROM AllExpense WHERE Category='Groceries' and  Date BETWEEN '2024-01-01' AND '2024-01-31' order by date;
