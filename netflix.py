import streamlit as st 
import pandas as pd

st.title("Movie Recommender")

movies = pd.read_csv('netflix_titles.csv')
st.write(movies)

st.write("Fill in your interests")
type_choice = st.selectbox("Choose content type:", ["Movie", "TV Show"])
year_min, year_max = int(movies["release_year"].min()), int(movies["release_year"].max())
year_range = st.slider("Select release year range:", min_value=year_min, max_value=year_max, value=(2000, 2020))

f = movies[
    (movies["type"] == type_choice) &
    (movies["release_year"].between(year_min, year_max))
].sort_values(["release_year", "title"], ascending=[False, True])


cols = ["show_id", "type", "title", "director", "cast", "release_year", "rating", "duration"]
cols = [c for c in cols if c in f.columns]

st.dataframe(f[cols], use_container_width=True)



