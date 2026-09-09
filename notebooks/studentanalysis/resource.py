# ============================================
# Q14: Student-Designed Analysis 2
# Resource Efficiency Analysis
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q14: Resource Efficiency Analysis")
print("="*70)

# Step 1: Calculate efficiency metrics
print("\n Efficiency Metrics by Season:")
print("-"*50)

# Water Efficiency: Yield per unit of water
df['Water_Efficiency'] = df['Yield_Tonnes_Ha'] / (df['Water_Used_m3'] + 1)

# Cost Efficiency: Profit per unit of cost
df['Cost_Efficiency'] = df['Profit_INR'] / (df['Total_Cost_INR'] + 1)

# Water-Cost Efficiency: Combining both
df['Overall_Efficiency'] = df['Water_Efficiency'] * (df['Cost_Efficiency'] / df['Cost_Efficiency'].max())

# Calculate metrics by season
efficiency_metrics = df.groupby('Season').agg({
    'Water_Efficiency': 'mean',
    'Cost_Efficiency': 'mean',
    'Overall_Efficiency': 'mean',
    'Water_Used_m3': 'mean',
    'Yield_Tonnes_Ha': 'mean'
}).round(4)

print(" Efficiency Metrics by Season:")
print(efficiency_metrics)

# Step 2: Find most efficient season
print("\n Most Efficient Season:")
print("-"*50)

best_water = efficiency_metrics['Water_Efficiency'].idxmax()
best_cost = efficiency_metrics['Cost_Efficiency'].idxmax()
best_overall = efficiency_metrics['Overall_Efficiency'].idxmax()

print(f"    Best Water Efficiency: {best_water} ({efficiency_metrics.loc[best_water, 'Water_Efficiency']:.4f} Tonnes/m³)")
print(f"    Best Cost Efficiency: {best_cost} ({efficiency_metrics.loc[best_cost, 'Cost_Efficiency']:.4f})")
print(f"    Best Overall Efficiency: {best_overall} ({efficiency_metrics.loc[best_overall, 'Overall_Efficiency']:.4f})")

# Step 3: Water usage analysis
print("\n Water Usage Analysis:")
print("-"*50)

water_by_season = df.groupby('Season')['Water_Used_m3'].mean().sort_values(ascending=False)
for season, water in water_by_season.items():
    print(f"   {season}: {water:.2f} m³")

# Step 4: Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Water Efficiency by Season
efficiency_metrics['Water_Efficiency'].plot(kind='bar', ax=axes[0,0], color='blue')
axes[0,0].set_title('Water Efficiency by Season', fontsize=12, fontweight='bold')
axes[0,0].set_xlabel('Season')
axes[0,0].set_ylabel('Water Efficiency (Tonnes/m³)')
axes[0,0].tick_params(axis='x', rotation=0)

# Plot 2: Cost Efficiency by Season
efficiency_metrics['Cost_Efficiency'].plot(kind='bar', ax=axes[0,1], color='green')
axes[0,1].set_title('Cost Efficiency by Season', fontsize=12, fontweight='bold')
axes[0,1].set_xlabel('Season')
axes[0,1].set_ylabel('Cost Efficiency')
axes[0,1].tick_params(axis='x', rotation=0)

# Plot 3: Water Usage by Season
water_by_season.plot(kind='bar', ax=axes[1,0], color='skyblue')
axes[1,0].set_title('Average Water Usage by Season', fontsize=12, fontweight='bold')
axes[1,0].set_xlabel('Season')
axes[1,0].set_ylabel('Water Used (m³)')
axes[1,0].tick_params(axis='x', rotation=0)

# Plot 4: Overall Efficiency by Season
efficiency_metrics['Overall_Efficiency'].plot(kind='bar', ax=axes[1,1], color='purple')
axes[1,1].set_title('Overall Efficiency by Season', fontsize=12, fontweight='bold')
axes[1,1].set_xlabel('Season')
axes[1,1].set_ylabel('Overall Efficiency')
axes[1,1].tick_params(axis='x', rotation=0)

plt.tight_layout()
save_chart('q14_resource_efficiency.png')
plt.show()

# Step 5: Scatter plot - Water vs Yield
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['Water_Used_m3'], df['Yield_Tonnes_Ha'], 
                      c=df['Season'].map({'Kharif': 0, 'Rabi': 1, 'Zaid': 2}), 
                      alpha=0.5, cmap='viridis')
plt.title('Water Usage vs Yield (Colored by Season)', fontsize=14, fontweight='bold')
plt.xlabel('Water Used (m³)')
plt.ylabel('Yield (Tonnes/Ha)')
plt.colorbar(scatter, label='Season')
plt.tight_layout()
save_chart('q14_water_yield_scatter.png')
plt.show()

print("\n" + "="*70)
print(" Q14 Complete!")