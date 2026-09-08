# ============================================
# Q10: Bivariate Analysis
# - Bivariate analysis completed
# - Seasonal comparisons started
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q10: Bivariate Analysis")
print("="*70)

# Step 1: Season vs Yield
print("\n Season vs Yield:")
print("-"*40)
season_yield = df.groupby('Season')['Yield_Tonnes_Ha'].mean().sort_values(ascending=False)
for season, yield_val in season_yield.items():
    print(f"   {season}: {yield_val:.2f} Tonnes/Ha")

# Step 2: Season vs Profit
print("\nSeason vs Profit:")
print("-"*40)
season_profit = df.groupby('Season')['Profit_INR'].mean().sort_values(ascending=False)
for season, profit in season_profit.items():
    print(f"   {season}: ₹{profit:,.2f}")

# Step 3: Correlation between key pairs
print("\n Correlation between Key Pairs:")
print("-"*40)

pairs = [
    ('Rainfall_mm', 'Yield_Tonnes_Ha'),
    ('Yield_Tonnes_Ha', 'Profit_INR'),
    ('Water_Used_m3', 'Yield_Tonnes_Ha'),
    ('Avg_Temperature_C', 'Yield_Tonnes_Ha'),
    ('Farm_Area_Hectares', 'Production_Tonnes'),
    ('Revenue_INR', 'Profit_INR')
]

for pair in pairs:
    corr = df[pair[0]].corr(df[pair[1]])
    if corr > 0.3:
        strength = "Positive"
    elif corr < -0.3:
        strength = "Negative"
    else:
        strength = "Weak/No"
    print(f"   {pair[0]} vs {pair[1]}: {corr:.3f} ({strength} correlation)")

# Step 4: Create visualizations
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Plot 1: Season vs Yield (Boxplot)
df.boxplot(column='Yield_Tonnes_Ha', by='Season', ax=axes[0,0])
axes[0,0].set_title('Yield by Season', fontsize=11, fontweight='bold')
axes[0,0].set_xlabel('Season')
axes[0,0].set_ylabel('Yield (Tonnes/Ha)')

# Plot 2: Season vs Profit (Boxplot)
df.boxplot(column='Profit_INR', by='Season', ax=axes[0,1])
axes[0,1].set_title('Profit by Season', fontsize=11, fontweight='bold')
axes[0,1].set_xlabel('Season')
axes[0,1].set_ylabel('Profit (INR)')

# Plot 3: Rainfall vs Yield (Scatter)
scatter = axes[0,2].scatter(df['Rainfall_mm'], df['Yield_Tonnes_Ha'], 
                            c=df['Season'].map({'Kharif': 0, 'Rabi': 1, 'Zaid': 2}), 
                            alpha=0.5, cmap='viridis')
axes[0,2].set_title('Rainfall vs Yield', fontsize=11, fontweight='bold')
axes[0,2].set_xlabel('Rainfall (mm)')
axes[0,2].set_ylabel('Yield (Tonnes/Ha)')

# Plot 4: Yield vs Profit (Scatter)
axes[1,0].scatter(df['Yield_Tonnes_Ha'], df['Profit_INR'], alpha=0.5, color='green')
axes[1,0].set_title('Yield vs Profit', fontsize=11, fontweight='bold')
axes[1,0].set_xlabel('Yield (Tonnes/Ha)')
axes[1,0].set_ylabel('Profit (INR)')

# Plot 5: Temperature vs Yield (Scatter)
axes[1,1].scatter(df['Avg_Temperature_C'], df['Yield_Tonnes_Ha'], alpha=0.5, color='red')
axes[1,1].set_title('Temperature vs Yield', fontsize=11, fontweight='bold')
axes[1,1].set_xlabel('Temperature (°C)')
axes[1,1].set_ylabel('Yield (Tonnes/Ha)')

# Plot 6: Water vs Yield (Scatter)
axes[1,2].scatter(df['Water_Used_m3'], df['Yield_Tonnes_Ha'], alpha=0.5, color='blue')
axes[1,2].set_title('Water Usage vs Yield', fontsize=11, fontweight='bold')
axes[1,2].set_xlabel('Water Used (m³)')
axes[1,2].set_ylabel('Yield (Tonnes/Ha)')

plt.tight_layout()
save_chart('q10_bivariate_analysis.png')
plt.show()

print("\n" + "="*70)
print("✅ Q10 Complete!")