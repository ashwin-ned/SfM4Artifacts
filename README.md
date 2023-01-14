
### AI LAB: Computer Vision & NLP Final Project: 3D Reconstruction of Roman Artifacts using SfM
## Author: Ashwin Nedungadi


# Running the code

For a simple two view reconstruction use the two_view_SfM.m script. 
Make sure that the camera parameter files are in the same directory oneplus_cameraParameters.mat and oneplus_estimationErrors.mat
Make sure that the directory for the input images are set correctly and exists. 

# Camera Calibration Data

The camera calibration parameters are already provided with the code. The camera used was a mobile camera of a oneplus 6 with 12 MP and 25mm focal length. 
The camera was calibrated using the MATLAB camera calibrator app using 12 different images of a standard camera calibration checkerboard with 20mm squares. 

# Tuning Parameters for better results 

The parameters of the feature detection and matching commands can be tuned for better results i.e. using more octaves, more number of points (selectStrongest) etc. 
MATLAB offers different feature matching algorithms, SURF is used here but others can be used.
Region of Interest can also be used to better detect more features in the object and not the background. 

# Datasets

For reconstructing an object, make sure to take pictures of the object with slight overlap between the consecutive images. Since the algorithm used is an Incremental SfM, the order of the images matter for obtaining the final product. 

some example datasets from Rome is provided in the datasets folder.

# Using the Multi-View SfM Script

In the multi_view_SfM folder there are scripts for performing incermental Multi-View SfM using multiple images. The results from this script however, does not restlt in a colored pointcloud. 


# Output

The output will be saved as an "output.ply" file. This can be changed in the last section of the script.
The final pointcloud is obtained by performing two_view_SfM on all the image pairs and then aligning and stitching the results since the two_view_SfM algorithm only results in partial pointclouds.
