# PhysicalIQA

Implementing the RoBERTa w. CNQA on the PhysicalIQA dataset with a few modifications.
1. With 5000 instances of training data.
2. Batch size = 2

Link to the Readme.md file of the model used - https://github.com/isi-nlp/ai2/blob/ai2_stable/README.md
    
## Tasks in Progress:
    1. Implementing the base model.
    2. Learning common implementations in PyTorch.
    3. How to do error analysis.
    
## Future Tasks:
1. [ ] Analysing the output of the base model - CNQA
2. [ ] Implementing the McQueen model.
3. [ ] Analysing the error analysis provided by Kuntal for the McQueen model to come up with some categorizaiton, which when solved will          improve the accuracy.
4. [ ] Identify where improvements could be made on the CNQA model.
    
    
 ## Contributions:
 
 ### Archana:
 1. Ran the master branch of the ai2 model on my local computer.
    * Faced problems related to versions of the required modules and fixed them.
    * Came across some unresolvable errors.
 2. Implemented a stable branch of the model in my local.
    * Ran into CUDA out of memory exception because of the size of my RAM.
 3. Executed the stable version on colab editor.
    * Kept running into lazy_trainer_dataloader error.
    * Fixed the error and installed proper versions of certain libraries like pytorch lightning.
    * Ran into CUDA out of memory. So reduced the training data size into 5000 instances.
 4. Understanding how PyTorch and the forward function works.

 ### Stutee:
 1. Executed the stable branch of the ai2 model on my local computer.
    * Installed dependencies to run the project.
    * The program ran into CUDA out of memory exception while still executing the first Epoch.
 2. Implemented the master branch of the model.
    * Resolved dependencies.
    * Ran into AttributeError. Tried to fix the error by modifying the code, could not resolve the issues successfully.
 3. Learning the use of PyTorch with respect to how it implements BERT and RoBERTa.
 4. Investigating the dataset to comprehend how the model is trained and what might be changed to help improve accuracy of the system.

### Simran:
1. Ran the master version of the ai2 model on my local computer.
    * Faced certain problems installing apex and implementing it in the code.
    * Faced certain problems with the class label error.
2. Executed the branch of the ai2 model on my local computer with less data.
    * Installed dependencies to run the project.
    * The model was trained with the given data.
    * Evaluated the same model and got 0.2 as F1 score, 95.0 as confidence and 22.8 as accuracy.
3. Interpreting and understanding dataset given to train the model.
4. Trying to implement McQueen model on my local computer with less data.

