#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 16:59:47 2023

@author: mayank
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
circle_radius = 0.5
arrow_length = 0.1
orbital_radius = 3  # Increase this value to increase the distance between the arrow and the orbiting circle
orbital_speed = 0.1
num_frames = 200

# Function to calculate the arrow position and direction
def calculate_arrow_position(angle):
    x_arrow = orbital_radius * np.cos(angle)
    y_arrow = orbital_radius * np.sin(angle)
    dx_arrow = -x_arrow  # Arrow points towards the center of the circle
    dy_arrow = -y_arrow
    return x_arrow, y_arrow, dx_arrow, dy_arrow

# Function to update the plot for each animation frame
def update(frame):
    ax.clear()
    angle = frame * orbital_speed

    # Calculate arrow position and direction
    x_arrow, y_arrow, dx_arrow, dy_arrow = calculate_arrow_position(angle)

    # Plot the circle
    circle = plt.Circle((0, 0), circle_radius, fill=True, color='blue')
    ax.add_patch(circle)

    # Plot the arrow
    ax.arrow(x_arrow, y_arrow, dx_arrow / 5, dy_arrow / 5, head_width=0.3, head_length=0.3, fc='red', ec='red',zorder=11)

    # Calculate the position of the circle on top of the arrow
    circle_x = x_arrow + dx_arrow * -0.051
    circle_y = y_arrow + dy_arrow * -0.05

    # Plot the circle on top of the arrow
    circle_on_arrow = plt.Circle((circle_x, circle_y), circle_radius / 1, fill=True, color='green')
    ax.add_patch(circle_on_arrow)

    # Set plot limits and labels
    ax.set_xlim(-orbital_radius * 1.5, orbital_radius * 1.5)
    ax.set_ylim(-orbital_radius * 1.5, orbital_radius * 1.5)
    ax.set_aspect('equal')
    ax.set_title(f'Arrow with Circle Animation (Frame {frame + 1}/{num_frames})')

# Create the figure and axis for the animation
fig, ax = plt.subplots()

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)

# Display the animation
plt.show()

animation.save('tidal_locking_animation.gif', writer='imagemagick', fps=30)

