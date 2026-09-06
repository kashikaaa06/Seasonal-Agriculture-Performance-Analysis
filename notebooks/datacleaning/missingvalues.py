# Q2 missing values 
# missing values are a common issue identified and handled

exec(open('setup.py').read())
print("\n" + "="*70)
print("Q2: Missing Values")
print("="*70)

print("\n Missing Values Before Handling:")
missing_values = df.isnull().sum()
missing_cols = missing_values[missing_values > 0]

if len(missing_cols) == 0:
    print(" No missing values found in dataset")
else:
    print(missing_cols)
    print("\n Total missing values: {missing_values.sum()}") 
    print("\n Handling missing values")

for col in missing_values.index:
     if df[col].dtype in ['float64','int64']:
         median_val = df[col].median()
         df[col].fillna(median_val , inplace=True)
         print(f"Filled missing values in {col} with median: {median_val:.2f}")
     else:
         mode_val = df[col].mode()[0]
         df[col].fillna(mode_val, inplace=True)
         print(f" Filled missing values in '{col}' with mode: '{mode_val}'")

     missing_after = df.isnull().sum().sum()
     print(f"\n Missing Values After Handling: {missing_after}")

print("\n" + "="*70)
print("Q2 Complete!")