
## Content-based Movie Recommender Application

Try out the [Movie-Recommender Application](https://movie-recommender-app.streamlit.app/). (Deployed using **streamlit**)

This Repository contains a Machine Learning Project. It is a content-based movie recommender system which uses the **tmdb 5000 movies and credits** kaggle dataset to recommend 5 movies based on a movie watched. 

Some of the main points to mention about this project are as follows:

 - It is a content-based system of recommendation.
 - The **tmdb 5000 movies and credits datasets** have been used: [Kaggle Dataset Link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)
 - It utilizes the technique of **Text Vectorization** using tags from the movie overview, crew details, genre etc.
 - There are various ways to vectorize text, however, I have chosen the simple but effective technique of **Bag of Words** .
 - Some of the major python modules used are **numpy**, **pandas**, **nltk**, **pickle**, **tmdbv3api**, **requests** and **streamlit**.
 - **Cosine Distance** has been used as the criteria for determining similarity (closeness) between the vectors. (In higher dimensional spaces, Euclidean distance is not a differentiating factor) 

### Steps to run and execute the application locally:

To execute the file, simply clone the repository in your local machine, download the datasets from the [Drive Link](https://shorturl.at/bmHJ6) and execute the entire .ipynb file. Once it is done, you will have two files **similarity.pkl** and **movie_dictionary.pkl**. After this, simply open the terminal and execute **app.py**. 

    streamlit run app.py
**OR**, if you wish to save time, you can simply download the .pkl files too from the given [Drive Link](https://shorturl.at/bmHJ6). 

**P.S.** *Ensure that all the files are in the same directory before running app.py and follow the steps carefully.*
