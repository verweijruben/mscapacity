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

import powerfactory

app=powerfactory.GetApplication()

Ldf=app.GetFromStudyCase('ComLdf')

FoldOperScens=app.GetProjectFolder('scen')

for OperScen in FoldOperScens.GetChildren(1)[0]:

   OperScen.Activate()

   Ldf.Execute()

   app.PrintPlain(i)
