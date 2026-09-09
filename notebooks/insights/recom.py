# ============================================
# Q16: Key Insights & Recommendations
# - 3 meaningful insights documented
# - Evidence-based recommendations provided
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q16: Key Insights & Recommendations")
print("="*70)

# Step 1: Calculate key metrics for insights
print("\n CALCULATING KEY METRICS FOR INSIGHTS...")
print("-"*50)

# Season-wise metrics
season_metrics = df.groupby('Season').agg({
    'Yield_Tonnes_Ha': 'mean',
    'Profit_INR': 'mean',
    'Revenue_INR': 'mean',
    'Production_Tonnes': 'mean',
    'Water_Used_m3': 'mean'
}).round(2)

print("\n Seasonal Performance Summary:")
print(season_metrics)

# Crop-wise metrics (top 5)
top_crops = df.groupby('Crop').agg({
    'Yield_Tonnes_Ha': 'mean',
    'Profit_INR': 'mean'
}).sort_values('Yield_Tonnes_Ha', ascending=False).head(5)

print("\n Top 5 Crops by Yield:")
print(top_crops)

# State-wise metrics (top 5)
top_states = df.groupby('State').agg({
    'Yield_Tonnes_Ha': 'mean',
    'Profit_INR': 'mean'
}).sort_values('Yield_Tonnes_Ha', ascending=False).head(5)

print("\n Top 5 States by Yield:")
print(top_states)

# Step 2: Extract 3 Key Insights
print("\n" + "="*70)
print("🔍 3 KEY INSIGHTS FROM THE ANALYSIS")
print("="*70)

# Insight 1: Best Season
best_season = season_metrics['Yield_Tonnes_Ha'].idxmax()
best_yield = season_metrics.loc[best_season, 'Yield_Tonnes_Ha']
best_profit_season = season_metrics['Profit_INR'].idxmax()
best_profit = season_metrics.loc[best_profit_season, 'Profit_INR']

print(f"\n INSIGHT 1: Seasonal Performance")
print(f"   {best_season} season gives the highest average yield ({best_yield:.2f} Tonnes/Ha)")
print(f"   {best_profit_season} season is the most profitable (₹{best_profit:,.2f})")
print(f"    Evidence: Based on analysis of {len(df):,} records across all seasons")

# Insight 2: Best Crop
best_crop = df.groupby('Crop')['Yield_Tonnes_Ha'].mean().idxmax()
best_crop_yield = df.groupby('Crop')['Yield_Tonnes_Ha'].mean().max()
best_crop_profit = df.groupby('Crop')['Profit_INR'].mean().idxmax()

print(f"\n INSIGHT 2: Crop Performance")
print(f"   {best_crop} is the highest yielding crop ({best_crop_yield:.2f} Tonnes/Ha)")
print(f"   {best_crop_profit} is the most profitable crop")
print(f"    Evidence: Analysis across all states and seasons")

# Insight 3: Weather Impact
rain_corr = df['Rainfall_mm'].corr(df['Yield_Tonnes_Ha'])
temp_corr = df['Avg_Temperature_C'].corr(df['Yield_Tonnes_Ha'])

print(f"\n INSIGHT 3: Weather Impact on Agriculture")
print(f"   Rainfall-Yield Correlation: {rain_corr:.3f}")
print(f"   Temperature-Yield Correlation: {temp_corr:.3f}")
if rain_corr > 0.3:
    print(f"    Higher rainfall is associated with better crop yields")
else:
    print(f"    Rainfall alone is not a strong predictor of yield")
if temp_corr < -0.3:
    print(f"    Higher temperatures are associated with lower yields")
else:
    print(f"    Temperature alone is not a strong predictor of yield")

# Step 3: Generate Recommendations
print("\n" + "="*70)
print(" EVIDENCE-BASED RECOMMENDATIONS")
print("="*70)

print("\n RECOMMENDATION 1: Seasonal Planning")
print("-"*50)
print(f"   ➜ Farmers should focus on {best_season} season for maximum yield")
print(f"   ➜ Plant high-value crops during {best_profit_season} for better profits")
print(f"   ➜ Consider crop rotation across seasons for sustainable farming")

print("\n RECOMMENDATION 2: Crop Selection")
print("-"*50)
print(f"   ➜ {best_crop} is recommended for high yield")
print(f"   ➜ {best_crop_profit} is recommended for high profit")
print(f"   ➜ Farmers should choose crops based on their local conditions")

print("\n RECOMMENDATION 3: Resource Management")
print("-"*50)
# Find most water-efficient season
water_efficiency = df.groupby('Season').apply(
    lambda x: x['Yield_Tonnes_Ha'].mean() / (x['Water_Used_m3'].mean() + 1)
)
best_water_season = water_efficiency.idxmax()
print(f"   ➜ {best_water_season} season is the most water-efficient")
print(f"   ➜ Use drip irrigation to reduce water usage")
print(f"   ➜ Monitor weather patterns for optimal planting time")

print("\n RECOMMENDATION 4: Regional Focus")
print("-"*50)
best_state = df.groupby('State')['Yield_Tonnes_Ha'].mean().idxmax()
best_state_yield = df.groupby('State')['Yield_Tonnes_Ha'].mean().max()
print(f"   ➜ {best_state} shows the highest average yield ({best_state_yield:.2f} Tonnes/Ha)")
print(f"   ➜ Consider replicating successful farming practices from top states")

# Step 4: Create Summary Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Season-wise Yield
season_metrics['Yield_Tonnes_Ha'].plot(kind='bar', ax=axes[0,0], color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
axes[0,0].set_title('Yield by Season', fontsize=12, fontweight='bold')
axes[0,0].set_xlabel('Season')
axes[0,0].set_ylabel('Yield (Tonnes/Ha)')
axes[0,0].tick_params(axis='x', rotation=0)

# Plot 2: Season-wise Profit
season_metrics['Profit_INR'].plot(kind='bar', ax=axes[0,1], color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
axes[0,1].set_title('Profit by Season', fontsize=12, fontweight='bold')
axes[0,1].set_xlabel('Season')
axes[0,1].set_ylabel('Profit (INR)')
axes[0,1].tick_params(axis='x', rotation=0)

# Plot 3: Top Crops by Yield
top_crops['Yield_Tonnes_Ha'].plot(kind='bar', ax=axes[1,0], color='lightgreen')
axes[1,0].set_title('Top 5 Crops by Yield', fontsize=12, fontweight='bold')
axes[1,0].set_xlabel('Crop')
axes[1,0].set_ylabel('Yield (Tonnes/Ha)')
axes[1,0].tick_params(axis='x', rotation=45)

# Plot 4: Top States by Yield
top_states['Yield_Tonnes_Ha'].plot(kind='bar', ax=axes[1,1], color='skyblue')
axes[1,1].set_title('Top 5 States by Yield', fontsize=12, fontweight='bold')
axes[1,1].set_xlabel('State')
axes[1,1].set_ylabel('Yield (Tonnes/Ha)')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
save_chart('q16_insights_summary.png')
plt.show()

print("\n" + "="*70)
print(" Q16 Complete!")