#To run the file run the command: python get_wiki_data.py <num>
#*******where num is from 0 to 16******

import sys
import pandas as pd
import numpy as np
import wikipedia
import warnings
from string import punctuation
from tqdm import tqdm

warnings.filterwarnings('ignore')

premises = pd.read_csv('train_goals.csv')
premises = premises.values
premises = np.asarray([str(word).replace('\\','').lower() for word in premises])
premisespremises = np.unique(premises)
premises = np.asarray([word.replace('\n','').replace('\\','').replace('\"','').replace('[','').replace(']','').replace("'",'') for word in premises])
print(premises.shape)
n=int(sys.argv[1])
print(n)
start = n*1000
end = min(16113 , (n+1)*1000)
premises = premises[start:end]


data = []
for query in tqdm(premises):
    # query = premises[i]
    temp = []
    summary = "None"
    result = "None"
    results = wikipedia.search(query)
    index = 0
    flag = True
    while flag and index<len(results):
        try:
            result = results[index]
            wiki_page = wikipedia.page(result, auto_suggest=False)
            summary = wiki_page.summary
            summary = summary.replace('\n','')
            flag=False
        except:
            index+=1

    temp.append(query)
    temp.append(result)
    temp.append(summary)
    
    data.append(temp)
    
    
df = pd.DataFrame(data, columns = ['query', 'result', 'content']) 
df.to_csv('train_wiki_results_with_content_'+str(n)+'.csv', index=False)