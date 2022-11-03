# basic system and numerical packages
import sys
import numpy as np
import matplotlib.pyplot as plt
import pycraters as pc

# build wrapper and params
exec_location = sys.argv[1]
wrapper = pc.create_wrapper("TRI3DST", exec_location) 
params  = wrapper.create_parameters()

#basic parameter setup
params.beam = "Ar"
params.energy = 1000 #eV
params.angle = None #degrees
params.impacts = 1000 #number of impacts
params.target = [["Si", 1.0]] #target material and fraction of target

# do the simulations
angles = np.linspace(0,80,9)
finedeg = np.linspace(0,90,91)
for aa in angles:
  print("running angle %02d." % (aa))
  params.angle = aa
  wrapper.go(params, save_raw_data=False)

# plot graph of M0
fits  = pc.helpers.linked_PDE_coefficients_1D(wrapper, params, angles, finedeg)
plots = pc.helpers.plot_single_flat_angle_dependence_summary(fits[0])
plt.show()

