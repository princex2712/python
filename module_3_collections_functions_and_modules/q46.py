# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
# 300}, o {'item': 'item1', 'amount': 750}]
# Expected Output:
# Counter ({'item1': 1150, 'item2': 300})
list_ = [
    {'item': 'item1', 'amount': 400}, 
    {'item': 'item2', 'amount':300},
    {'item': 'item1', 'amount': 750}
]
result = {}

for dct in list_:
    item = dct['item']
    amount = dct['amount']

    if item in result:
        result[item]+=amount
    else:
        result[item] = amount
print(result)
