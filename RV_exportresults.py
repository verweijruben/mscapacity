#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      766141
#
# Created:     12-04-2016
# Copyright:   (c) 766141 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
Generic script for an internal Python script in PowerFactory.

The script gets all terminals of usage 'busbar', runs a load-flow, and sorts
the buses on per unit voltage from highest to lowest.

The results are printed to a text path at a user defined path.
"""

import os
import csv
#Below required to get python to run in 15.2
os.environ["PATH"] = r'C:\Program Files\DIgSILENT\PowerFactory 15.2;' + os.environ["PATH"]
import powerfactory as pf

def sort_key(bus):
    '''Returns the bus voltage in per unit to the sorted function'''
    return bus.GetAttribute('m:u')

#def main():
#Get the application
app = pf.GetApplication()

#Clear the output window
app.ClearOutputWindow()

#Get the load-flow command and run it
ldf = app.GetFromStudyCase('ComLdf')
ierr = ldf.Execute()

#Get the buses
buses = app.GetCalcRelevantObjects('*.ElmTerm')

#List for storing the results
buseswithresults = []

for bus in buses:
    if bus.HasAttribute('m:u')[0] and bus.iUsage == 0:
        buseswithresults.append(bus)

#Open a file for printing
#Change the path as desired



filepath = r'S:/Stedin/Techniek/AM/Afdelingen/RM-PM/1.1.10 Werkmappen/Ruben Verweij/Collegas/Osisoft_MS_capaciteit/resultaten/results.txt'

with open(filepath, 'w') as f:
    print('%-20s %15s'%('BusName','Voltage_pu'), file=f)
    for bus in sorted(buseswithresults, key=sort_key, reverse = True):
        voltage = bus.GetAttribute('m:u')
        print('%-20s %15.3f'%(bus.loc_name.replace(" ", ""),  voltage), file = f)




##with open(filepath, 'w') as f:
##    results = csv.writer(f, delimiter='')
##    results.writerow('%-20s %15s' %('Bus Name','Voltage (p.u)'))
##    for bus in sorted(buseswithresults, key=sort_key, reverse = True):
##        voltage = bus.GetAttribute('m:u')
##        results.writerow('%-20s %15.3f' %(bus.loc_name,  voltage))




##with open('eggs.csv', 'wb') as csvfile:
##
##    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
##    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


app.PrintPlain('Wrote results to %s' %(filepath))
#if __name__ == '__main__':
#main()
