import pandas as pd

sales_data = pd.DataFrame({
    'Item': ['A', 'B', 'A', 'C', 'B', 'C'],
    'Units Sold': [10, 20, 15, 30, 25, 18]
})

pivot_table = sales_data.pivot_table(values='Units Sold', index='Item', aggfunc='sum')

print("Pivot Table - Item wise units sold:")
print(pivot_table)
