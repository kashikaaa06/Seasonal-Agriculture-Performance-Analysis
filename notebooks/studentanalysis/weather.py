# ============================================
# Q15: Student-Designed Analysis 3
# Weather Impact Analysis
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q15: Weather Impact Analysis")
print("="*70)

# Step 1: Weather summary by season
print("\n Weather Summary by Season:")
print("-"*50)

weather_summary = df.groupby('Season').agg({
    'Rainfall_mm': 'mean',
    'Avg_Temperature_C': 'mean',
    'Humidity_pct': 'mean',
    'Yield_Tonnes_Ha': 'mean'
}).round(2)

print(weather_summary)

# Step 2: Correlation with weather variables
print("\n Weather Correlations with Yield:")
print("-"*50)

rain_corr = df['Rainfall_mm'].corr(df['Yield_Tonnes_Ha'])
temp_corr = df['Avg_Temperature_C'].corr(df['Yield_Tonnes_Ha'])
humidity_corr = df['Humidity_pct'].corr(df['Yield_Tonnes_Ha'])

print(f"   Rainfall vs Yield: {rain_corr:.3f}")
print(f"   Temperature vs Yield: {temp_corr:.3f}")
print(f"   Humidity vs Yield: {humidity_corr:.3f}")

if rain_corr > 0.3:
    print("    Rainfall has a positive correlation with yield")
elif rain_corr < -0.3:
    print("    Rainfall has a negative correlation with yield")
else:
    print("    Rainfall has weak correlation with yield")

# Step 3: Optimal weather conditions
print("\n Optimal Weather Conditions for High Yield:")
print("-"*50)

# Create yield categories
df['Yield_Category'] = pd.cut(df['Yield_Tonnes_Ha'], 
                               bins=[0, 2, 4, 6, 10], 
                               labels=['Low', 'Medium', 'High', 'Very High'])

weather_optimal = df.groupby('Yield_Category').agg({
    'Rainfall_mm': 'mean',
    'Avg_Temperature_C': 'mean',
    'Humidity_pct': 'mean'
}).round(2)

print(weather_optimal)

print("\n Optimal Conditions for Very High Yield:")
very_high = weather_optimal.loc['Very High']
print(f"   Rainfall: {very_high['Rainfall_mm']:.2f} mm")
print(f"   Temperature: {very_high['Avg_Temperature_C']:.2f} °C")
print(f"   Humidity: {very_high['Humidity_pct']:.2f}%")

# Step 4: Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Rainfall by Season
weather_summary['Rainfall_mm'].plot(kind='bar', ax=axes[0,0], color='blue')
axes[0,0].set_title('Average Rainfall by Season', fontsize=12, fontweight='bold')
axes[0,0].set_xlabel('Season')
axes[0,0].set_ylabel('Rainfall (mm)')
axes[0,0].tick_params(axis='x', rotation=0)

# Plot 2: Temperature by Season
weather_summary['Avg_Temperature_C'].plot(kind='bar', ax=axes[0,1], color='red')
axes[0,1].set_title('Average Temperature by Season', fontsize=12, fontweight='bold')
axes[0,1].set_xlabel('Season')
axes[0,1].set_ylabel('Temperature (°C)')
axes[0,1].tick_params(axis='x', rotation=0)

# Plot 3: Weather vs Yield Correlation (Heatmap)
weather_vars = ['Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 'Yield_Tonnes_Ha']
weather_corr = df[weather_vars].corr()
sns.heatmap(weather_corr, ax=axes[1,0], annot=True, fmt='.2f', cmap='coolwarm', center=0)
axes[1,0].set_title('Weather-Yield Correlations', fontsize=12, fontweight='bold')

# Plot 4: 3D-like scatter (Rainfall vs Temperature vs Yield)
scatter = axes[1,1].scatter(df['Rainfall_mm'], df['Avg_Temperature_C'], 
                            c=df['Yield_Tonnes_Ha'], cmap='viridis', alpha=0.5)
axes[1,1].set_title('Rainfall vs Temperature (Color = Yield)', fontsize=12, fontweight='bold')
axes[1,1].set_xlabel('Rainfall (mm)')
axes[1,1].set_ylabel('Temperature (°C)')
plt.colorbar(scatter, ax=axes[1,1], label='Yield (Tonnes/Ha)')

plt.tight_layout()
save_chart('q15_weather_impact.png')
plt.show()

# Step 5: Weather impact insights
print("\n" + "="*70)
print(" Weather Impact Insights:")
print("="*70)

print(f"1. {weather_summary['Rainfall_mm'].idxmax()} season has highest rainfall ({weather_summary['Rainfall_mm'].max():.2f} mm)")
print(f"2. {weather_summary['Avg_Temperature_C'].idxmax()} season is hottest ({weather_summary['Avg_Temperature_C'].max():.2f} °C)")
print(f"3. {weather_summary['Yield_Tonnes_Ha'].idxmax()} season gives best yield ({weather_summary['Yield_Tonnes_Ha'].max():.2f} Tonnes/Ha)")
print(f"4. Optimal rainfall for high yield: {weather_optimal.loc['Very High', 'Rainfall_mm']:.2f} mm")
print(f"5. Optimal temperature for high yield: {weather_optimal.loc['Very High', 'Avg_Temperature_C']:.2f} °C")

print("\n" + "="*70)
print(" Q15 Complete!")