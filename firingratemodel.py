import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Parameters
tau_r = 10 # (ms) how rapidly the firing rate approaches its steady state value for constant synaptic current
gamma = 5 # threshold (Hz) minimum input required to produce a non zero firing rate

# Variables
input_size = 1 # number of neurons on the input layer
output_size = 1 # number of neurons on the output layer
u = [] # input rates (Hz)
W = [] # weight matrix, N_u entries, where w_i > 0 means excitatory and w_i < 0 inhibitory
v = [] # output rates (Hz)

# Time 
dt = 1 # step size (ms)
tmax = 500 # total time (ms)
t = np.arange(0, tmax, dt)
s = np.zeros((len(t), output_size)) # output rates over time for each neuron

# Initialization
u = np.zeros(input_size)
v = np.zeros(output_size)
W = np.ones((output_size, input_size)) 
s[0] = v

# Apply current
u[0] = 20 # Hz

# Time loop: forward Euler method
## tau_r * dv/dt = -1 * v + F(I_s), where F = [I_s-gamma]+ and I_s = W * u
## dv/dt = (-1 * v + max(0, (W*u-gamma)))/tau_r
for k in tqdm(range(len(t) - 1)):
    # Unless we turn off the input, it will keep supplying
    # after 50 ms we stop applying input current
    if t[k] >= 50:
        u[0] = 0
    # Synaptic current is calculated as weighted input rate
    I_s = W @ u 
    f = np.maximum(0, I_s-gamma)
    # Change rate
    dv_dt = (-v + f) / tau_r
    # Euler update
    v = v + dt * dv_dt
    # Store output 
    s[k+1] = v

# Visualization
plt.plot(t, s[:, 0])
plt.xlabel("Time (ms)")
plt.ylabel("Firing rate (Hz)")
plt.show()