# Bayena_task
  This is repo is meant to create a classification model starting from predectings the masks through yolo8-seg and use these masks to train a nn-unet and use its prediction for the classification.

  This repo also contains 5 main notebooks in which you only need you specify the paths to your owns path following the data structure of Frac_Atlas dataset.
  
## a Walk through notebooks:

  # S2_bayena_Yolo_to_mask.ipynb
  this notebook takes the images from the fracatlas and gives you an output of full res images and full res masks for all the data, hence the non fractured masks are just black images as it doesnt have any segmentations or labels.

  Just add your own paths and you are ready to go.

  # S3_Bayena_Data_splitting_preprocessing_for_nnunet.ipynb
  this one is meant to to preprocess the full res outputs from the yolo , resize the images and prepare the data folders and names to work with directly with nn-unet.
    like the previous one, add your paths paths and you are good to go. but also you can skip this one for reason that will be discussed in the next few lines.


  # S4_Bayena_model_Training_for_nnunet.ipynb  
  this notebook take the output from s2 and then process it for nn-unet. and to train nn-unet, all you have to do is to carefully walk throught the notebook starting from # Import basic packages for later use
then you will be able to train a new nn-unet model using a new dataset without having any errors. I picked 1517 images splitted into 717 fractured and 800 non fracture and trained for 50 epochs 5 folds using the "-tr nnUNetTrainer_10epochs" class. 

  I have created this notebook to be a future refrence for this kind of work pipeline in the future and added some links  for furture need.

  # s5_classifcation.ipynb
  now that you have the 224p orginals images and 224p segmented masks, all you have to do is to modifiy the original data frame so that you have the orginal labels and the new images. 
   I have written a full custom generator "class MyGen(Dataset)" that resturns the segmented image array ( the image and the masks combined ) in a format that any deeplearning can use.

  with some modification and parameters changes walking through this notebook, you can modify it to any similar tasks with no issue.

  # s6_Classifier_inference.ipynb
  this is an inference refrence for the classifier as the nn-unet doesnt have any inference code in their docs yet you can run the s4 notebooks starting from the nn-unet part and skip the training cells and run the prediction cell and then you can use the output seperatly.




      
    
