import streamlit as st
import pickle
import pandas as pd
import requests

def recommend(movie):
    idx = movies_list[movies_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(cs[idx])), reverse=True, key=lambda x:x[1])
    rec_movies = []
    rec_posters = []
    for i in distances[1:6]:
        movie_id = movies_list.iloc[i[0]].id
        rec_posters.append(fetch_poster(movie_id))
        rec_movies.append(movies_list.iloc[i[0]].title)
    return rec_movies, rec_posters

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

st.title('Movies Recommender System')
movies = pickle.load(open('movies_dict.pkl','rb'))
cs = pickle.load(open('cs.pkl','rb'))
movies_list = pd.DataFrame(movies)
option = st.selectbox(
    "Which movie recommendations you want?",
    movies_list['title'].values,
    index=None,
    placeholder = "Enter and Select Movie...",
    )
# st.button("Recommend", type="primary")
if st.button("Recommend"):
    rec_names, rec_post = recommend(option)
    # for col in st.columns(5):
    #     st.text(rec_names[col])
    #     st.image(rec_post[col])
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(rec_names[0])
        st.image(rec_post[0])
    with col2:
        st.text(rec_names[1])
        st.image(rec_post[1])

    with col3:
        st.text(rec_names[2])
        st.image(rec_post[2])
    with col4:
        st.text(rec_names[3])
        st.image(rec_post[3])
    with col5:
        st.text(rec_names[4])
        st.image(rec_post[4])
    