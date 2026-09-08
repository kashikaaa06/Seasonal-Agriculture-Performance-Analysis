# ============================================
# Q8: Univariate Analysis - Numerical Variables
# - Important numerical variables analyzed
# - Production/performance distributions
# - Economic distributions
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q8: Numerical Variables Analysis")
print("="*70)

# Step 1: Identify key numerical columns
numerical_cols = ['Yield_Tonnes_Ha', 'Profit_INR', 'Revenue_INR', 
                  'Production_Tonnes', 'Water_Used_m3']

print(" Analyzing Numerical Variables:")
print("="*70)

# Step 2: Summary statistics for each numerical column
for col in numerical_cols:
    print(f"\n {col}:")
    print("-"*40)
    print(f"   Mean: {df[col].mean():.2f}")
    print(f"   Median: {df[col].median():.2f}")
    print(f"   Min: {df[col].min():.2f}")
    print(f"   Max: {df[col].max():.2f}")
    print(f"   Std Dev: {df[col].std():.2f}")
    
    # Skewness (positive = right-skewed, negative = left-skewed)
    skewness = df[col].skew()
    if skewness > 1:
        print(f"   Skewness: {skewness:.2f} (Highly Right-Skewed)")
    elif skewness > 0.5:
        print(f"   Skewness: {skewness:.2f} (Moderately Right-Skewed)")
    elif skewness < -1:
        print(f"   Skewness: {skewness:.2f} (Highly Left-Skewed)")
    elif skewness < -0.5:
        print(f"   Skewness: {skewness:.2f} (Moderately Left-Skewed)")
    else:
        print(f"   Skewness: {skewness:.2f} (Approximately Symmetric)")

# Step 3: Create histograms and boxplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

for idx, col in enumerate(numerical_cols):
    row, col_idx = idx // 3, idx % 3
    
    # Histogram
    df[col].hist(bins=30, ax=axes[row, col_idx], color='lightblue', edgecolor='black')
    axes[row, col_idx].set_title(f'Distribution of {col}', fontsize=11, fontweight='bold')
    axes[row, col_idx].set_xlabel(col, fontsize=10)
    axes[row, col_idx].set_ylabel('Frequency', fontsize=10)

# Remove empty subplot
if len(numerical_cols) < 6:
    fig.delaxes(axes[1, 2])

plt.tight_layout()
save_chart('q8_numerical_distributions.png')
plt.show()

# Step 4: Additional boxplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

for idx, col in enumerate(numerical_cols):
    row, col_idx = idx // 3, idx % 3
    df.boxplot(column=col, ax=axes[row, col_idx])
    axes[row, col_idx].set_title(f'Boxplot of {col}', fontsize=11, fontweight='bold')

if len(numerical_cols) < 6:
    fig.delaxes(axes[1, 2])

plt.tight_layout()
save_chart('q8_numerical_boxplots.png')
plt.show()

print("\n" + "="*70)
print(" Q8 Complete!")