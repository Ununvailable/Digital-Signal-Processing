# prompt: animate brownian motion

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generate Brownian motion data
def brownian_motion(n_steps, start=0, end=1):
  """Generates Brownian motion data."""
  x = np.zeros(n_steps + 1)
  for i in range(n_steps):
    x[i + 1] = x[i] + np.random.normal()
  return np.linspace(start, end, n_steps+1), x

# Set the number of steps for the Brownian motion
n_steps = 100

# Generate the Brownian motion data
time, x = brownian_motion(n_steps)

# Create the animation
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 1)
ax.set_ylim(np.min(x) - 0.5, np.max(x) + 0.5)
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title('Brownian Motion')

def animate(i):
    line.set_data(time[:i+1], x[:i+1])
    return line,

ani = FuncAnimation(fig, animate, frames=n_steps+1, interval=50, blit=True)
ani.save('brownian_motion.gif',writer='imagemagick')
plt.show()