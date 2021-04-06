import numpy as np
from matplotlib import pyplot

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)

np_city = np.column_stack((height, weight))

xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'
pyplot.title(title)
pyplot.xlabel(xlab)
pyplot.ylabel(ylab)

# logarithmic scale
pyplot.xscale('log')

col = {
    'Asia': 'red',
    'Europe': 'green',
    'Africa': 'blue',
    'Americas': 'yellow',
    'Oceania': 'black'
}

# Additional customizations
pyplot.text(1550, 71, 'India', withdash=True)
pyplot.text(5700, 80, 'China', withdash=True)

# scatter plot, use s kwarg to increase the size of the dots, alpha sets the opacity, c sets the color of the dots
pyplot.scatter(height, weight, s=np_city * 2, alpha=0.8)

# adds a grid
pyplot.grid(True)

# ticks
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
pyplot.xticks(tick_val, tick_lab)
pyplot.show()
