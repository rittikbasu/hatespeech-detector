# Automated Detection of Hate Speech

Repository for Rittik Basu, Rehmat Irphany, Sanah Saleem, and Shaurya Sood.
For more information on the project [click here](https://docs.google.com/document/d/1DQqylMDdDANnePqJwtOnycg6JS85KcJbqYFKYoQHI2Y/edit?usp=sharing) to read the report


A key challenge for automatic hate-speech detection on social media is the separation of hate speech from other instances of offensive language. Lexical detection methods tend to have low precision because they classify all messages containing particular terms as hate speech and previous work using supervised learning has failed to distinguish between the two categories. Therefore in order to create a hate-speech-detecting algorithm, we used Python-based NLP machine learning techniques.

* Firstly, we used a crowd-sourced hate speech lexicon to collect tweets containing hate speech keywords. The data is labelled into three categories: those containing hate speech, only offensive language, and those with neither.

* Then, using a *NLP (Natural Language Processing)* technique called *Tf-Idf vectorization*, we extracted keywords from the dataset that convey importance within hate speech.

* Finally, based on a machine learning technique called *logistic regression*, which is popular for probability calculations, we trained the model to classify hate speech.


