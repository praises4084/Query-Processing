import pandas as pd

sales_data = pd.DataFrame({
    'Item': ['A', 'B', 'A', 'C', 'B', 'C'],
    'Sales': [100, 200, 150, 300, 250, 180]
})

pivot_table = sales_data.pivot_table(values='Sales', index='Item', aggfunc={'max', 'min'})

print("Pivot Table:")
print(pivot_table)

max_sales = pivot_table['max']
min_sales = pivot_table['min']

print("\nMaximum sale value of items:")
print(max_sales)
print("\nMinimum sale value of items:")
print(min_sales)
