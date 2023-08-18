import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create initial planet and atmosphere data
planet_radius = 1
initial_atmosphere_radius = 1.5
final_atmosphere_radius = 1.0
num_frames = 50

# Create figure and axis
fig, ax = plt.subplots()

# Initialize photon positions and velocities
num_photons = 15
photon_positions = np.linspace(-planet_radius * 2.5, -planet_radius * 1.5, num_photons)
photon_speeds = np.linspace(0.01, 0.1, num_photons)  # Adjust speeds as needed

def update(frame):
    ax.clear()

    # Calculate new atmosphere radius for this frame
    frame_progress = frame / num_frames
    current_atmosphere_radius = initial_atmosphere_radius - frame_progress * (initial_atmosphere_radius - final_atmosphere_radius)

    # Plot planet
    planet = plt.Circle((0, 0), planet_radius, color='blue')
    ax.add_patch(planet)

    # Plot atmosphere
    atmosphere = plt.Circle((0, 0), current_atmosphere_radius, color='lightblue', alpha=0.5)
    ax.add_patch(atmosphere)

    # Plot photons as arrows coming from the left and moving right
    for i in range(num_photons):
        if photon_positions[i] < -current_atmosphere_radius:
            ax.arrow(photon_positions[i], 0, photon_speeds[i], 0, head_width=0.1, head_length=0.1, fc='y', ec='y')
            photon_positions[i] += photon_speeds[i]
    # Set plot limits
    ax.set_xlim(-planet_radius * 2.5, planet_radius * 1.5)
    ax.set_ylim(-planet_radius * 1.5, planet_radius * 1.5)

    # Add title
    ax.set_title(f'Frame {frame+1}/{num_frames}')

# Create animation
ani = FuncAnimation(fig, update, frames=50, interval=100)

plt.show()
ani.save('photo_eva.gif', writer='imagemagick', fps=30)
