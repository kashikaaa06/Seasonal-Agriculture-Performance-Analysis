# ============================================
# Q12: Seasonal Comparisons
# - Seasonal comparisons performed
# - Compare Kharif, Rabi, Zaid across multiple metrics
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q12: Seasonal Comparisons")
print("="*70)

# Step 1: Compare seasons across multiple metrics
print("📊 Seasonal Performance Comparison:")
print("="*70)

metrics = {
    'Yield (Tonnes/Ha)': 'Yield_Tonnes_Ha',
    'Profit (INR)': 'Profit_INR',
    'Revenue (INR)': 'Revenue_INR',
    'Production (Tonnes)': 'Production_Tonnes',
    'Water Used (m³)': 'Water_Used_m3'
}

season_comparison = {}
for metric_name, col in metrics.items():
    avg_by_season = df.groupby('Season')[col].mean().sort_values(ascending=False)
    season_comparison[metric_name] = avg_by_season
    
    print(f"\n📊 {metric_name}:")
    for season, value in avg_by_season.items():
        print(f"   {season}: {value:.2f}")

# Step 2: Identify best season for each metric
print("\n" + "="*70)
print("🏆 Best Season by Metric:")
print("="*70)

for metric_name, avg_by_season in season_comparison.items():
    best_season = avg_by_season.index[0]
    best_value = avg_by_season.iloc[0]
    print(f"   {metric_name}: {best_season} ({best_value:.2f})")

# Step 3: Create comparison table
print("\n" + "="*70)
print("📊 Seasonal Comparison Table:")
print("="*70)

comparison_df = pd.DataFrame(season_comparison)
print(comparison_df.round(2))

# Step 4: Create visualizations
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Plot 1: Yield comparison
comparison_df['Yield (Tonnes/Ha)'].plot(kind='bar', ax=axes[0,0], color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
axes[0,0].set_title('Yield by Season', fontsize=12, fontweight='bold')
axes[0,0].set_xlabel('Season')
axes[0,0].set_ylabel('Yield (Tonnes/Ha)')
axes[0,0].tick_params(axis='x', rotation=0)

# Plot 2: Profit comparison
comparison_df['Profit (INR)'].plot(kind='bar', ax=axes[0,1], color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
axes[0,1].set_title('Profit by Season', fontsize=12, fontweight='bold')
axes[0,1].set_xlabel('Season')
axes[0,1].set_ylabel('Profit (INR)')
axes[0,1].tick_params(axis='x', rotation=0)

# Plot 3: Revenue comparison
comparison_df['Revenue (INR)'].plot(kind='bar', ax=axes[0,2], color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
axes[0,2].set_title('Revenue by Season', fontsize=12, fontweight='bold')
axes[0,2].set_xlabel('Season')
axes[0,2].set_ylabel('Revenue (INR)')
axes[0,2].tick_params(axis='x', rotation=0)

# Plot 4: Production comparison
comparison_df['Production (Tonnes)'].plot(kind='bar', ax=axes[1,0], color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
axes[1,0].set_title('Production by Season', fontsize=12, fontweight='bold')
axes[1,0].set_xlabel('Season')
axes[1,0].set_ylabel('Production (Tonnes)')
axes[1,0].tick_params(axis='x', rotation=0)

# Plot 5: Water usage comparison
comparison_df['Water Used (m³)'].plot(kind='bar', ax=axes[1,1], color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
axes[1,1].set_title('Water Usage by Season', fontsize=12, fontweight='bold')
axes[1,1].set_xlabel('Season')
axes[1,1].set_ylabel('Water Used (m³)')
axes[1,1].tick_params(axis='x', rotation=0)

# Plot 6: Radar chart (spider chart) - better for comparison
from math import pi
categories = comparison_df.columns.tolist()
N = len(categories)

# Normalize values for radar chart
normalized = comparison_df.copy()
for col in normalized.columns:
    normalized[col] = (normalized[col] - normalized[col].min()) / (normalized[col].max() - normalized[col].min())

# Create angles
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Plot radar
ax = axes[1,2]
for i, season in enumerate(normalized.index):
    values = normalized.loc[season].tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, label=season)
    ax.fill(angles, values, alpha=0.1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=8)
ax.set_title('Seasonal Performance Comparison (Normalized)', fontsize=12, fontweight='bold')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))

plt.tight_layout()
save_chart('q12_seasonal_comparisons.png')
plt.show()

print("\n" + "="*70)
print("✅ Q12 Complete!")