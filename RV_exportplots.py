#-------------------------------------------------------------------------------
# Name:        module2
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

obj=app.GetGraphicsBoard()

VIPages=obj.GetContents('*.SetVipage')

for i in VIPages[0]:

   obj.Show(i)

   Page_name=i.loc_name

   File_name=('D:\\Users\\PowerFactory\\%s' %(Page_name))

   obj.WriteWMF(File_name)
