#-------------------------------------------------------------------------------
# Name:        module1
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

# Import
imp = app.GetFromStudyCase('ComExport')

