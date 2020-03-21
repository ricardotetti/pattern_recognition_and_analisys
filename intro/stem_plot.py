import matplotlib.pyplot as plot
import numpy as np
import pylab
# marks obtained by students in an examination
marks = [10,11,22,24,35,37,45,47,48,58,56,59,61,71,81,92,95]
# corresponding stems
stems = [1,1,2,2,3,3,4,4,4,5,5,5,6,7,8,9,9]
# set the x axis and y axis limits
pylab.xlim([0,10])
pylab.ylim([0,100])
# Provide a title for the stem plot
plot.title('Stem Plot(Stem and Leaf Plot)')
# Give x axis label for the stem plot
plot.xlabel('Range/Stems')
# Give y axis label for the stem plot
plot.ylabel('Marks obtained/Leafs')
# plot the stem plot using matplotlib
markerline, stemlines, baseline = plot.stem(stems, marks, '-.')
# display the stem plot
plot.show()
