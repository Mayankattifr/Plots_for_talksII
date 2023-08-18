import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
mass_central_body = 5.972e24  # Mass of the central body (e.g., Earth) in kg
radius_central_body = 2.5e6  # Reduced radius of the central body in meters
orbital_radius = 1.5e7  # Orbital radius of the central body in meters
orbital_speed = 1.0e3  # Orbital speed of the central body in m/s
num_frames = 200  # Number of frames in the animation

# Function to calculate the tidal bulge height
def tidal_bulge_height(angle):
    return amplitude *1#*np.sin(angle)

# Function to calculate the gravitational force between two bodies
def gravitational_force(m1, m2, r):
    return G * m1 * m2 / r**2

# Function to update the plot for each animation frame
def update(frame):
    ax.clear()
    angle = frame *1 * np.pi / num_frames
    kappa=-10+angle*180/np.pi
    x_earth = 0  # Stationary Earth at the center
    y_earth = 0
    x_tidal = orbital_radius * np.cos(angle)
    y_tidal = orbital_radius * np.sin(angle)
    
    # Plot the orbiting central body (e.g., another planet)
    ax.add_patch(plt.Circle((x_tidal, y_tidal), radius_central_body/2,facecolor='b',edgecolor='g'))
    
    # Plot Earth as a stationary central body
    ax.add_patch(plt.Circle((x_earth, y_earth), radius_central_body, facecolor='yellow',edgecolor='orange'))
    
    # Calculate the tidal bulge height and plot the following ellipse
    tidal_height = tidal_bulge_height(angle)
    tidal_semi_major_axis = radius_central_body + tidal_height
    tidal_semi_minor_axis = radius_central_body - tidal_height * 0.8
    tidal_ellipse = Ellipse((x_earth, y_earth), width=tidal_semi_major_axis*2, height=tidal_semi_minor_axis*2, angle=kappa, color='orange',alpha=0.4)
    ax.add_patch(tidal_ellipse)
    
    # Set plot limits and labels
    ax.set_xlim(-orbital_radius * 1.5, orbital_radius * 1.5)
    ax.set_ylim(-orbital_radius * 1.5, orbital_radius * 1.5)
    ax.set_aspect('equal')
    ax.set_title(f'Tidal Bulge Animation (Frame {frame + 1}/{num_frames})')

# Calculate the reduced tidal bulge amplitude (arbitrary scaling for visualization)
amplitude = radius_central_body * 0.2

# Create the figure and axis for the animation
fig, ax = plt.subplots()

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)

# Display the animation
plt.show()

animation.save('tidal_bulge_animation.gif', writer='imagemagick', fps=20)

