import csv
import pandas

df = pandas.read_csv('mempool.csv')
print(df)

#max value of weight with pandas

max_value_column = df["weight"].max()
print(max_value_column)

#just checking with csv of weight 

with open('mempool.csv') as f:
    reader = csv.reader(f)
    next(reader)    
    answer = max(int(column[2].replace(',', '')) for column in reader)
print(answer)

#max value of weight is 295164

#sorting dataframe in ascending order with weight 
sorted_df_weight = df. sort_values(by=["weight"], ascending=True)

#sorting dataframe in descending order with fee
sorted_df_fee = df. sort_values(by=["fee"], ascending=False)


temp_sum_weight = 0
#list_of_all_weights indexes whose sum is less then max weight when sorted in ascending order to get max number of weights
list_of_all_weights = []
for i in range(len(sorted_df_weight["weight"])):
    temp_sum_weight+=sorted_df_weight["weight"][i]
    
    if temp_sum_weight <=295164:
        list_of_all_weights.append(i)
    if temp_sum_weight > 295164:
        break
print(list_of_all_weights)

#fee if we take coloumn sorted in asscending order of weight
fee_with_weight = []
for i in lis:
    fee_with_weight.append(sorted_df_weight["fee"][i])
print(sum(fee_with_weight))

#value of tx_id for maximizing fee for all weights less then max value of weights
list_tx_id = []
#fee when we sort columns in descending order of fee
fee_with_fee = []
temp = 0
for i in range(len(sorted_df_fee["fee"])):
    temp+=sorted_df_fee["weight"][i]
    if temp<=295164:
        list_tx_id.append(sorted_df_fee["tx_id"][i])
        fee_with_fee.append(sorted_df_fee["fee"][i])
    if temp> 295164:
        break

#this will return all required values of tx_id to maximize fee
print("\n".join(list_tx_id))
