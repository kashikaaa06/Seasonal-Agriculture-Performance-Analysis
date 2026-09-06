# ============================================
# Q5: Outlier Analysis
# - Outliers investigated
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q5: Outlier Analysis")
print("="*70)

# Step 1: Key columns for outlier analysis
key_cols = ['Yield_Tonnes_Ha', 'Profit_INR', 'Revenue_INR', 
            'Water_Used_m3', 'Production_Tonnes']

print(" Outlier Investigation using IQR Method:")
print("="*70)

# Step 2: Calculate outliers for each column
outlier_summary = {}

for col in key_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outlier_count = len(outliers)
    outlier_pct = (outlier_count / len(df)) * 100
    
    outlier_summary[col] = {
        'Q1': Q1, 'Q3': Q3, 'IQR': IQR,
        'lower': lower_bound, 'upper': upper_bound,
        'count': outlier_count, 'pct': outlier_pct
    }
    
    print(f"\n{col}:")
    print(f"   Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
    print(f"   Lower Bound: {lower_bound:.2f}, Upper Bound: {upper_bound:.2f}")
    print(f"   Outliers: {outlier_count} ({outlier_pct:.2f}%)")

# Step 3: Find columns with most outliers
print("\n" + "="*70)
print("Columns with Most Outliers:")
print("="*70)
sorted_outliers = sorted(outlier_summary.items(), key=lambda x: x[1]['count'], reverse=True)
for col, data in sorted_outliers:
    print(f"   {col}: {data['count']} outliers ({data['pct']:.2f}%)")

# Step 4: Create visualization
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

for idx, col in enumerate(key_cols):
    row, col_idx = idx // 3, idx % 3
    df.boxplot(column=col, ax=axes[row, col_idx])
    axes[row, col_idx].set_title(f'Boxplot of {col}', fontsize=11, fontweight='bold')
    axes[row, col_idx].set_ylabel(col)

# Remove empty subplot
if len(key_cols) < 6:
    fig.delaxes(axes[1, 2])

plt.tight_layout()
save_chart('q5_outliers.png')
plt.show()

print("\n" + "="*70)
print(" Q5 Complete!")