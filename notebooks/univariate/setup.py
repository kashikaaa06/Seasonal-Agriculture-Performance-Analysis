# ============================================
# COMMON SETUP - Section 3: Univariate Analysis
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

# Load the data
df = pd.read_csv('../../data/agriculture_dataset.csv')

print("="*70)
print(" SEASONAL AGRICULTURE PERFORMANCE ANALYSIS")
print(" SECTION 3: UNIVARIATE ANALYSIS")
print("="*70)
print(f" Data loaded: {df.shape[0]:,} rows, {df.shape[1]} columns")
print("="*70)


def save_chart(filename):
    os.makedirs('../../visualizations', exist_ok=True)
    plt.savefig(f'../../visualizations/{filename}', dpi=300, bbox_inches='tight')
    print(f" Chart saved: visualizations/{filename}")