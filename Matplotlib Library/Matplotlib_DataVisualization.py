'''
This script provides simple examples to data visualization using Python Matplotlib library.
For more details, see: https://matplotlib.org/
'''

import matplotlib.pyplot as plt
import numpy as npy

## Createa simple figure ##

x = npy.linspace(0, 2*npy.pi, 1000)
y1 = npy.sin(x)

plt.plot(x,y1)

# We can set title, xlabel, and ylabel simply as follows:
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Figure of f(x) = sin(x)')
plt.show()

# ---------------------------------------

# Curve color and type can be edited:
y2 = npy.cos(x)
plt.figure(2) # To create a new figure
plt.plot(x,y2, '--m')

# We can set title, xlabel, and ylabel simply as follows:
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title('Figure of f(x) = cos(x)')
plt.show()
# ---------------------------------------

## Creating multi-panel(subplot) figures ##
plt.figure(3)
plt.subplot(1,2,1)
plt.plot(x,y1)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Figure of f(x) = sin(x)')

plt.subplot(1,2,2)
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title('Figure of f(x) = cos(x)')
plt.plot(x,y2, '--m')

plt.show()
# ---------------------------------------

## Creating figures using figure objects ##

# Using figure objects, we have more freedom on the figures and we can create more personal figures.

fig = plt.figure(4) # This is an empty panel.

# We need to add axes to the panel on which the curve will be plotted.
ax = fig.add_axes([0.1, 0.1, 0.75, 0.75]) # The list that we pass specifies the size of the axes in the format: [left, bottom, width, height] in range 0 to 1.

y3 = x ** 2
ax.plot(x,y3,'-.r')

# The title, xlabel and ylabel can be added as follows:
ax.set_xlabel('x')
ax.set_ylabel('y = $x^2$')
ax.set_title('Figure of f(x) = $x^2$')
plt.show()
# ---------------------------------------

# More complex example:

# The figure size can be edited when creating figure object as well:
fig = plt.figure(5, figsize = (12, 6))

ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.2, 0.5, 0.3, 0.3])
ax3 = fig.add_axes([0.65, 0.2, 0.2, 0.2])

ax1.plot(x,y3, '-.r')
ax1.set_xlabel('x')
ax1.set_ylabel('y = $x^2$')
ax1.set_title('Multi-panel custom figure')

ax2.plot(x,y1)
ax2.set_xlabel('x')
ax2.set_ylabel('sin(x)')
ax2.set_title('Figure of f(x) = sin(x)')

ax3.plot(x,y2, '--m', linewidth = 2)
ax3.set_xlabel('x')
ax3.set_ylabel('cos(x)')
ax3.set_title('Figure of f(x) = cos(x)')

plt.show()

# ---------------------------------------

## Multiple curves can be plotted on the same axes ##

fig = plt.figure(6, figsize = (8,6))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, x, 'y')
ax.plot(x, x**(1/2), 'b')
ax.plot(x, x**(1/3), 'r')
ax.plot(x, x**(1/4), 'k')
ax.plot(x, x**(1/5), 'g')
ax.legend(['y = $x$', 'y = $x^{1/2}$', 'y = $x^{1/3}$', 'y = $x^{1/4}$', 'y = $x^{1/5}$']) # adds legend for the curves
ax.set_title('Multiple Curves')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# The location of the legends can be specified using .legend(loc = 1) for northeast of the panel
# loc = 2 --> for northwest of the panel
# loc = 3 --> for southeast of the panel
# loc = 4 --> for southwest of the panel

plt.show()

# ---------------------------------------

## Matplotlib.pyplot has built-in special plot functions ##
randData = npy.random.randn(1000)

# Histogram Plot #
plt.figure(7)
plt.hist(randData, bins = 50)

plt.title('Histogram Plot')
plt.show()

# Scatter Plot #
randData = npy.random.randn(2,1000)

plt.figure(8)
plt.scatter(x = randData[0,:], y = randData[1,:])

plt.title('Scatter Plot')
plt.show()

# Box Plot #

plt.figure(9)
plt.boxplot(randData.transpose())

plt.title('Box Plot')
plt.show()

# Violin Plot #

plt.figure(10)
plt.violinplot(randData.transpose())

plt.title('Violin Plot')
plt.show()

# For more examples for other plot types, see: https://matplotlib.org/gallery/index.html