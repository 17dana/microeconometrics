import matplotlib

import matplotlib.pyplot as plt
import scipy.stats as ss
import pandas as pd
import numpy as np

from matplotlib.ticker import MaxNLocator

def plot_individual_specific_effects(with_parameters=None):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(-5, 5, 5000)
    pdf = ss.norm.pdf(x, 0, 1)
    ax.plot(x, pdf)
    
    ax.set_xlabel('$\delta$')
    ax.set_ylabel('Density')
    ax.set_xticklabels(['', '', '', 0.5, '', '', ''])
    ax.set_xlim([-3, 3])
    ax.set_ylim([0, 0.5])
    
    ax.yaxis.set_major_locator(MaxNLocator(prune='both'))
    pos = with_parameters
    
    if with_parameters and len(set(pos)) != 1:
        ax.axvline(x=pos[0], linewidth=3, label='ATE', color='red')
        ax.axvline(x=pos[2], linewidth=3, label='ATT', color='orange')
        ax.axvline(x=pos[1], linewidth=3, label='ATC', color='green')
        ax.legend()        
        
    elif with_parameters and len(set(pos)) == 1:
        ax.axvline(x=pos[0], linewidth=3, label='ATE = ATT = ATC', color='red')
        ax.legend()        