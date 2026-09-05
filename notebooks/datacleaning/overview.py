# ============================================
# Q1: Dataset Overview
# - Dataset shape and structure examined
# - Top 5 rows analyzed
# - Data types examined
# ============================================

# Import the common setup (data is already loaded)
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q1: Dataset Overview")
print("="*70)

# Step 1: Check dataset shape
print(f"\n Dataset Shape:")
print(f"   Rows: {df.shape[0]:,}")
print(f"   Columns: {df.shape[1]}")

# Step 2: Display first 5 rows
print("\n Top 5 rows of the dataset:")
print(df.head().to_string())

# Step 3: Display last 5 rows
print("\n Bottom 5 rows of the dataset:")
print(df.tail().to_string())

# Step 4: Check column names
print("\n Column Names:")
print(df.columns.tolist())


print("\n Data Types:")
print(df.dtypes)

# Step 6: Data types summary
print("\n Data Types Summary:")
data_types = df.dtypes.value_counts()
for dtype, count in data_types.items():
    print(f"   {dtype}: {count} columns")

# Step 7: Check unique values in categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
print(f"\n Categorical Columns:")
for col in categorical_cols:
    print(f"   {col}: {df[col].nunique()} unique values")
    if df[col].nunique() <= 10:
        print(f"      Values: {df[col].unique().tolist()}")
    else:
        print(f"      First 5 values: {df[col].unique()[:5].tolist()}")

print("\n" + "="*70)
print(" Q1 Complete!")