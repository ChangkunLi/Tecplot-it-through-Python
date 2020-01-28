#!/usr/bin/python

# e.g. python movie.py /Volumes/DATA_disk/Mercury_run/run_22/RESULTS_22/run_22/GM

# The location of Shue.dat or Zhong.dat should be set as input in the future

import sys
import os
import glob

dir = sys.argv[1]
dir_mp = sys.argv[2]
command = "ls " + dir + "/3d*plt > file.txt"
os.system("rm -f file.txt")
os.system(command)
file = []
with open('file.txt') as f:
    for line in f:
        file.append(line.rstrip())

count = 0
for x in file:
    count = count + 1
    os.system('touch plot.mcr')
    f = open('plot.mcr','a')
    f.write('#!MC 1410\n')
    f.write('''$!ReadDataSet  \'"''' + x + '''"\'''')
    f.write('''
  ReadDataOption = New
  ResetStyle = Yes
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '"X [R]" "Y [R]" "Z [R]" "Rho [amu/cm^3]" "U_x [km/s]" "U_y [km/s]" "U_z [km/s]" "B1_x [nT]" "B1_y [nT]" "B1_z [nT]" "B_x [nT]" "B_y [nT]" "B_z [nT]" "P [nPa]" "eta" "J_x [`mA/m^2]" "J_y [`mA/m^2]" "J_z [`mA/m^2]" "dt [s]" "dtblk [s]" "cons" "impl" "dx [R]" "Status"'
$!FieldLayers ShowShade = No
$!SetContourVar 
  Var = 4
  ContourGroup = 1
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 5
  ContourGroup = 2
  LevelInitMode = ResetToNice
$!ContourLevels New
  ContourGroup = 1
  RawData
14
0
12.3076923077
24.6153846154
36.9230769231
49.2307692308
61.5384615385
73.8461538462
86.1538461538
98.4615384615
110.769230769
123.076923077
135.384615385
147.692307692
160
$!GlobalContour 1  ColorMapName = 'Small Rainbow'
$!GlobalRGB RedChannelVar = 4
$!GlobalRGB GreenChannelVar = 4
$!GlobalRGB BlueChannelVar = 8
$!SetContourVar 
  Var = 6
  ContourGroup = 3
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 7
  ContourGroup = 4
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 8
  ContourGroup = 5
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 9
  ContourGroup = 6
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 10
  ContourGroup = 7
  LevelInitMode = ResetToNice
$!SetContourVar 
  Var = 11
  ContourGroup = 8
  LevelInitMode = ResetToNice
$!SliceLayers Show = Yes
$!SliceAttributes 1  SliceSurface = YPlanes
$!RedrawAll 
$!View Zoom
  X1 = -2.41491068782
  Y1 = -8.00733543857
  X2 = 3.43171518796
  Y2 = 8.76993881368
$!Pick SetMouseMode
  MouseMode = Select
$!ThreeDView ViewerPosition{X = 0.508402250068115791}
$!ThreeDView ViewerPosition{Y = -1615.69219381652988}
$!ThreeDView ViewerPosition{Z = 0.381301687551271029}
$!ThreeDView PSIAngle = 90
$!ThreeDView ThetaAngle = 0
$!ThreeDView ViewerPosition{X = 1615.69219381652988}
$!ThreeDView ViewerPosition{Y = 0.50840225006801687}
$!ThreeDView ThetaAngle = -90
$!RedrawAll 
$!ThreeDView ViewerPosition{X = 0.508402250068115791}
$!ThreeDView ViewerPosition{Y = -1615.69219381652988}
$!ThreeDView ThetaAngle = 0
$!RedrawAll 
$!View Zoom
  X1 = -2.89007125231
  Y1 = -3.17203896177
  X2 = 2.42703412609
  Y2 = 2.9538170729
$!Pick SetMouseMode
  MouseMode = Select
$!ThreeDView 
  ViewerPosition
    {
    X = 0.8554281999663685
    Y = -1615.69219381653
    Z = -0.02743286397538285
    }
  ViewWidth = 6.89159
$!ThreeDView 
  ViewerPosition
    {
    X = 0.6166768878459609
    Y = -1615.69219381653
    Z = 0.02283057015522928
    }
  ViewWidth = 6.89159
$!ThreeDView 
  ViewerPosition
    {
    X = 0.534998807383716
    Y = -1615.69219381653
    Z = 0.01654764088890277
    }
  ViewWidth = 6.89159
$!Pick SetMouseMode
  MouseMode = Select
$!IsoSurfaceLayers Show = Yes
$!IsoSurfaceAttributes 2  DefinitionContourGroup = 1
$!IsoSurfaceAttributes 2  DefinitionContourGroup = 2
$!IsoSurfaceAttributes 2  DefinitionContourGroup = 3
$!IsoSurfaceAttributes 2  DefinitionContourGroup = 4
$!IsoSurfaceAttributes 2  DefinitionContourGroup = 5
$!IsoSurfaceAttributes 2  DefinitionContourGroup = 6
$!IsoSurfaceAttributes 1  ShowGroup = No
$!IsoSurfaceAttributes 1  ShowGroup = Yes
$!IsoSurfaceAttributes 1  ShowGroup = No
$!IsoSurfaceAttributes 2  ShowGroup = Yes
$!SetContourVar 
  Var = 11
  ContourGroup = 2
  LevelInitMode = ResetToNice
$!ContourLevels New
  ContourGroup = 2
  RawData
51
-50
-48
-46
-44
-42
-40
-38
-36
-34
-32
-30
-28
-26
-24
-22
-20
-18
-16
-14
-12
-10
-8
-6
-4
-2
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
$!GlobalContour 2  ColorMapName = 'Diverging - Blue/Red'
$!IsoSurfaceAttributes 2  DefinitionContourGroup = 2
$!SetContourVar 
  Var = 13
  ContourGroup = 3
  LevelInitMode = ResetToNice
$!IsoSurfaceAttributes 2  DefinitionContourGroup = 3
$!IsoSurfaceAttributes 2  Isovalue1 = 0
$!RedrawAll 
$!Pick AddAtPosition
  X = 9.17179487179
  Y = 6.1741025641
  ConsiderStyle = Yes
$!GlobalContour 2  Labels{AutoLevelSkip = 2}
$!GlobalContour 2  Labels{AutoLevelSkip = 3}
$!GlobalContour 2  Labels{AutoLevelSkip = 4}
$!GlobalContour 2  Labels{AutoLevelSkip = 5}
$!RedrawAll 
$!Pick Shift
  X = 0.106666666667
  Y = 3.74974358974
$!Pick AddAtPosition
  X = 8.24461538462
  Y = 4.72179487179
  ConsiderStyle = Yes
$!Pick Shift
  X = 0.0328205128205
  Y = -0.607179487179
$!Pick AddAtPosition
  X = 9.55743589744
  Y = 5.24692307692
  ConsiderStyle = Yes
$!Pick AddAtPosition
  X = 9.58205128205
  Y = 5.26333333333
  ConsiderStyle = Yes
$!Pick DeselectAll
$!Pick AddAllInRect
  SelectText = Yes
  SelectGeoms = Yes
  SelectZones = Yes
  ConsiderStyle = Yes
  X1 = 9.29487179487
  X2 = 9.36871794872
  Y1 = 6.09205128205
  Y2 = 6.36282051282
$!Pick AddAtPosition
  X = 9.03230769231
  Y = 6.35461538462
  ConsiderStyle = Yes
$!Pick Shift
  X = 0.0738461538462
  Y = -0.328205128205
$!RedrawAll 
$!Pick AddAtPosition
  X = 8.53179487179
  Y = 5.79666666667
  ConsiderStyle = Yes
$!ThreeDView 
  PSIAngle = 85.8974
  ThetaAngle = -90.2564
  AlphaAngle = 4.57296E-51
  ViewerPosition
    {
    X = 1611.532399833938
    Y = 7.746987279830398
    Z = 115.6064882728055
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 89.6718
  ThetaAngle = -138.338
  AlphaAngle = 4.57285E-51
  ViewerPosition
    {
    X = 1073.580085361296
    Y = 1207.39446303646
    Z = 9.271601897351571
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 80.6462
  ThetaAngle = -102.072
  AlphaAngle = 4.57065E-51
  ViewerPosition
    {
    X = 1558.840626279187
    Y = 333.9310132230486
    Z = 262.6167015377181
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 75.3949
  ThetaAngle = -55.1385
  AlphaAngle = 4.17035E-20
  ViewerPosition
    {
    X = 1283.196662604265
    Y = -893.2383927712511
    Z = 407.4224471208195
    }
  ViewWidth = 6.89159
$!Pick SetMouseMode
  MouseMode = Select''')
    f.write('''
$!ReadDataSet  '"''' + dir_mp + '''/Shue.dat" ' ''')
    f.write(''' 
  ReadDataOption = Append
  ResetStyle = No
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '"X [R]" "Y [R]" "Z [R]" "Rho [amu/cm^3]" "U_x [km/s]" "U_y [km/s]" "U_z [km/s]" "B1_x [nT]" "B1_y [nT]" "B1_z [nT]" "B_x [nT]" "B_y [nT]" "B_z [nT]" "P [nPa]" "eta" "J_x [`mA/m^2]" "J_y [`mA/m^2]" "J_z [`mA/m^2]" "dt [s]" "dtblk [s]" "cons" "impl" "dx [R]" "Status" "MP_Nx" "MP_Ny" "MP_Nz"'
$!FieldLayers ShowMesh = Yes
$!FieldLayers ShowMesh = No
$!FieldLayers ShowMesh = Yes
$!FieldLayers ShowContour = Yes
$!LinearInterpolate 
  SourceZones =  [1]
  DestinationZone = 2
  VarList =  [6-14,16-18]
  LinearInterPConst = 0
  LinearInterpMode = DontChange
$!AlterData  [2]
  Equation = '{Bn} = V11*V25 + V12*V26 + V13*V27'
$!FieldMap [1]  Contour{Show = No}
$!FieldMap [1]  Contour{Show = Yes}
$!SetContourVar 
  Var = 28
  ContourGroup = 4
  LevelInitMode = ResetToNice
$!ContourLevels New
  ContourGroup = 4
  RawData
26
-50
-46
-42
-38
-34
-30
-26
-22
-18
-14
-10
-6
-2
2
6
10
14
18
22
26
30
34
38
42
46
50
$!GlobalContour 4  ColorMapName = 'Small Rainbow'
$!GlobalContour 4  Labels{AutoLevelSkip = 2}
$!GlobalContour 4  Labels{AutoLevelSkip = 3}
$!GlobalContour 4  Labels{AutoLevelSkip = 4}
$!RedrawAll 
$!FieldMap [2]  Contour{FloodColoring = Group4}
$!RedrawAll 
$!ThreeDView 
  PSIAngle = 93.2821
  ThetaAngle = -109.949
  AlphaAngle = 4.17035E-20
  ViewerPosition
    {
    X = 1516.075332869836
    Y = 550.8392328084076
    Z = -92.48392465656833
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 74.0821
  ThetaAngle = -161.477
  AlphaAngle = 4.16691E-20
  ViewerPosition
    {
    X = 493.0933720140661
    Y = 1473.414597621916
    Z = 443.1364368314453
    }
  ViewWidth = 6.89159
$!Pick SetMouseMode
  MouseMode = Select
$!FieldLayers UseTranslucency = Yes
$!ThreeDView 
  PSIAngle = 88.8513
  ThetaAngle = -120.123
  AlphaAngle = 4.16732E-20
  ViewerPosition
    {
    X = 1396.94228674017
    Y = 811.1495360435247
    Z = 32.40724225765221
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 89.5077
  ThetaAngle = -85.6615
  AlphaAngle = 4.16739E-20
  ViewerPosition
    {
    X = 1611.04341093311
    Y = -121.6860575510371
    Z = 13.89903392015465
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 84.7487
  ThetaAngle = -114.544
  AlphaAngle = 4.16739E-20
  ViewerPosition
    {
    X = 1463.315012463721
    Y = 668.8041557202733
    Z = 147.8909302385162
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 83.7641
  ThetaAngle = -113.559
  ViewerPosition
    {
    X = 1472.0443474109
    Y = 642.4491835753514
    Z = 175.516487647702
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 93.2821
  ThetaAngle = -167.549
  ViewerPosition
    {
    X = 347.2648398361113
    Y = 1575.219161371174
    Z = -92.48392465656904
    }
  ViewWidth = 6.89159
$!Pick SetMouseMode
  MouseMode = Select
$!SliceAttributes 1  Effects{UseTranslucency = Yes}
$!SliceAttributes 1  Effects{SurfaceTranslucency = 40}
$!RedrawAll 
$!ThreeDView 
  PSIAngle = 87.3469
  ThetaAngle = -167.556
  AlphaAngle = -1.30948
  ViewerPosition
    {
    X = 347.2648398361113
    Y = 1576.157069978242
    Z = 74.81693276517741
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 95.979
  ThetaAngle = -167.5
  AlphaAngle = 0.598574
  ViewerPosition
    {
    X = 347.2648398361113
    Y = 1568.932365380146
    Z = -168.2852207813977
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 73.2771
  ThetaAngle = -167.011
  AlphaAngle = -4.52151
  ViewerPosition
    {
    X = 347.2648398361113
    Y = 1507.872477568171
    Z = 464.9615834272871
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 73.0292
  ThetaAngle = -166.994
  AlphaAngle = -4.58129
  ViewerPosition
    {
    X = 347.2648398361113
    Y = 1505.79325870794
    Z = 471.6517197048142
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 86.6497
  ThetaAngle = -162.235
  AlphaAngle = -4.58129
  ViewerPosition
    {
    X = 491.6236270825777
    Y = 1536.177466975931
    Z = 94.48042605092161
    }
  ViewWidth = 6.89159
$!Pick SetMouseMode
  MouseMode = Select
$!ThreeDView 
  PSIAngle = 75.9831
  ThetaAngle = -98.2348
  AlphaAngle = -4.58129
  ViewerPosition
    {
    X = 1551.330259999873
    Y = 225.0507955189239
    Z = 391.3925337844462
    }
  ViewWidth = 6.89159
$!ThreeDView 
  PSIAngle = 84.8446
  ThetaAngle = -87.24
  AlphaAngle = -4.58129
  ViewerPosition
    {
    X = 1607.309760745933
    Y = -76.95392188516922
    Z = 145.2411049757476
    }
  ViewWidth = 6.89159
$!Pick SetMouseMode
  MouseMode = Select
$!SliceLayers Show = No
$!RedrawAll 
$!IsoSurfaceLayers Show = No
$!RedrawAll 
$!FieldLayers UseLightingEffect = No
$!RedrawAll 
$!IsoSurfaceLayers Show = Yes
$!SliceLayers Show = Yes
$!RedrawAll 
$!ThreeDView 
  PSIAngle = 84.3523
  ThetaAngle = -130.563
  ViewerPosition
    {
    X = 1221.117961702455
    Y = 1045.959725570684
    Z = 159.0620248487265
    }
  ViewWidth = 6.89159
$!Pick SetMouseMode
  MouseMode = Select
$!Pick AddAtPosition
  X = 9.3441025641
  Y = 2.82641025641
  ConsiderStyle = Yes
$!Pick Shift
  X = -1.05846153846
  Y = 3.74153846154
$!Pick AddAtPosition
  X = 7.85897435897
  Y = 3.72076923077
  CollectingObjectsMode = HomogeneousAdd
  ConsiderStyle = Yes
$!RedrawAll 
$!GlobalContour 4  ColorMapName = 'Small Rainbow'
$!RedrawAll 
$!IsoSurfaceLayers Show = No
$!RedrawAll 
$!ThreeDView 
  PSIAngle = 84.8446
  ThetaAngle = -132.532
  AlphaAngle = -4.58129
  ViewerPosition
    {
    X = 1185.418085069084
    Y = 1088.186811477628
    Z = 145.2411049757483
    }
  ViewWidth = 6.89159
$!Pick SetMouseMode
  MouseMode = Select
$!FieldMap [2]  Effects{SurfaceTranslucency = 20}
$!RedrawAll 
$!FieldMap [2]  Effects{SurfaceTranslucency = 30}
$!RedrawAll 
$!ThreeDView 
  PSIAngle = 82.3831
  ThetaAngle = -150.255
  AlphaAngle = -4.58129
  ViewerPosition
    {
    X = 794.0631026148451
    Y = 1390.696212223267
    Z = 214.2180805414563
    }
  ViewWidth = 6.89159
$!Pick SetMouseMode
  MouseMode = Select
$!ThreeDView ViewerPosition{X = 1615.69219042466329}
$!ThreeDView ViewerPosition{Y = 0.545127708364242292}
$!ThreeDView ViewerPosition{Z = 0.0171422471705411396}
$!ThreeDView PSIAngle = 90
$!ThreeDView ThetaAngle = -90
$!ThreeDView AlphaAngle = 0
$!RedrawAll 
$!PrintSetup Palette = Color
$!ExportSetup ImageWidth = 1096
$!ExportSetup UseSuperSampleAntiAliasing = Yes
$!ExportSetup SuperSampleFactor = 5
''')
    f.write("$!ExportSetup ExportFName = '" + dir_mp  + "/%04d.png'" % count)
    f.write('''
$!Export 
  ExportRegion = AllFrames
''')
    f.close()
    os.system('tec360 -b plot.mcr')
    command = "mv plot.mcr plot" + str(count) + ".mcr"
    os.system(command)
    #os.system('rm -f plot.mcr')         


