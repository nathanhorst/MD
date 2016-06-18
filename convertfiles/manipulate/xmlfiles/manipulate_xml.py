# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os
import sys
from math import sqrt

###########################################################################
### This function simply copies an xml file, and renames the particle types
###########################################################################

def rename_particles_xml(save,read,newname,oldname):
    
    fid = open(save,'w')
    inputfile = open(read,'r')
    fdata=inputfile.read()
    data=fdata.splitlines()

    for line in data:
        if line.startswith(oldname):    
            fid.write(('%s \n')%(newname))
        else:
            fid.write(('%s \n')%(line))

##################################################################
### This function simply copies an xml file, and renames the bonds
##################################################################

def rename_bonds_xml(save,read,newname,oldname):
    
    fid = open(save,'w')
    inputfile = open(read,'r')
    fdata=inputfile.read()
    data=fdata.splitlines()

    for line in data:
        if line.startswith(oldname):
            s=line.split()
            fid.write(('%s %s %s \n')%(newname,s[1],s[2]))
        else:
            fid.write(('%s \n')%(line))

###################################################################
### This function simply copies an xml file, and renames the angles
###################################################################

def rename_angles_xml(save,read,newname,oldname):
    
    fid = open(save,'w')
    inputfile = open(read,'r')
    fdata=inputfile.read()
    data=fdata.splitlines()

    for line in data:
        if line.startswith(oldname):
            s=line.split()
            fid.write(('%s %s %s %s \n')%(newname,s[1],s[2],s[3]))
        else:
            fid.write(('%s \n')%(line))
            
##############################################################################
### This function shifts the positions of xyz files in the x y or z directions
##############################################################################

#### THIS FUNCTION DOES NOT CURRENTLY WORK AND IS NOT FINISHED

def shift_xml(save,read,shiftx,shifty,shiftz,npart):


    #Open input file for reading in xml format

    fin=open(read,'r')
    fdata=fin.read()
    data=fdata.splitlines()

    #Open output file for writing in xml format

    fout=open(save,'w')

    for line in data:
        s=line.split()
        if line.startswith('<position>'):
            for line, i in range(npart-1):
                x=float(s[0])+shiftx
                y=float(s[1])+shifty
                z=float(s[2])+shiftz
                fout.write(("%s %f %f %f\n")%(x,y,z))

##########################
### Example run script ###
##########################
"""        
import os
import sys

import manipulate_xml as m

save='newname.xml'
read='tetra.xml'
newname='Au'
oldname='C'

m.rename_particles_xml(save,read,newname,oldname)
"""
