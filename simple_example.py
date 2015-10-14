import numpy as np
import matplotlib.pyplot as plt

x  = np.linspace(-2*np.pi, 2*np.pi, 100) 
f1 = np.sin(x)
f2 = np.cos(x)

print x[20]

plt.plot(x, f1, 'darkgreen', linestyle='--', linewidth=3, label='$\sin(x)$') 
plt.plot(x, f2, 'darkmagenta', linestyle='-', linewidth=3, label='$\cos(x)$') 

plt.xlim([-2*np.pi, 2*np.pi])      # x-axis bounds
plt.ylim([-1.5, 1.5])              # y-axis bounds

legend = plt.legend(loc='upper right')

plt.title('Trigonometric functions') 
plt.xlabel('Angle (in radians)')
plt.ylabel('Function')
plt.subplots_adjust(left=0.15)        # prevents overlapping of the y label

plt.show()
