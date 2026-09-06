# ============================================
# Q4: Descriptive Statistics
# - Descriptive statistical analysis performed
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q4: Descriptive Statistics")
print("="*70)

# Step 1: Get numerical columns
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
print(f" Numerical Columns: {len(numerical_cols)} columns")

# Step 2: Display descriptive statistics
print("\nDescriptive Statistics for All Numerical Columns:")
print(df[numerical_cols].describe().to_string())

# Step 3: Key Statistics Summary
print("\n" + "="*70)
print(" Key Statistics Summary:")
print("="*70)

# Farm size
print(f"\n Farm Size:")
print(f"   Total Area: {df['Farm_Area_Hectares'].sum():,.2f} hectares")
print(f"   Average Area: {df['Farm_Area_Hectares'].mean():.2f} hectares")
print(f"   Min Area: {df['Farm_Area_Hectares'].min():.2f} hectares")
print(f"   Max Area: {df['Farm_Area_Hectares'].max():.2f} hectares")

# Yield
print(f"\n Crop Yield:")
print(f"   Average Yield: {df['Yield_Tonnes_Ha'].mean():.2f} tonnes/ha")
print(f"   Min Yield: {df['Yield_Tonnes_Ha'].min():.2f} tonnes/ha")
print(f"   Max Yield: {df['Yield_Tonnes_Ha'].max():.2f} tonnes/ha")

# Production
print(f"\n Production:")
print(f"   Total Production: {df['Production_Tonnes'].sum():,.2f} tonnes")
print(f"   Average Production: {df['Production_Tonnes'].mean():.2f} tonnes")

# Financial
print(f"\n Financial Summary:")
print(f"   Total Revenue: ₹{df['Revenue_INR'].sum():,.2f}")
print(f"   Total Cost: ₹{df['Total_Cost_INR'].sum():,.2f}")
print(f"   Total Profit: ₹{df['Profit_INR'].sum():,.2f}")
print(f"   Average Revenue: ₹{df['Revenue_INR'].mean():,.2f}")
print(f"   Average Profit: ₹{df['Profit_INR'].mean():,.2f}")

# Resources
print(f"\n Resources:")
print(f"   Average Rainfall: {df['Rainfall_mm'].mean():.2f} mm")
print(f"   Average Temperature: {df['Avg_Temperature_C'].mean():.2f} °C")
print(f"   Average Humidity: {df['Humidity_pct'].mean():.2f}%")
print(f"   Total Water Used: {df['Water_Used_m3'].sum():,.2f} m³")

print("\n" + "="*70)
print("Q4 Complete!")