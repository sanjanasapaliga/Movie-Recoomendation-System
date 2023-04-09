import streamlit as st
import pickle
import pandas
import requests
movies_list=pickle.load(open('movies_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=34aa9a0bc9898f1f043950e346ef6d84&language=en-US'.format(movie_id))
    data=response.json()
    return 'https://image.tmdb.org/t/p/original/'+data['poster_path']


def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distances=similarity[index]
    movies_recommend=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[0:10]
    recommended=[]
    poster=[]
    for i in movies_recommend:
        movieId=movies.iloc[i[0]].id
        recommended.append(movies.iloc[i[0]].title)
        poster.append(fetch_poster(movieId))
    return recommended,poster


movies = pandas.DataFrame(movies_list)
st.title('Movie Recommendation System')


selected_movie = st.selectbox('Type the Movie', movies['title'])

if st.button('Search'):
    recommendations,poster=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)
    col6, col7, col8, col9, col10=st.columns(5)
    with col1 :
        st.image(poster[0])
        st.text(recommendations[0])
    with col2:
        st.image(poster[1])
        st.text(recommendations[1])
    with col3:
        st.image(poster[2])
        st.text(recommendations[2])
    with col4:
        st.image(poster[3])
        st.text(recommendations[3])
    with col5:
        st.image(poster[4])
        st.text(recommendations[4])
    with col6:
        st.image(poster[5])
        st.text(recommendations[5])
    with col7:
        st.image(poster[6])
        st.text(recommendations[6])
    with col8:
        st.image(poster[7])
        st.text(recommendations[7])
    with col9:
        st.image(poster[8])
        st.text(recommendations[8])
    with col10:
        st.image(poster[9])
        st.text(recommendations[9])
