import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Load dataset
df = pd.read_excel(r"C:\Users\varad\Downloads\Data_analytics\Groceries dataset for Market Basket Analysis\original_data\basket.xlsx")

# Step 2: Clean each row into a transaction list
transactions = df.apply(lambda row: [str(item).strip().lower() for item in row if pd.notnull(item)], axis=1)

# Step 3: Encode transactions into binary format
te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
basket_df = pd.DataFrame(te_array, columns=te.columns_)

# Step 4: Convert booleans to binary (1/0)
basket_df = basket_df.astype(int)

# Step 5: Add Transaction ID
basket_df.insert(0, 'Transaction_ID', range(1, len(basket_df) + 1))

# Step 6: Save preprocessed binary data to Excel
basket_df.to_excel(r"C:\Users\varad\Downloads\Data_analytics\Groceries dataset for Market Basket Analysis\Preprocessed_data\preprocessed_basket_data_binary.xlsx", index=False)

# Step 7: Apply Apriori algorithm (skip 'Transaction_ID' column)
frequent_itemsets = apriori(basket_df.drop(columns=["Transaction_ID"]), min_support=0.02, use_colnames=True)

# Step 8: Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Step 9: Sort rules by confidence
rules_sorted = rules.sort_values(by="confidence", ascending=False)

# Step 10: Export rules to Excel
rules_sorted.to_excel(r"C:\Users\varad\Downloads\Data_analytics\Groceries dataset for Market Basket Analysis\Preprocessed_data\association_rules_output.xlsx", index=False)

print("✅ Preprocessing and rule generation completed successfully!")
