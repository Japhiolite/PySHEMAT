'''Simple example to determine the temperature gradient in one geological formation in the model

Created on Jun 8, 2012
@author: JFW
'''

import PySHEMAT as PS

# this is a simple output file in the example folder, change to whatever your file is;
# if you want to change to another directory, use:
# import os
# os.chdir(r'C:\Path\to\directory\')
S1 = PS.Shemat_file(filename='temp_gradient.nlo')

# formation id
formation_id = 2

# determine 
temp_grad_xy = S1.calc_formation_temp_gradient(formation_id)

# now create a 2-D map of gradients for this formation
#
# if you want to have contours as well, uncomment the contour keyword
# for a list of possible colormaps, see:
# http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps
S1.create_2D_property_plot(temp_grad_xy,
                           savefig = True,
                           interpolation = 'nearest',
                           cmap = 'YlOrRd',
#                           contour = True,
                           filename = 'temp_gradient_fomration_%d' % formation_id,
                           title = 'Temperature gradient of formation %d' % formation_id,
                           xscale = 'kilometer',
                           yscale = 'kilometer',
                           xlabel = 'E-W [km]',
                           ylabel = 'N-S [km]',
                           colorbar = True)

