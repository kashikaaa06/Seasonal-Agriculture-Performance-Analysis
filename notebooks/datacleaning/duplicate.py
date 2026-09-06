# Q3: Duplicate records 
# - Duplicate records can be identified and handled 

exec(open('setup.py').read())
print("\n"+"="*70)
print("Q3: Duplicate Records")
print("="*70)
duplicate_count = df.duplicated().sum()
print(f"Duplicate Records Before: {duplicate_count}")



if duplicate_count > 0:
    print(f"Found {duplicate_count} duplicate records!")
    
    # Step 2: Remove duplicates
    df.drop_duplicates(inplace=True)
    print(f" Removed {duplicate_count} duplicate records")
    
    # Step 3: Verify
    duplicate_after = df.duplicated().sum()
    print(f" Duplicate Records After: {duplicate_after}")
else:
    print(" No duplicate records found in the dataset!")

# Step 4: Final dataset shape
print(f"\n Final Dataset Shape:")
print(f" Rows: {df.shape[0]:,}")
print(f" Columns: {df.shape[1]}")

print("\n" + "="*70)
print(" Q3 Complete!")