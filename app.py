import streamlit as st
import pickle
import pandas as pd
from tmdbv3api import TMDb
from tmdbv3api import Movie
import requests
tmdb=TMDb()
tmdb.api_key='d3702932f6c0f678bb8f65665c01f376'
base_url='https://image.tmdb.org/t/p/original/'
def fetch_poster(movie_id):
    movie=Movie()
    movie_details=movie.details(movie_id)
    poster_path=movie_details.poster_path
    poster_url=base_url+poster_path
    return(poster_url)
def recommend(movie):
    idx=movies[movies['title']==movie].index[0]
    distances=similarity[idx]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended=[]
    posters=[]
    for i in movie_list:
        id=movies.iloc[i[0]].movie_id
        # posters will be fetched from an API
        recommended.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(id))
    return(recommended,posters)
st.title('Movie Recommender Application:')
movies_dict=pickle.load(open('movies_dictionary.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)
option=st.selectbox('Enter a Movie',movies['title'].values)
if st.button('Find Recommendations'):
    recommendations,posters=recommend(option)
    st.write("Top 5 Movie Recommendations based on your choice:")
    columns=st.columns(5)
    for i in range(len(recommendations)):
        columns[i].write(recommendations[i])
        columns[i].image(posters[i], use_column_width=True)
