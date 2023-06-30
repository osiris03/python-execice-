"""Format variables using a string.format() method.
Write a program to use string.format() method to format the following three variables as per the expected output"""

totalMoney = 1000
quantity = 3
price = 450
statement = "I have {1} dollars so i can buy {0} football for {2:.2f} dollars"
print(statement.format(quantity,totalMoney, price))