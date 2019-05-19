import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt

fandango = pd.read_csv('../resources/fandango_score_comparison.csv')
series_film = fandango['FILM']
# print (type(series_film))
# print(series_film[0:5])
series_rt = fandango['RottenTomatoes']
# print(series_rt[0:5])

film_names = series_film.values
rt_scores = series_rt.values
series_custom = Series(rt_scores,index=film_names)
series_custom[[]]

