#Lorenz
from manim import *
import numpy as np

class LorenzAttractor(Scene):
    def construct(self):
        # Parameters
        sigma = 10
        rho = 28
        beta = 8/3

        # Initial conditions
        x0, y0, z0 = 0, 1, 20

        # Time step and duration
        dt = 0.01
        duration = 10  # in seconds

        # Calculate number of steps
        steps = int(duration / dt)

        # Initialize lists to store x, y, z coordinates
        x_coords, y_coords, z_coords = [x0], [y0], [z0]

        # Run simulation
        for _ in range(steps):
            dx = sigma * (y_coords[-1] - x_coords[-1]) * dt
            dy = (x_coords[-1] * (rho - z_coords[-1]) - y_coords[-1]) * dt
            dz = (x_coords[-1] * y_coords[-1] - beta * z_coords[-1]) * dt

            x_coords.append(x_coords[-1] + dx)
            y_coords.append(y_coords[-1] + dy)
            z_coords.append(z_coords[-1] + dz)

        # Create points from the coordinates
        points = VGroup(*[Dot(point=np.array([x, y, z]), radius=0.01, color=BLUE) for x, y, z in zip(x_coords, y_coords, z_coords)])

        # Draw the attractor
        self.add(points)
        self.wait(duration)

# Preview the scene
if __name__ == "__main__":
    LorenzAttractor().render()
