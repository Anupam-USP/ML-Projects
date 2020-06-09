import warnings

import pandas as pd

warnings.filterwarnings('ignore')

# Get the dataset
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
# Give your path to dataset
df = pd.read_csv("/home/anupam/Downloads/ml-100k/u.data",
                 sep='\t', names=column_names)

movies_title = pd.read_csv(
    "/home/anupam/Downloads/ml-100k/u.item", sep='\|', header=None)

movies_title = movies_title[[0, 1]]
movies_title.columns = ['item_id', 'title']

df = pd.merge(df, movies_title, on='item_id')

# Exploratory data analysis
ratings = pd.DataFrame(df.groupby('title').mean()['rating'])
ratings['no. of ratings'] = pd.DataFrame(df.groupby('title').count()['rating'])

movie_matrix = df.pivot_table(
    index="user_id", columns="title", values="rating")


def predict(movie_name):
    # if movie_name in movies_title[1]:
    try:
        movie_user_ratings = movie_matrix[movie_name]
        similar_to_movie = movie_matrix.corrwith(movie_user_ratings)

        corr_movie = pd.DataFrame(similar_to_movie, columns=['correlation'])
        corr_movie.dropna(inplace=True)

        corr_movie = corr_movie.join(ratings['no. of ratings'])
        prediction = corr_movie[corr_movie['no. of ratings'] > 100].sort_values('correlation', ascending=False)
        print(prediction.head())
        return prediction
    except KeyError:
        print("Movie not present or guidelines not followed!")


movie_name = input("Enter movie name:")
prediction = predict(movie_name)
