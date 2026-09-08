# ============================================
# Q7: Univariate Analysis - Categorical Variables
# - Important categorical variables analyzed
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q7: Categorical Variables Analysis")
print("="*70)

# Step 1: Identify categorical columns
categorical_cols = ['Season', 'State', 'Crop', 'Irrigation_Method']

print(" Analyzing Categorical Variables:")
print("="*70)

# Step 2: Analyze each categorical column
for col in categorical_cols:
    print(f"\n {col}:")
    print("-"*40)
    counts = df[col].value_counts()
    
    # Show top values
    if col == 'State':
        print(counts.head(10))
        print(f"\n   Total States: {df[col].nunique()}")
    elif col == 'Crop':
        print(counts.head(10))
        print(f"\n   Total Crops: {df[col].nunique()}")
    else:
        print(counts)
        print(f"\n   Total Categories: {df[col].nunique()}")
    
    # Show percentages
    print(f"\n   Percentage Breakdown:")
    for value, count in counts.head(5).items():
        pct = (count / len(df)) * 100
        print(f"      {value}: {pct:.2f}%")

# Step 3: Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

for idx, col in enumerate(categorical_cols):
    row, col_idx = idx // 2, idx % 2
    counts = df[col].value_counts()
    
    if col == 'State':
        counts.head(10).plot(kind='bar', ax=axes[row, col_idx], color='skyblue', edgecolor='black')
        axes[row, col_idx].set_title(f'Top 10 {col}s', fontsize=12, fontweight='bold')
    elif col == 'Crop':
        counts.head(10).plot(kind='bar', ax=axes[row, col_idx], color='lightgreen', edgecolor='black')
        axes[row, col_idx].set_title(f'Top 10 {col}s', fontsize=12, fontweight='bold')
    else:
        counts.plot(kind='bar', ax=axes[row, col_idx], color='coral', edgecolor='black')
        axes[row, col_idx].set_title(f'Distribution of {col}', fontsize=12, fontweight='bold')
    
    axes[row, col_idx].set_xlabel(col, fontsize=11)
    axes[row, col_idx].set_ylabel('Count', fontsize=11)
    axes[row, col_idx].tick_params(axis='x', rotation=45)

plt.tight_layout()
save_chart('q7_categorical_variables.png')
plt.show()

print("\n" + "="*70)
print(" Q7 Complete!")