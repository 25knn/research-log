import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, PathPatch

# Simple script to generate the cover image
# Run this locally to get 'minkowski_viz.png'

def setup_plot():
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    for a in ax:
        a.set_aspect('equal')
        a.axis('off')
        a.set_xlim(-2, 2)
        a.set_ylim(-2, 2)
    return fig, ax

# Génération de l'image simplifiée pour l'exemple
fig, ax = setup_plot()
circle = Circle((0, 0), 0.5, facecolor='#e74c3c')
ax[1].add_patch(circle)
ax[1].text(0,0, "B", color="white", ha="center")
plt.savefig('minkowski_viz.png', dpi=300, bbox_inches='tight')
print("Image generated.")
