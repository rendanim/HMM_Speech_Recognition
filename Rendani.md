## 15-12-2016
Met with Sudanshu and Helder for intial discussions. Helder mentioned he had done some work and that feature creation seems to be the biggest challenge. The team discussed Bag of Words features and n-grams on the amino acids. The team resovled to work independenlty over the chrismas period.
## 20-12-2016
Started reading some notable works in the area of signal peptide detection. Realised one needed to understand protein transport and targeting first. This site proved to be a good reference http://www.signalpeptide.de/.
## 02-01-2017
After getting a better unstandning of what signal peptides are and what they do. I read the following paper.
Tittle: Machine learning approaches for the prediction of signal peptides
and other protein sorting signals
Autors:Nielsen e.t.al
The paper foused on a Hidden Markov Models and Artificial Neural Networks. The best approach seemed to be a hybrid NN-HMM.
## 04-01-2017
I was assigned the task of implementation of the trained models on new proteomes. Initailly there were some doubts as to which proteomes where right ones - which filters to put on biomart. After some googling i settled on the ftp site for biomart http://www.ensembl.org/info/data/ftp/index.html. The species I chose were `Homo Sepien` and `Mus musculus`.
## 05-01-2017
Wrote code to get predictions on the new proteomes. Initally I had incoorectly created new vectorizers for the new datasets. I corrected this after some errors from the `predict()` methods. The predicted peptides in Human were as follows:
Classifier | Predicted Peptides Signal
-----------| -----------
KNN | 46124 
SVC Linear | 30143 
SVC RBF | 41710 
Decision Tree | 45830 
Random Forest | 48916 
Adaboost | 49505  
MLP | 38492 

## 06-01-2017
I then documented the results in the latex document. In addition to this I also wrote the the discussion of results and other observations.

