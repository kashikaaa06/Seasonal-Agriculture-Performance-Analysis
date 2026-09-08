# ============================================
# Q9: Univariate Analysis - Seasonal Distribution
# - Seasonal distribution analyzed
# - Season-wise performance distributions
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q9: Seasonal Distribution Analysis")
print("="*70)

# Step 1: Count records by season
season_counts = df['Season'].value_counts()

print(" Seasonal Distribution:")
print("="*70)
for season, count in season_counts.items():
    pct = (count / len(df)) * 100
    print(f"   {season}: {count:,} records ({pct:.2f}%)")

# Step 2: Key metrics by season
print("\n" + "="*70)
print(" Key Metrics by Season:")
print("="*70)

season_metrics = df.groupby('Season').agg({
    'Yield_Tonnes_Ha': 'mean',
    'Profit_INR': 'mean',
    'Revenue_INR': 'mean',
    'Production_Tonnes': 'mean',
    'Water_Used_m3': 'mean'
}).round(2)

print(season_metrics)

# Step 3: Best season for each metric
print("\n" + "="*70)
print(" Best Season by Metric:")
print("="*70)

metrics = ['Yield_Tonnes_Ha', 'Profit_INR', 'Revenue_INR', 'Production_Tonnes']
for metric in metrics:
    best_season = season_metrics[metric].idxmax()
    best_value = season_metrics[metric].max()
    print(f"   {metric}: {best_season} ({best_value:.2f})")

# Step 4: Create visualizations
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart - Season counts
season_counts.plot(kind='bar', ax=axes[0], color=['#FF6B6B', '#4ECDC4', '#45B7D1'], edgecolor='black')
axes[0].set_title('Distribution of Records by Season', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Season', fontsize=11)
axes[0].set_ylabel('Number of Records', fontsize=11)
axes[0].tick_params(axis='x', rotation=0)

# Pie chart - Season distribution
season_counts.plot(kind='pie', ax=axes[1], autopct='%1.1f%%', startangle=90)
axes[1].set_title('Season Distribution', fontsize=12, fontweight='bold')
axes[1].set_ylabel('')

plt.tight_layout()
save_chart('q9_seasonal_distribution.png')
plt.show()

# Step 5: Season-wise yield distribution
plt.figure(figsize=(10, 6))
df.boxplot(column='Yield_Tonnes_Ha', by='Season')
plt.title('Yield Distribution by Season', fontsize=14, fontweight='bold')
plt.suptitle('')
plt.xlabel('Season', fontsize=12)
plt.ylabel('Yield (Tonnes/Ha)', fontsize=12)
plt.tight_layout()
save_chart('q9_yield_by_season.png')
plt.show()

print("\n" + "="*70)
print(" Q9 Complete!")