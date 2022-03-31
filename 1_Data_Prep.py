import pandas as pd


"""
Load data
"""
path = "folder path/raw_data_1.xlsx"
data_1 = pd.read_excel(path)
# print(data_1.head())

"""
Create a list to hold all the data in data_1
"""
list_1 = []

"""
define a function to put all data currently in
data_1 into list_1
"""
def compose_list():
    for gram in data_1.a:
        list_1.append(gram)
    for gram in data_1.b:
        list_1.append(gram)
    for gram in data_1.c:
        list_1.append(gram)
    for gram in data_1.d:
        list_1.append(gram)
    for gram in data_1.e:
        list_1.append(gram)


compose_list()
# print(list_1)
# print(len(list_1))  # 3900

"""
remove all nan values
"""
list_2 = [item for item in list_1 if not(pd.isnull(item)) == True]
# print(list_2)
# print(len(list_2))  # 3870

"""
remove all string values from list_2
"""
list_3 = [item for item in list_2 if str != type(item)]
# print(list_3)
# print(len(list_3))  # 3707

"""
Convert all 'float' to 'int'
"""
list_4 = [int(x) for x in list_3]
# print(list_4)
# print(len(list_4))  # 3707

"""
put a decimal point between first and 
second digits of each number
"""
list_5 = [x/10000 for x in list_4]
# print(list_5)
# print(len(list_5))  # 3707

"""
create an empty dataframe and 
place list_5 in it
"""
processed_data = pd.DataFrame()

processed_data['gram_weight'] = pd.Series(
    x for x in list_5)

"""
create another column in processed_data
and number all values in the 'gram_weight' 
column
"""
processed_data['seed_number'] = pd.Series(
    x for x in range(len(processed_data.index)))

"""
see the processed data
"""
# print(processed_data.head())

"""
save data
"""
processed_data.to_excel('processed_data.xlsx', index=False)
