# ============================================
# Q6: Correlation Analysis
# - Correlation analysis completed
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q6: Correlation Analysis")
print("="*70)

# Step 1: Select numerical columns for correlation
corr_cols = ['Farm_Area_Hectares', 'Rainfall_mm', 'Avg_Temperature_C', 
             'Humidity_pct', 'Yield_Tonnes_Ha', 'Production_Tonnes',
             'Revenue_INR', 'Total_Cost_INR', 'Profit_INR', 'Water_Used_m3']

print(" Correlation Analysis between these variables:")
for col in corr_cols:
    print(f"   - {col}")

# Step 2: Calculate correlation matrix
corr_matrix = df[corr_cols].corr()

print("\n Correlation Matrix:")
print(corr_matrix.to_string())

# Step 3: Find strongest correlations
print("\n" + "="*70)
print(" Strongest Correlations:")
print("="*70)

# Get all correlation pairs (excluding self-correlations)
corr_pairs = []
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        corr_value = corr_matrix.iloc[i, j]
        corr_pairs.append((corr_matrix.columns[i], corr_matrix.columns[j], corr_value))

# Sort by absolute correlation value
corr_pairs_sorted = sorted(corr_pairs, key=lambda x: abs(x[2]), reverse=True)

print("\n Top 10 Strongest Correlations:")
for i, pair in enumerate(corr_pairs_sorted[:10], 1):
    strength = "Strong" if abs(pair[2]) > 0.5 else "Moderate" if abs(pair[2]) > 0.3 else "Weak"
    direction = "Positive" if pair[2] > 0 else "Negative"
    print(f"   {i}. {pair[0]} ↔ {pair[1]}: {pair[2]:.3f} ({direction}, {strength})")

# Step 4: Create heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            fmt='.2f', square=True, linewidths=0.5)
plt.title('Correlation Heatmap of Agricultural Variables', 
          fontsize=14, fontweight='bold')
plt.tight_layout()
save_chart('q6_correlation_heatmap.png')
plt.show()

# Step 5: Key insights from correlation
print("\n" + "="*70)
print(" Key Correlation Insights:")
print("="*70)

# Find correlations with Yield
yield_corr = corr_matrix['Yield_Tonnes_Ha'].sort_values(ascending=False)
print("\n Factors affecting Crop Yield:")
for var, corr in yield_corr.items():
    if var != 'Yield_Tonnes_Ha':
        if abs(corr) > 0.3:
            print(f"   {var}: {corr:.3f}")

# Find correlations with Profit
profit_corr = corr_matrix['Profit_INR'].sort_values(ascending=False)
print("\n Factors affecting Profit:")
for var, corr in profit_corr.items():
    if var != 'Profit_INR':
        if abs(corr) > 0.3:
            print(f"   {var}: {corr:.3f}")

print("\n" + "="*70)
print(" Q6 Complete!")