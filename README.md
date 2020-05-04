# PhysicalIQA

Implementing the RoBERTa w. CNQA on the PhysicalIQA dataset with a few modifications.
1. With 6000 instances of training data.
2. Batch size = 4

Link to the Readme.md file of the model used - https://github.com/isi-nlp/ai2/blob/ai2_stable/README.md
   
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
 
 #### Phase 3:
 1. I Created a dataset with extra 400 samples that are made up of additional question answer pairs which are different from each other by the prepositions that were present(if any) in the original question answer pair.
 2. I used Spacy similarity to identify how similar the sentences are with respect to presence of differnet prepositions in them which was not useful. I went ahead with using common sense knowledge to identify similar and dissimilar prepositions.
 3. The additional set consists of both positive and negative samples.
 4. I Ran the CNQA base model with this tweaked data set for the same number of samples(6000) was observed an increase in the accuracy to 0.725.
 

 ### Stutee:
   #### Phase 1:
 1. Executed the stable branch of the ai2 model on my local computer.
    * Installed dependencies to run the project.
    * The program ran into CUDA out of memory exception while still executing the first Epoch.
 2. Implemented the master branch of the model.
    * Resolved dependencies.
    * Ran into AttributeError. Tried to fix the error by modifying the code, could not resolve the issues successfully.
 3. Learning the use of PyTorch with respect to how it implements BERT and RoBERTa.
 4. Investigating the dataset to comprehend how the model is trained and what might be changed to help improve accuracy of the system.
 
  #### Phase 2:
 1. After looking at the dataset, going through McQueen model's report and comparing it with the source of the data, I noticed how the training data was retrieved.
 2. So, I looked for data retrieval and modification techniques to use the same data source and retrieve more relevant information.
 3. By providing the same information mutltiple times with a little modification, the system can be trained to link a particular question to a particular set of answers. This modification can be done by replacing original words with new words having similar vector representation.
 4. The rationale behind this idea is that the machine will link a group of words with similar vector representations in the question to a group of words with similar vector representation in the answer, i.e, to link a word in query to a word in answer and create more such links with similar words finally forming a pair pattern. Thus, making the model look for words that mostly co-occur in patterns while looking for answers.
 5. After researchhing a bit into it, the information retrieval task was an unrealistic goal to achieve in a short time. 
 6. Two of our proposed approaches had data augmentation in common. So, by combining part of my approach of preparing the same questions with their synonyms and augmenting data we came up with one solution.
 7. To execute this approach, we replaced a random word in the question with its synonym and did the same with the answer thus increasing the dataset and providing the same information multiple times to train the model into chosing the intended answer.


### Simran:
 #### Phase 1:
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
 
 #### Phase 2:
 1. After performing the error analysis on the McQueen data shared to us, I looked at the instances where the model had failed and tried to find similarities between the failures.
 2. Found that there were many examples where the model was not able to distinguish identify the correct solution even if the answer was given to the model while training in the form of wikihow data.
 3. So I came up with the idea to, identify such instances where the goal statement could be augmented and could be added to the dataset.
 4. This inturn would result in an expanded dataset. The model might be able to learn better by introducing Question and Answer pairs.
 5. Working currently on identifying how the text could be augmented. Found certain github repositories which could help us achieve the goal.
 
 #### Phase 3:
 1. Worked and researched on the github repositories found in phase 2, which could help in text augmentation.
 2. Found 1 repository which was built upon NLTK and WORDNET which could achieve our goal with the help of:
    * Synonym Replacement (SR)
    * Random Insertion (RI)
    * Random Swap (RS)
    * Random Deletion (RD)
 3. Implemented this to augment the dataset.
    * Since our dataset was in different format, the codebase for this had to be changed and adjusted according to our dataset format.
    * Number of augments was given as a parameter to the code.
 4. Tried expanding the dataset with number of augmented goals as 3 at first but the data was too large and could not be executed even in COLAB. Then tried expanding the dataset with number of augmented goals as 1 but again the data was too large and could not be executed even in COLAB.
 5. Since, it could not have been executed and hence we could not know what would it impact the accuracy, I started analyzing the new dataset and started comparing new augmented goal statements with the old ones.
 6. The analysis showed that there were certain agmented sentences which might not effect the accuracy, but there were certain sentences that would effect the accuracy but since it is not tested, it is still unknown.

### Haseeb:

 #### Phase 1:
1. Executed ai2 master branch on local computer:
        * Fixed issues related to library/module (CPU only modules)
	* Training started succesfully but ran for nearly 2 days and then failed due to memory allocation error
2. Executed ai2 stable branch on local computer:
	* Model ran for 1 epoch, created a checkpoint and then got stuck in a saving checkpoint loop - couldnt resolve further
	* Ran the evaluation script with the created checkpoint but ran into library version errors
3. Executed ai2 master branch on colab:
	* lazy_trainer_dataloader error - fixed by using the stable branch
4. Executed ai2 stable branch on colab:
	* Fixed the lazy_trainer_dataloader error by installing pytorch 1.2.0 and corresponding torchvision library
	* Ran into CUDA out of memory. So reduced the training data size
5. Base model ran successfully. Obtained F1 score of 0.517 with 5000 training size
6. Error sheet analysis

 #### Phase 2:
  1. From the initial error analysis I found that there are instances where the relevant information was available easily.
  2. This information was not available in the wikihow file which was the primary source for knowledge in the original model.
  3. I started working on an algorithm to fetch context during runtime from internet
  4. Using wikipedia api libraries, I was able to design an algorithm, wiki_data_extractor, to use the question of an example as a query and fetch a wikipedia page object. Using this a summary passage can be extracted from to be used as context for selected example.
 
 #### Phase 3:
 1. I made  further enhancements to the wiki_data_extractor algorithm to rectify the initial search errors. Ouput file contains query, wikipedia result, wikipedia summary (train_wiki_data.csv)
 2. Also created a modified version of the script to combine the question and solutions of each example to create two queries and using them to fetch data from wikipedia (train_wiki_data_with_sols.csv)
 3. Wikipedia lookups for each example took about 1 to 2 seconds. For training dataset of  16,000+ examples the total runtime was 4+ hours. To reduce this I created a python script to run the algorithm parellely and then combine the resulting files. This reduces runtime to less than an hour.
 4. Tried to execute McQueen model on colab (McQueen_colab.ipynb) as well as install elasticsearch on colab. Ran into elasticsearch server related issues and other 'files missing' error.


