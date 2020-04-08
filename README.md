# PhysicalIQA

Implementing the RoBERTa w. CNQA on the PhysicalIQA dataset with a few modifications.
1. With 6000 instances of training data.
2. Batch size = 4

Link to the Readme.md file of the model used - https://github.com/isi-nlp/ai2/blob/ai2_stable/README.md
    
## Tasks in Progress:
    1. Improving the acuuracy of the base model.
    2. Learning common implementations in PyTorch.
    3. How to do error analysis.
    
## Future Tasks:
1. [ ] Analysing the output of the base model - CNQA
2. [ ] Implementing the McQueen model.
3. [ ] Analysing the error analysis provided by Kuntal for the McQueen model to come up with some categorizaiton, which when solved will          improve the accuracy.
4. [ ] Identify where improvements could be made on the CNQA model.
    
    
 ## Contributions:
 
 ### Archana:
 #### Phase 1:
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
 5. Implemented the base model successfully with a F1 score of 0.528.
 6. Improved the accuracy of the CNQA model to 0.69 using 6000 rows of training data.
 7. Learnt to perform error analysis.
 8. Performed error analysis on the results produced by different models and found some inisghts on why the models were not able to predict the correct answers for certain questions.
 
 #### Phase 2:
 1. After performing the error analysis on the McQueen data shared to us, I looked at the instances where the model had failed and tried to find similarities between the failures.
 2. Found that there were many examples where the model was not able to distinguish between prepositions that mark sematic roles.
 3. So I came up with the idea to, identify such prepositions and to perturb them with similar possible replacement words.
 4. This inturn would result in an expanded dataset. The model might be able to learn better by introducing Question and Answer pairs that are highly positive cases and that are highly negative cases.
 5. Working currently on identifying the possible set of replacement tokens that would make sense with the instances under consideration.
 

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
    * Wrote a script to transform the dataset as per requirements of the code
    * Faced certain errors and tried solving them.
5. Learning about PyTorch and its usage to understand the code implementation.

### Haseeb:
1.Executed ai2 master branch on local computer:
        * Fixed issues related to library/module (CPU only modules)
	*Training started succesfully but ran for nearly 2 days and then failed due to memory allocation error
2.Executed ai2 stable branch on local computer:
	Model ran for 1 epoch, created a checkpoint and then got stuck in a saving checkpoint loop - couldnt resolve further
	Ran the evaluation script with the created checkpoint but ran into library version errors
3.Executed ai2 master branch on colab:
	lazy_trainer_dataloader error - fixed by using the stable branch
4.Executed ai2 stable branch on colab:
	Fixed the lazy_trainer_dataloader error by installing pytorch 1.2.0 and corresponding torchvision library
	Ran into CUDA out of memory. So reduced the training data size
5.Base model ran successfully. Obtained F1 score of 0.517 with 5000 training size
6.Error sheet analysis

