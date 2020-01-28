#!/usr/bin/python

# e.g. python cut_ray.py /Volumes/DATA_disk/Frontera_run/SW_test/RUN_34/GM

import sys
import os
import glob

dir = sys.argv[1]
command = "ls " + dir + "/cut_ray*.plt > file.txt"
os.system("rm -f file.txt")
os.system(command)
file = []
with open('file.txt') as f:
    for line in f:
        file.append(line.rstrip())

x = ''
for name in file:
    x = x + '"' + name + '" '

os.system('rm -f cut_ray.mcr')
os.system('touch cut_ray.mcr')
f = open('cut_ray.mcr','a')
f.write('#!MC 1410\n')
f.write('''$!ReadDataSet  \'''' + x + '''\'''')
f.write('''
  ReadDataOption = New
  ResetStyle = No
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '"X" "Y" "Z" "B_x" "B_y" "B_z" "theta_1" "phi_1" "theta_2" "phi_2" "Status" "Block #"'
$!PlotType = Cartesian3D
$!ThreeDView ViewerPosition{X = 0}
$!ThreeDView ViewerPosition{Y = 0}
$!ThreeDView ViewerPosition{Z = 21.2007066058843208}
$!ThreeDView PSIAngle = 0
$!ThreeDView ThetaAngle = 0
$!ThreeDView ViewerPosition{X = 15.9005299544132335}
$!ThreeDView ViewerPosition{Y = 9.18017524943820007}
$!ThreeDView ViewerPosition{Z = 10.6003533029421622}
$!ThreeDView PSIAngle = 59.9999999999999929
$!ThreeDView ThetaAngle = 239.999999999999972
$!FieldLayers ShowShade = No
$!FieldLayers UseLightingEffect = No
$!SetContourVar 
  Var = 4
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 5
  ContourGroup = 8
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 6
  ContourGroup = 7
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 7
  ContourGroup = 6
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 8
  ContourGroup = 5
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 9
  ContourGroup = 4
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 10
  ContourGroup = 3
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 11
  ContourGroup = 2
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 3
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 2
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 1
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 11
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!ContourLevels New
  ContourGroup = 1
  RawData
7
-3
-2
-1
0
1
2
3
$!GlobalContour 1  ColorMapName = 'Small Rainbow'
$!GlobalRGB RedChannelVar = 4
$!GlobalRGB GreenChannelVar = 4
$!GlobalRGB BlueChannelVar = 4
$!FieldLayers ShowContour = Yes
$!FieldLayers ShowMesh = Yes
$!RedrawAll 
$!ActiveFieldMaps = [2]
$!RedrawAll 
$!ActiveFieldMaps = [3]
$!RedrawAll 
$!ActiveFieldMaps = [4]
$!RedrawAll 
$!ActiveFieldMaps = [3]
$!ActiveFieldMaps = [2]
$!ActiveFieldMaps = [1]
$!ActiveFieldMaps = [2]
$!ActiveFieldMaps = [3]
$!ActiveFieldMaps = [4]
$!GlobalThreeD RotateOrigin{X = 0}
$!GlobalThreeD RotateOrigin{Y = 0}
$!GlobalThreeD RotateOrigin{Z = 0}
$!View Fit
  ConsiderBlanking = Yes
$!Pick SetMouseMode
  MouseMode = Select
$!RedrawAll
''')
f.close()

os.system('tec360 cut_ray.mcr')
