#-------------------------------------------------------------------------------
# Name:        Draaien loadflow en weergeven van resultaten
# Purpose:
#
# Author:      766141
#
# Created:     07-04-2016
# Copyright:   (c) 766141 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import powerfactory as pf

# Get PowerFactory application
app = pf.GetApplication()
app.ClearOutputWindow()

# Run load flow
ldf = app.GetFromStudyCase('ComLdf')
ierr = ldf.Execute()

# Get lists of buses and lines
loads = app.GetCalcRelevantObjects('*.ElmLod')
lines = app.GetCalcRelevantObjects('*.ElmLne')



# Print loading on lines
tabel = []
for line in lines:
    if line.outserv == 0:
        loading = round(line.GetAttribute('m:loading'),2)
        tabel.append(loading)
        app.PrintPlain('Loading on line ' + str(line) + ': ' + str(loading) + '%%')



app.PrintPlain(sum(tabel))
app.PrintPlain(loads)


