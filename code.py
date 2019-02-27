# --------------
import numpy as np
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.

data_ipl = np.genfromtxt(path,delimiter=',',dtype=str,skip_header=True)
# print(data_ipl)
# How many matches were held in total we need to know so that we can analyze further statistics keeping that in mind.
# print(data_ipl[:,0:4])
# print(data_ipl[0])
print(len(set(data_ipl[:,0])))
# print(len(np.unique(data_ipl[:0])))

# this exercise deals with you getting to know that which are all those six teams that played in the tournament.
team_1 = set(data_ipl[:,3])
team_2 = set(data_ipl[:,4])
# print(team_1)
# print(team_2)

print(team_1.union(team_2))
# An exercise to make you familiar with indexing and slicing up within data.


# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
extras_data = data_ipl[:,17]
extra_data_int = map(int,extras_data)
print(sum(extra_data_int))
# this exercise will help you get the statistics on one particular team
given_batsmen = 'ST Jayasuriya'
is_out = data_ipl[:,-3] == given_batsmen
# print(is_out)
print(data_ipl[:,[-12,-2]][is_out])

print(len(set(data_ipl[data_ipl[:,5]=='Mumbai Indians'][:,0])))

# data_ipl[:,-7]
filter = data_ipl[:,-7].astype(int)==6
batsmans = data_ipl[filter][:,13]
from collections import Counter
cnt_batsmans = Counter(batsmans)
print(max(cnt_batsmans,key=cnt_batsmans.get))

# An exercise to know who is the most aggresive player or maybe the scoring player



