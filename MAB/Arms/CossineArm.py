import numpy as np 
import pandas as pd 
import pickle

with open(r"E:\SHIVAM MAHAJAN\Desktop\Github\Beer-Recommendation-and-Application-of-MAB\Data\beer_profile_hash.pickle", "rb") as handle:
	hash_beers = pickle.load(handle)
	hash_profiles = pickle.load(handle)
	hash_beers_inv = pickle.load(handle)
	hash_profiles_inv = pickle.load(handle)

class CossineArm:
	def __init__(self):
		with open(r"E:\SHIVAM MAHAJAN\Desktop\Github\Beer-Recommendation-and-Application-of-MAB\Data\cossine_arm.pickle", 'rb') as handle:
			self.sim = np.array(pickle.load(handle))
		print type(self.sim)
		self.name = 'Cossine'
		self.value = 0
		self.count = 0

	def recommend(self, input_beers, k = 10):
		self.k = k
		input_beers = np.array(input_beers)
		n = len(input_beers)
		beer_nos = np.array([hash_beers[beer] for beer in input_beers])
		arr = np.sum(self.sim[beer_nos, :], axis = 0)/float(n)
		top_beers = np.array([hash_beers_inv[a] for a in np.argsort(-arr)[:k+n]])
		top_beers = np.array([beer for beer in top_beers if hash_beers[beer] not in beer_nos])
		#top_k_beers_sno = [a for a in np.argsort(-arr)[1:k+1]]
		top_k_beers = top_beers[:k]
		return top_k_beers

	def draw(self, input):
		return self.k - input + 1  # Index 0 has rank 1.


if __name__ == "__main__":
	arm = CossineArm()
	beers = ["60 Minute IPA", "Stone Ruination IPA"]
	input_beer = raw_input("Enter a beer you like!")
	beers.append(input_beer)
	arr = arm.recommend(beers, 10)
	for i in range(len(arr)):
		print str(i+1) + ") " + arr[i]
	print str(arm.k + 1) + ") " + "None"
	input_rank = raw_input("Enter the Beer you would like to have ?")
	print "Score obtained is " + str(arm.draw(int(input_rank)))



		
