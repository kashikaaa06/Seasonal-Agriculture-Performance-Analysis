# ============================================
# Q13: Student-Designed Analysis 1
# Crop Performance by State
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("\n" + "="*70)
print("Q13: Crop Performance by State")
print("="*70)

# Step 1: Find best crop for each state (by yield)
print("\n Best Crop by State (by Yield):")
print("-"*50)

# Get top 10 states by number of records
top_states = df['State'].value_counts().head(10).index.tolist()

for state in top_states:
    state_data = df[df['State'] == state]
    best_crop = state_data.groupby('Crop')['Yield_Tonnes_Ha'].mean().idxmax()
    best_yield = state_data.groupby('Crop')['Yield_Tonnes_Ha'].mean().max()
    print(f"   {state}: {best_crop} ({best_yield:.2f} Tonnes/Ha)")

# Step 2: Find best crop for each state (by profit)
print("\n Best Crop by State (by Profit):")
print("-"*50)

for state in top_states:
    state_data = df[df['State'] == state]
    best_crop = state_data.groupby('Crop')['Profit_INR'].mean().idxmax()
    best_profit = state_data.groupby('Crop')['Profit_INR'].mean().max()
    print(f"   {state}: {best_crop} (₹{best_profit:,.2f})")

# Step 3: Find best state for each crop
print("\n Best State for Each Major Crop:")
print("-"*50)

# Get top 10 crops
top_crops = df['Crop'].value_counts().head(10).index.tolist()

for crop in top_crops:
    crop_data = df[df['Crop'] == crop]
    best_state = crop_data.groupby('State')['Yield_Tonnes_Ha'].mean().idxmax()
    best_yield = crop_data.groupby('State')['Yield_Tonnes_Ha'].mean().max()
    print(f"   {crop}: {best_state} ({best_yield:.2f} Tonnes/Ha)")

# Step 4: Create visualizations
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: State-wise average yield (top 10 states)
state_yield = df.groupby('State')['Yield_Tonnes_Ha'].mean().sort_values(ascending=False).head(10)
state_yield.plot(kind='bar', ax=axes[0], color='skyblue', edgecolor='black')
axes[0].set_title('Top 10 States by Average Yield', fontsize=12, fontweight='bold')
axes[0].set_xlabel('State')
axes[0].set_ylabel('Average Yield (Tonnes/Ha)')
axes[0].tick_params(axis='x', rotation=45)

# Plot 2: State-wise average profit (top 10 states)
state_profit = df.groupby('State')['Profit_INR'].mean().sort_values(ascending=False).head(10)
state_profit.plot(kind='bar', ax=axes[1], color='lightgreen', edgecolor='black')
axes[1].set_title('Top 10 States by Average Profit', fontsize=12, fontweight='bold')
axes[1].set_xlabel('State')
axes[1].set_ylabel('Average Profit (INR)')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
save_chart('q13_crop_by_state.png')
plt.show()

# Step 5: Heatmap - State vs Crop (Yield)
print("\n📊 Creating State vs Crop Yield Heatmap...")
pivot_state_crop = df.pivot_table(values='Yield_Tonnes_Ha', 
                                   index='State', 
                                   columns='Crop', 
                                   aggfunc='mean')

# Select top states and crops for better visualization
top_states_list = df['State'].value_counts().head(8).index.tolist()
top_crops_list = df['Crop'].value_counts().head(8).index.tolist()

pivot_filtered = pivot_state_crop.loc[top_states_list, top_crops_list]

plt.figure(figsize=(12, 8))
sns.heatmap(pivot_filtered, annot=True, fmt='.2f', cmap='YlGn', linewidths=0.5)
plt.title('State vs Crop: Average Yield (Tonnes/Ha)', fontsize=14, fontweight='bold')
plt.tight_layout()
save_chart('q13_state_crop_heatmap.png')
plt.show()

print("\n" + "="*70)
print(" Q13 Complete!")