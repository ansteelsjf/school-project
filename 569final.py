# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:22:24 2021

@author: MSI-PC
"""

import SimpleITK as sitk

# A file name that belongs to the series we want to read
file_name = 'Moving_001.dcm'
data_directory = '.'

# Read the file's meta-information without reading bulk pixel data
file_reader = sitk.ImageFileReader()
file_reader.SetFileName(file_name)
file_reader.ReadImageInformation()

# Get the sorted file names, opens all files in the directory and reads the meta-information
# without reading the bulk pixel data
series_ID = file_reader.GetMetaData('0020|000e')
sorted_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(data_directory, series_ID)

# Read the bulk pixel data
img = sitk.ReadImage(sorted_file_names)
sitk.Show(img)
import SimpleITK as sitk
import sys
import os
def command_iteration(method):
    print(f"{method.GetOptimizerIteration():3} = {method.GetMetricValue():10.5f} : {method.GetOptimizerPosition()}")


if len(sys.argv) < 4:
    print("Usage:", sys.argv[0], "<fixedImageFilter> <movingImageFile>",
          "<outputTransformFile>")
    sys.exit(1)
fixed = sitk.ReadImage(sys.argv[1], sitk.sitkFloat32)
#fixedImage3d = sitk.ReadImage('refLung_001.dcm')
#fixedImage2d = sitk.Extract(fixedImage3d, (fixedImage3d.GetWidth(), fixedImage3d.GetHeight(), 0), (0, 0, 0))
#fixed=fixedImage2d
moving = sitk.ReadImage(sys.argv[2], sitk.sitkFloat32)

R = sitk.ImageRegistrationMethod()
R.SetMetricAsMeanSquares()
R.SetOptimizerAsRegularStepGradientDescent(4.0, .01, 200)
R.SetInitialTransform(sitk.TranslationTransform(fixed.GetDimension()))
R.SetInterpolator(sitk.sitkLinear)

R.AddCommand(sitk.sitkIterationEvent, lambda: command_iteration(R))

outTx = R.Execute(fixed, moving)
