import pymysql 
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt


st.title("Analyzing Personal Expenses")

st.image("C:/Users/Micron/Desktop/ExpenseImage.jpg",use_container_width=True)

conn1=pymysql.connect(host="localhost",user="root",password='123456789')
cursor= conn1.cursor()


page = st.sidebar.radio("Choose a section", ["SQL Queries", "Data Visualization"])

if page == "SQL Queries":
    cursor.execute("use personalexpense")

    #Displaying the table
    st.subheader("Expense Data from January 2024 to December 2024 ")
    cursor.execute("select * from allexpense order by date")
    datatable=cursor.fetchall()

    column_names_table = [desc[0] for desc in cursor.description]
    df_table=pd.DataFrame(datatable, columns=column_names_table)
    st.dataframe(df_table,height=300,use_container_width=True)


    ######Query1
    st.subheader("1.Total Expense done in this 12 months ")
    cursor.execute("select sum(amount) as total from allexpense")
    data=cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]
    df=pd.DataFrame(data, columns=column_names)

    if st.button('View Result',key='button1'):
        st.dataframe(df)
    else:
        st.write("Click the button to view Result.")




    ######Query2
    st.subheader("2.Select  total amount spend for Groceries in each month")
    cursor.execute("SELECT MONTH(Date) AS Month, SUM(Amount) AS Total_Groceries_Amount FROM AllExpense WHERE Category = 'Groceries' GROUP BY MONTH(Date) ORDER BY Month")
    data1=cursor.fetchall()

    column_names1 = [desc[0] for desc in cursor.description]
    df1=pd.DataFrame(data1, columns=column_names1)

    # dfbarchart = pd.DataFrame(data1, columns=column_names1)
    # fig1 = px.bar(dfbarchart, x='Month', y='Total_Groceries_Amount', title='Total Amount for Groceries in each Month', labels={'Month': 'Month', 'Groceries_Amount': 'Total_Groceries_Amount'})
    # fig1.update_layout(bargap=0.2)
    if st.button('View Result',key='button2'):
        st.dataframe(df1)
    else:
        st.write("Click the button to view Result.")
    print(column_names1)
    ######Query3
    st.subheader("3.Total amount transferred using Gpay")
    cursor.execute("SELECT SUM(Amount) AS Total_Amount_Transferred_using_Gpay FROM AllExpense WHERE Payment_modes = 'Gpay'")
    data3=cursor.fetchall()

    column_names3 = [desc[0] for desc in cursor.description]

    df3=pd.DataFrame(data3, columns=column_names3)

    if st.button('View Result',key='button3'):
        st.dataframe(df3)
    else:
        st.write("Click the button to view Result.")
    print(column_names3)


    ######Query4
    st.subheader("4.Total amount spent in each category and sort in descending order")
    cursor.execute("SELECT Category, sum(amount) as Total_Amount_in_each_category from AllExpense group by Category order by Total_Amount_in_each_category desc")
    data4=cursor.fetchall()

    column_names4 = [desc[0] for desc in cursor.description]

    df4=pd.DataFrame(data4, columns=column_names4)

    #dfpiechart = pd.DataFrame(data4, columns=column_names4)
    dfpiechart = pd.DataFrame(data4, columns=column_names4)
    fig = px.pie(dfpiechart, names='Category', values='Total_Amount_in_each_category', title='Expense Distribution by Category')
    if st.button('View Result',key='button4'):
        st.dataframe(df4)
        st.plotly_chart(fig)
    else:
        st.write("Click the button to view Result.")
    print(column_names4)


    ######Query5
    st.subheader("5.Total amount Spend as Fees in each Month")
    cursor.execute("SELECT  DATE_FORMAT(date, '%Y-%m') AS month_year,SUM(Amount) AS Total_Fees_Amount ,Description FROM AllExpense WHERE Category = 'Fees' Group by month_year,Description order by month_year")
    data5=cursor.fetchall()

    column_names5 = [desc[0] for desc in cursor.description]

    df5=pd.DataFrame(data5, columns=column_names5)

    if st.button('View Result',key='button5'):
        st.dataframe(df5)
    else:
        st.write("Click the button to view Result.")
    print(column_names5)


    ######Query6
    st.subheader("6.In which Category least amont in spent")
    cursor.execute("SELECT Category, sum(Amount) as Total_Amount_Spent from AllExpense group by Category order by sum(Amount) asc limit 1;")
    data6=cursor.fetchall()

    column_names6 = [desc[0] for desc in cursor.description]

    df6=pd.DataFrame(data6, columns=column_names6)

    if st.button('View Result',key='button6'):
        st.dataframe(df6)
    else:
        st.write("Click the button to view Result.")
    print(column_names6)

    ######Query7
    st.subheader("7.Amount Spend for LIC")
    cursor.execute("SELECT Description, sum(Amount) as Total_Amount_Spent from AllExpense where Description='LIC' group by Description")
    data7=cursor.fetchall()

    column_names7 = [desc[0] for desc in cursor.description]

    df7=pd.DataFrame(data7, columns=column_names7)

    if st.button('View Result',key='button7'):
        st.dataframe(df7)
    else:
        st.write("Click the button to view Result.")
    print(column_names7)


    ######Query8
    st.subheader("8.How much Amount transferred using Net-Banking in the month of March")
    cursor.execute("SELECT Payment_modes,sum(Amount) as Total_Transferred_Amount from AllExpense where Payment_modes='Net Banking'and  date between '2024-03-01' and '2024-03-31' group by Payment_modes")
    data8=cursor.fetchall()

    column_names8 = [desc[0] for desc in cursor.description]

    df8=pd.DataFrame(data8, columns=column_names8)

    if st.button('View Result',key='button8'):
        st.dataframe(df8)
    else:
        st.write("Click the button to view Result.")
    print(column_names8)


    ######Query9
    st.subheader("9.Total Amount transfeered using each Payment mode for all 12 month")
    cursor.execute("SELECT Payment_modes,sum(Amount) as Total_Transferred_Amount from AllExpense  group by Payment_modes")
    data9=cursor.fetchall()

    column_names9 = [desc[0] for desc in cursor.description]

    df9=pd.DataFrame(data9, columns=column_names9)

    if st.button('View Result',key='button9'):
        st.dataframe(df9)
    else:
        st.write("Click the button to view Result.")
    print(column_names9)


    ######Query10
    st.subheader("10.In which month Maximum cashback received and how much?")
    cursor.execute("SELECT MONTH(Date) AS Month,sum(cashback) as Total_Cashback_in_a_month from AllExpense group by Month order by Total_Cashback_in_a_month desc limit 1 ;")
    data10=cursor.fetchall()

    column_names10 = [desc[0] for desc in cursor.description]

    df10=pd.DataFrame(data10, columns=column_names10)

    if st.button('View Result',key='button10'):
        st.dataframe(df10)
    else:
        st.write("Click the button to view Result.")
    print(column_names10)


    ######Query11
    st.subheader("11.How many times the transaction is done for Fuel ineach month")
    cursor.execute("SELECT MONTH(Date) AS Month,count(Category) as Fuel_Trans_Count  from AllExpense where Category='Fuel' group by Month order by Month;")
    data11=cursor.fetchall()

    column_names11 = [desc[0] for desc in cursor.description]

    df11=pd.DataFrame(data11, columns=column_names11)

    fig11, ax11 = plt.subplots()

    # Plot the bar chart
    ax11.bar(df11['Month'], df11['Fuel_Trans_Count'])

    # Add labels to the x and y axes
    ax11.set_xlabel('Month')  # X-axis label
    ax11.set_ylabel('Fuel_Trans_Count')     # Y-axis label
    ax11.set_title('Fuel Tansaction count in each month')  # Title of the chart

    if st.button('View Result',key='button11'):
        st.dataframe(df11,use_container_width=True)
    
    # Display the chart in Streamlit
        st.pyplot(fig11)
    else:
        st.write("Click the button to view Result.")
    print(column_names11)


    ######Query12
    st.subheader("12.In which Payment mode the maximum amount of transaction is done")
    cursor.execute("SELECT Payment_modes ,sum(Amount) as Total_Amount_Transferred from AllExpense group by Payment_modes order by Total_Amount_Transferred desc limit 1 ;")
    data12=cursor.fetchall()

    column_names12 = [desc[0] for desc in cursor.description]

    df12=pd.DataFrame(data12, columns=column_names12)

    if st.button('View Result',key='button12'):
        st.dataframe(df12)
    else:
        st.write("Click the button to view Result.")
    print(column_names12)

    ######Query13
    st.subheader("13.What is the Highest Amount of Electricity Bill paid and in which month")
    cursor.execute("select Month(Date) as Month,max(Amount) as Maximum_Amonut_Paid from AllExpense where Description='Electricity Bill' group by Month order by Maximum_Amonut_Paid desc limit 1;")
    data13=cursor.fetchall()

    column_names13 = [desc[0] for desc in cursor.description]

    df13=pd.DataFrame(data13, columns=column_names13)

    if st.button('View Result',key='button13'):
        st.dataframe(df13)
    else:
        st.write("Click the button to view Result.")
    print(column_names13)

    ######Query14
    st.subheader("14.Retrieve set of expenses have the same amount spent but belong to different categories.")
    cursor.execute("SELECT e1.Date AS Date1, e1.Category AS Category1, e1.Amount AS Amount1, e2.Date AS Date2, e2.Category AS Category2, e2.Amount AS Amount2 FROM AllExpense e1 INNER JOIN AllExpense e2 ON e1.Amount = e2.Amount AND e1.Category != e2.Category;;")
    data14=cursor.fetchall()

    column_names14 = [desc[0] for desc in cursor.description]

    df14=pd.DataFrame(data14, columns=column_names14)

    if st.button('View Result',key='button14'):
        st.dataframe(df14,use_container_width=True)
    else:
        st.write("Click the button to view Result.")
    print(column_names14)


    ######Query15
    st.subheader("15.Retrieve the most expensive amount spent in each category.")
    cursor.execute("SELECT Date, Category, Description, Amount FROM AllExpense e1 WHERE Amount = (SELECT MAX(Amount) FROM AllExpense e2 WHERE e2.Category = e1.Category);")
    data15=cursor.fetchall()

    column_names15 = [desc[0] for desc in cursor.description]

    df15=pd.DataFrame(data15, columns=column_names15)

    if st.button('View Result',key='button15'):
        st.dataframe(df15,use_container_width=True)
    else:
        st.write("Click the button to view Result.")
    print(column_names15)

    ######Query16
    st.subheader("16.Retrieve the most expensive amount spent in each category for each items(description).")
    cursor.execute("SELECT Date, Category, Description, Amount FROM AllExpense e1 WHERE Amount = (SELECT MAX(Amount) FROM AllExpense e2 WHERE e2.Category = e1.Category and e2.Description = e1.Description) order by category;")
    data16=cursor.fetchall()

    column_names16 = [desc[0] for desc in cursor.description]

    df16=pd.DataFrame(data16, columns=column_names16)

    if st.button('View Result',key='button16'):
        st.dataframe(df16,use_container_width=True)
    else:
        st.write("Click the button to view Result.")
    print(column_names16)

    ######Query17
    st.subheader("17.Retrieve the Same Cashback received for same category  and description in different date.")
    cursor.execute("SELECT e1.Date, e1.Category, e1.Description, e1.Amount, e1.Cashback, e2.Date AS Matching_Cashback_Date, e2.Category as Matching_Category,e2.Description as Matching_Description,e2.Cashback AS Matching_Cashback_Amount FROM AllExpense e1 Inner JOIN AllExpense e2 ON e1.Category = e2.Category AND e1.Cashback = e2.Cashback AND e1.Date != e2.Date and e1.description=e2.description;")
    data17=cursor.fetchall()

    column_names17 = [desc[0] for desc in cursor.description]

    df17=pd.DataFrame(data17, columns=column_names17)

    if st.button('View Result',key='button17'):
        st.dataframe(df17,use_container_width=True)
    else:
        st.write("Click the button to view Result.")
    print(column_names17)


    ######Query18
    st.subheader("18.How many times I have spent for diesel this year.")
    cursor.execute("SELECT Description, count(Amount) as No_of_Times_Amount_Spent FROM AllExpense where Description='Diesel' Group by description;")
    data18=cursor.fetchall()

    column_names18 = [desc[0] for desc in cursor.description]

    df18=pd.DataFrame(data18, columns=column_names18)

    if st.button('View Result',key='button18'):
        st.dataframe(df18,use_container_width=True)
    else:
        st.write("Click the button to view Result.")
    print(column_names18)

    ######Query19
    st.subheader("19.Identify the expenses where the amount spend is greater than the average amount in the same category.")
    cursor.execute("SELECT Date, Category, Description, Amount FROM AllExpense e1 WHERE Amount > (SELECT AVG(Amount)FROM AllExpense e2 WHERE e2.Category = e1.Category);")
    data19=cursor.fetchall()

    column_names19 = [desc[0] for desc in cursor.description]

    df19=pd.DataFrame(data19, columns=column_names19)

    if st.button('View Result',key='button19'):
        st.dataframe(df19,use_container_width=True)
    else:
        st.write("Click the button to view Result.")
    print(column_names19)


    ######Query20
    st.subheader("20.Identify the expenses done for Groceries between 01-01-2024 to 31-01-2024.")
    cursor.execute("SELECT Date, Category, Amount FROM AllExpense WHERE Category='Groceries' and  Date BETWEEN '2024-01-01' AND '2024-01-31' order by date;;")
    data20=cursor.fetchall()

    column_names20 = [desc[0] for desc in cursor.description]

    df20=pd.DataFrame(data20, columns=column_names20)

    if st.button('View Result',key='button20'):
        st.dataframe(df20,use_container_width=True)
    else:
        st.write("Click the button to view Result.")
    print(column_names20)

elif page == "Data Visualization":

    #bar chart
    st.subheader("Personal Expense Bar Chart ")
    cursor.execute("use personalexpense")
    st.subheader("Transaction done using Cash in each month")
    cursor.execute("SELECT MONTH(Date) AS Month,count(Payment_modes) as Cash_Trans_Count  from AllExpense where Payment_modes='cash' group by Month order by Month;")
    data21=cursor.fetchall()

    column_names21 = [desc[0] for desc in cursor.description]

    df21=pd.DataFrame(data21, columns=column_names21)

    fig21, ax21 = plt.subplots()

    
    ax21.bar(df21['Month'], df21['Cash_Trans_Count'])

   
    ax21.set_xlabel('Month') 
    ax21.set_ylabel('Cash_Trans_Count')   
    ax21.set_title('Cash Tansaction count in each month')
    st.pyplot(fig21) 


    #scatter chart
    cursor.execute("use personalexpense")
    st.subheader("Transaction done using Debit Card in each month")
    cursor.execute("SELECT MONTH(Date) AS Month,count(Payment_modes) as Debit_Card_Trans_Count  from AllExpense where Payment_modes='Debit Card' group by Month order by Month;")
    data22=cursor.fetchall()

    column_names22 = [desc[0] for desc in cursor.description]

    df22=pd.DataFrame(data22, columns=column_names22)
    fig22, ax22 = plt.subplots()


    ax22.scatter(df22["Month"], df22["Debit_Card_Trans_Count"], color='blue', alpha=0.6, edgecolors='black', marker='o')

 
    ax22.set_title("Transaction done using Debit Card in each month")
    ax22.set_xlabel("Month")
    ax22.set_ylabel("Debit_Card_Trans_Count")


    plt.xticks(rotation=45)


    st.pyplot(fig22)


    # area chart
    cursor.execute("use personalexpense")
    st.subheader("Area chart for Dairy count in each month ")
    cursor.execute("SELECT MONTH(Date) AS Month,count(Description) as Dairy_count from AllExpense where description='Dairy' Group by Month order by Month;")
    data23=cursor.fetchall()

    column_names23 = [desc[0] for desc in cursor.description]

    df23=pd.DataFrame(data23, columns=column_names23)
    fig23, ax23 = plt.subplots()
    df23.plot.area(ax=ax23,color='skyblue')
    ax23.set_title("Dairy count of each month")
    ax23.set_xlabel("Month")
    ax23.set_ylabel("Dairy_count")

    st.pyplot(fig23)
    


    