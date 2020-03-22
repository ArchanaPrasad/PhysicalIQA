Implementing the RoBERTa w. CNQA on the PhysicalIQA dataset with a few modifications.
    1. With 5000 instances of training data.
    2. Batch size = 2
    
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
    
