# ============================================
# COMMON SETUP - Section 1: Data Loading & Cleaning
# This file is imported by all question files
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Load the data - CORRECT FILENAME
df = pd.read_csv('../../data/agriculture_dataset.csv')

print("="*70)
print(" SEASONAL AGRICULTURE PERFORMANCE ANALYSIS")
print(" SECTION 1: DATA LOADING & CLEANING")
print("="*70)
print(f" Data loaded: {df.shape[0]:,} rows, {df.shape[1]} columns")
print(f" Columns: {df.columns.tolist()}")
print("="*70)

# Helper function to save charts
def save_chart(filename):
    os.makedirs('../../visualizations', exist_ok=True)
    plt.savefig(f'../../visualizations/{filename}', dpi=300, bbox_inches='tight')
    print(f" Chart saved: visualizations/{filename}")