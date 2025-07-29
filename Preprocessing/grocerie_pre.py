import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load the dataset
df = pd.read_excel(r"C:\Users\varad\Downloads\Data_analytics\Groceries dataset for Market Basket Analysis\original_data\Groceries data.xlsx")

# Group items by (Member_number, Date) to form transactions (baskets)
transactions_series = df.groupby(['Member_number', 'Date'])['itemDescription'].apply(list)
transactions = transactions_series.tolist()

# Encode the transaction data into binary format
te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
basket_df = pd.DataFrame(te_array, columns=te.columns_).astype(int)

# Apply Apriori algorithm with low support to get more frequent itemsets
frequent_itemsets = apriori(basket_df, min_support=0.001, use_colnames=True)

# Generate association rules with low confidence threshold
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)

# Optional: Keep only item-pair rules (1 antecedent → 1 consequent)
rules = rules[(rules['antecedents'].apply(lambda x: len(x)) == 1) &
              (rules['consequents'].apply(lambda x: len(x)) == 1)]

# Sort rules by confidence
rules_sorted = rules.sort_values(by="confidence", ascending=False)

# Export binary transaction data, frequent itemsets, and association rules to Excel
output_path = r"C:\Users\varad\Downloads\Data_analytics\Groceries dataset for Market Basket Analysis\grocery_analysis_output.xlsx"

with pd.ExcelWriter(output_path) as writer:
    basket_df.to_excel(writer, sheet_name="Binary_Transactions", index=False)
    frequent_itemsets.to_excel(writer, sheet_name="Frequent_Itemsets", index=False)
    rules_sorted.to_excel(writer, sheet_name="Association_Rules", index=False)

# Print diagnostics
print("✅ Analysis complete. Output saved as 'grocery_analysis_output.xlsx'")
print(f"Transactions: {len(transactions)}")
print(f"Frequent Itemsets: {len(frequent_itemsets)}")
print(f"Association Rules: {len(rules_sorted)}")
