import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.style.use(['science', 'notebook', 'grid'])

plt.rc('xtick', labelsize=20)
plt.rc('ytick', labelsize=20)

def CreatePlot( CrossSections, BoltzmannDistribution, Energies, scale ):

    CrossSections = np.asarray( CrossSections )
    BoltzmannDistribution = np.asarray( BoltzmannDistribution )
    Energies = np.asarray( Energies )
    Gamow = CrossSections*BoltzmannDistribution
    
    gs = gridspec.GridSpec(2, 2,height_ratios=[0.7,2])
    ax1 = plt.subplot( gs[0] )
    ax2 = plt.subplot( gs[1] )
    ax3 = plt.subplot( gs[2:] )

    ax1.plot( Energies, CrossSections )
    ax1.set_xlabel( "Energy (keV)", fontsize=13, horizontalalignment='right',
                    x=1.0 )
    ax1.set_ylabel( "Cross Section (b)", fontsize=13,
                    horizontalalignment='right', y=1.0 )
    ax1.set_yscale( "log" )
    ax1.set_xlim( left=-10, right=600 )
    ax1.set_ylim( bottom=1e-24, top=1 )
    ax1.tick_params( axis = 'both', which = 'major', labelsize = 13 )
    
    ax2.plot( Energies, BoltzmannDistribution )
    ax2.set_xlabel( "Energy (keV)", fontsize=13, horizontalalignment='right',
                    x=1.0 )
    ax2.set_ylabel( "Boltzmann", fontsize=13,
                    horizontalalignment='right', y=1.0 )
    ax2.set_yscale( "log" )
    ax2.set_xlim( left=0, right=1000 )
    ax2.tick_params( axis = 'both', which = 'major', labelsize = 13 )
    
    
    ax3.plot( Energies, Gamow )
    ax3.set_xlabel( "Energy (keV)", fontsize=13,
                    horizontalalignment='right', x=1.0 )
    ax3.set_ylabel( "Gamow Window", fontsize=13, horizontalalignment='right',
                    y=1.0 )
    ax3.tick_params( axis = 'both', which = 'major', labelsize=13 )
    ax3.set_xlim( left=0, right=1000 )
    if( scale == "Log" ):
        ax3.set_yscale( "log" )
        ax3.set_ylim( bottom=1e-2 )
    else:
        ax3.set_yscale( "linear" )
        ax3.set_ylim( bottom=0 )

    plt.tight_layout( )
    plt.show( )
