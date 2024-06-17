### Basic Structure of how this WebApp makes prediction
To detect fake news the application :
  * Uses a Logistic Regression Model trainned on DataSets acquired at Kaggle (See Refrences Below) to get a basic prediciton based on wordings of the news article. To do this certain words which occur too frequently are removed from the text using the ``` ./lib/preprocess.py ``` module.
  * The processed articles are used to fit a TF-IDF vectorizer, which transforms the text data into numerical vectors. These vectors are then used to train a Logistic Regression model. Then both the acquired model and TFID vectorizer are exported to be used for future predictions using the ``` ./lib/preprocess.py ``` module.  
