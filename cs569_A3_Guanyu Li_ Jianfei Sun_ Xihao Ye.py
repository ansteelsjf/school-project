"""
CAI, Assignement 3
"""
# Import the library (5 points)
import SimpleITK as sitk
import sys




# Check that the right number of arguments were entered (5 points)
print(sys.argv)
if len(sys.argv) !=3 :
    print('Usage: ' + sys.argv[0] + '<InputFilname><OutputFilname>')
    sys.exit(1)
        
# Extract the command-line arguments passed to the script (5 points)
inputFilename = sys.argv[1]
outputFilename = sys.argv[2]

# Read the image (5 points)
image = sitk.ReadImage(inputFilename, sitk.sitkFloat32)
#sitk.Show(image)

# Preprocess image. Smooth image using CurvatureAnisotropicDiffusionImageFilter (20 points)

smoothing = sitk.CurvatureAnisotropicDiffusionImageFilter()
smoothingOutput = smoothing.Execute(image)
#sitk.Show(smoothingOutput)

# Segmentation. Use IsolatedConnectedImageFilter (20 points)
segmentation = sitk.IsolatedConnectedImageFilter()
segmentation.SetSeed1([111, 154])
segmentation.SetSeed2([154, 304])
segmentation.SetLower(80)
segmentation.SetUpper(180)
segmentation.SetReplaceValue(245)  
isolatedimage = segmentation.Execute(smoothingOutput) 

sitk.Show(isolatedimage)

#  Write out the segmentation image (5 points)
writer = sitk.ImageFileWriter()
writer.SetFileName(outputFilename)
writer.Execute(isolatedimage)