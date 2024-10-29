class NaiveBayes(object):
    """
    Your implementation of Naive Bayes classifier.
    """

    def __init__(self, alpha=1.0):
        """
        Initialize the Naive Bayes classifier.
        
        Parameters
        ----------
        alpha : float, default=1.0
            Additive (Laplace/Lidstone) smoothing parameter
            (0 for no smoothing).
        """

        self.alpha = alpha
    
    def fit(self, X, y):
        """
        Fit the Naive Bayes classifier on the training set (X, y).
        
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Training vectors, where n_samples is the number of samples
            and n_features is the number of features.
        y : array-like, shape (n_samples,)
            Target values.
        """

        self.n_features = X.shape[1]
        self.n_samples = X.shape[0]
        self.n_classes = np.unique(y).shape[0]

        self.beta = np.zeros((self.n_classes, self.n_features))
        self.pi = np.zeros(self.n_classes)

        # START YOUR CODE HERE
        # Given (X, y), compute the parameters `beta` and `pi`
        # (Hint: Calculate `beta` according to the frequencies of words
        #    and `pi` according to the class frequencies.
        #    Remember to consider `alpha` for the Laplace smoothing.)
        for c in range(self.n_classes):
            classSamples = X[y == c]
            self.beta[c] = np.sum(classSamples, axis=0) + self.alpha
            self.pi[c] = (np.sum(y == c) + self.alpha) / (self.n_samples + self.n_classes * self.alpha)
        self.beta /= np.sum(self.beta, axis=1)[:, np.newaxis]
        # END YOUR CODE HERE

        self.log_beta = np.log(self.beta)
        self.log_pi = np.log(self.pi)

    def predict_proba(self, X):
        """
        Return posterior probabilities of classification for X.
        
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Test vectors, where n_samples is the number of samples
            and n_features is the number of features.
        
        Returns
        -------
        y_prob : array-like, shape (n_samples, n_classes)
            Posterior probabilities of classification per class.
        """

        # START YOUR CODE HERE
        # Given `X``, return the posterior probabilities of classification
        # (Hint: Use `beta`` and `pi`. Remember to normalize the probabilities.)
        logProbs = np.dot(X, self.log_beta.T) + self.log_pi
        probs = np.exp(logProbs - np.max(logProbs, axis=1, keepdims=True))
        return probs / np.sum(probs, axis=1, keepdims=True)
        # END YOUR CODE HERE
        
        pass

    def predict_log_proba(self, X):
        """
        Return posterior log probabilities of classification for X.
        
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Test vectors, where n_samples is the number of samples
            and n_features is the number of features.
        
        Returns
        -------
        y_log_prob : array-like, shape (n_samples, n_classes)
            Posterior log probabilities of classification per class.
        """

        # START YOUR CODE HERE
        # Given X, return the posterior log probabilities of classification
        # (Hint: Use `log_beta`` and `log_pi`.)
        logProbs = np.dot(X, self.log_beta.T) + self.log_pi
        return logProbs - np.max(logProbs, axis=1, keepdims=True)
        # END YOUR CODE HERE

        pass
