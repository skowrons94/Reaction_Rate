import numpy as np
import matplotlib.pyplot as plt

class Data( ):
    def __init__( self, FileDir, M0, M1, Z0, Z1 ):
        self.FileDir = FileDir
        self.M0 = M0
        self.M1 = M1
        self.Z0 = Z0
        self.Z1 = Z1
        self.ReadData( )

    def ReadData( self ):

        fIn = open( self.FileDir, "r" )

        Lines = fIn.readlines( )
        self.Sfactor = np.zeros( shape=( len( Lines ), 2 ) )

        for idx in range( len( Lines ) ):
            l = Lines[idx].split( )
            self.Sfactor[idx][0] = float( l[0] )
            self.Sfactor[idx][1] = float( l[1] )

        self.CreateGraph( )

        fIn.close( )
        
    def CreateGraph( self ):

        fig = plt.figure( )
        graph = plt.plot( self.Sfactor[:,0], self.Sfactor[:,1] )
        plt.close( fig )

        self.SfactorGraph = [graph[0].get_xdata( ), graph[0].get_ydata( )]

    def GetSfactorValue( self, Energy ):

        idx = (np.abs( self.SfactorGraph[0] - Energy )).argmin()
        Sfactor = self.SfactorGraph[1][idx]

        return Sfactor

    def GetCrossValue( self, Energy ):

        Z       = self.Z0*self.Z1
        Mr      = self.M0*self.M1/( self.M0 + self.M1 )
        Sfactor = self.GetSfactorValue( Energy )

        Cross   = Sfactor*np.exp( -0.989534*Z*np.sqrt( Mr/( Energy ) ) )
        Cross  /= Energy

        return Cross
