### Basic Structure of how this WebApp makes prediction
To detect fake news the application :
  * Uses a Logistic Regression Model trainned on DataSets acquired at Kaggle (See Refrences Below) to get a basic prediciton based on wordings of the news article. To do this certain words which occur too frequently are removed from the text using the ``` ./lib/preprocess.py ``` script.
  * The processed articles are used to fit a TF-IDF vectorizer, which transforms the text data into numerical vectors. These vectors are then used to train a Logistic Regression model. Then both the acquired model and TFID vectorizer are exported to be used for future predictions using the ``` ./lib/preprocess.py ``` script.  
  * The article headline is then searched over google programitically and using a list of trusted newspaper publishers (in trusted.txt), the trusted articles are then scrapped from the web. This is done using the ``` ./lib/webscrap.js ``` script.
  * Using a Bert-Base model the article given to us and the article on the internet are checked for similarity and a similarity score is given.
  * The combination of the two score is used for giving the final prediction.


#### References
* News.csv - https://www.kaggle.com/c/fake-news/data
* news.csv - https://www.kaggle.com/datasets/imbikramsaha/fake-real-news
