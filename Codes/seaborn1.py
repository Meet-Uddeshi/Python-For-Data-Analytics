# 3D graphs- histogram, scatter, bar plot, line plot
# 360 degree graphs- pie plot
# Note: Since Seaborn doesn't natively support 3D plotting, we use Matplotlib's 3D projection 
# while styling the visual theme and colors using Seaborn to keep it elegant and modern.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the seaborn theme for a premium, clean layout
sns.set_theme(style="whitegrid")

# Create dummy data for the 3D plot
np.random.seed(42)
n_points = 100
x = np.random.normal(size=n_points)
y = np.random.normal(size=n_points)
z = np.random.normal(size=n_points)
colors = np.random.randint(0, 100, size=n_points)  # Color values for aesthetics

# Create a figure and add a 3D subplot axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Generate a 3D scatter plot
# We map color values using a beautiful Seaborn-friendly colormap ('viridis')
scatter = ax.scatter(x, y, z, c=colors, cmap='viridis', s=60, edgecolors='w', depthshade=True)

# Add title and axes labels with premium styling
ax.set_title("Beautiful 3D Scatter Plot (Seaborn Styled)", fontsize=16, pad=20, fontweight='bold')
ax.set_xlabel("X-Axis (Feature 1)", fontsize=12, labelpad=10)
ax.set_ylabel("Y-Axis (Feature 2)", fontsize=12, labelpad=10)
ax.set_zlabel("Z-Axis (Target)", fontsize=12, labelpad=10)

# Add a color bar representing the scale of values
cbar = fig.colorbar(scatter, ax=ax, pad=0.1, shrink=0.6)
cbar.set_label("Intensity Scale", fontsize=12)

# Display the 3D graph
plt.tight_layout()
plt.show()
