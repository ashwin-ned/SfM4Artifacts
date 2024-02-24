import os
import numpy as np
import cv2
import open3d


def dataloader(path):
    images = list()
    for filename in os.listdir(path):
        print(f"Reading file {filename}")
        if filename.endswith(".jpg" or ".png"):
            image = cv2.imread(os.path.join(path, filename))
            images.append(image) 
            resized_image = cv2.resize(image, (500, 500), interpolation = cv2.INTER_AREA)

            cv2.imshow('image', resized_image)
            cv2.waitKey(0)        
   
    print(f"Loaded {len(images)} images")
    
    return images 


if __name__ ==  "__main__":
    # Load Data
    images = 'C:/Users/Ashwin/Desktop/SfM Project/Sfm4Artifacts/datasets/laocoon/'
    output = 'C:/Users/Ashwin/Desktop/SfM Project/Sfm4Artifacts/outputs/'

    # Run the preprocessing pipeline

    # Run the COLMAP Reconstruction Pipeline 

    # Extract Features
  