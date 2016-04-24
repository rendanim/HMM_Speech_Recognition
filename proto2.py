import numpy as np
from tools2 import *
import sklearn.mixture as sm
import matplotlib.pyplot as plt
def main():
    tidigits=np.load('lab2_tidigits.npz')['tidigits']
    example=np.load('lab2_example.npz')['example'].item()
    models=np.load('lab2_models.npz')['models']
    
    print models[0]['pron']
    print models[0]['digit']
    print models[0]['gmm']['means'].shape
    ss=score_gmm(models,tidigits)
    print ss
    #print tt
    #print cmp(tt,ss)

    #log_gmm=log_multivariate_normal_density_diag(example['mfcc'],models[0]['gmm']['means'],models[0]['gmm']['covars'])
    #weights_m=models[0]['gmm']['weights']
    #gmmloglik_out=gmmloglik(log_gmm,weights_m)
    #print gmmloglik_out
    #print example['gmm_loglik']

    
    plt.figure('Gmm Scores') 
    plt.title('Gmm Scores')
    plt.imshow(ss,origin='lower',interpolation='nearest',aspect='auto')
    plt.show()
     
   
    
    
    



def score_gmm(model_arr, spch_data):
    '''' Score different gmm models and retrun a matrix of likelihood scores'''
    nM=model_arr.shape[0]
    nS=spch_data.shape[0]

    scores=np.empty((nS,nM))
    pred_digit=list()
    tru_digit=list()

    for i in xrange(0,nS):
        for j in xrange(0,nM):
            log_gmm=log_multivariate_normal_density_diag(spch_data[i]['mfcc'],model_arr[j]['gmm']['means'],model_arr[j]['gmm']['covars'])
            weights_m=model_arr[j]['gmm']['weights']
            scores[i,j]=gmmloglik(log_gmm,weights_m)
        pred_digit.append(model_arr[np.argmax(scores[i,:])]['digit'])
        tru_digit.append(spch_data[i]['digit'])

            
    return scores #pred_digit , tru_digit 









 




def gmmloglik(log_emlik, weights):
    """Log Likelihood for a GMM model based on Multivariate Normal Distribution.

    Args:
        log_emlik: array like, shape (N, K).
            contains the log likelihoods for each of N observations and
            each of K distributions
        weights:   weight vector for the K components in the mixture

    Output:
        gmmloglik: scalar, log likelihood of data given the GMM model.
    """
    l=log_emlik.shape[0]
    gmmloglik_out=0
    for i in xrange(0,l):
        gmmloglik_out+=logsumexp(np.log(weights)+log_emlik[i,:])

    return gmmloglik_out        
def forward(log_emlik, log_startprob, log_transmat):
    """Forward probabilities in log domain.

    Args:
        log_emlik: NxM array of emission log likelihoods, N frames, M states
        log_startprob: log probability to start in state i
        log_transmat: log transition probability from state i to j

    Output:
        forward_prob: NxM array of forward log probabilities for each of the M states in the model
    """

def backward(log_emlik, log_startprob, log_transmat):
    """Backward probabilities in log domain.

    Args:
        log_emlik: NxM array of emission log likelihoods, N frames, M states
        log_startprob: log probability to start in state i
        log_transmat: transition log probability from state i to j

    Output:
        backward_prob: NxM array of backward log probabilities for each of the M states in the model
    """

def viterbi(log_emlik, log_startprob, log_transmat):
    """Viterbi path.

    Args:
        log_emlik: NxM array of emission log likelihoods, N frames, M states
        log_startprob: log probability to start in state i
        log_transmat: transition log probability from state i to j

    Output:
        viterbi_loglik: log likelihood of the best path
        viterbi_path: best path

    """
if __name__ == "__main__":
    main()
