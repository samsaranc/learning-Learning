import numpy as np
from scipy import stats
import random
import matplotlib.pyplot as plt
#2D plotting

n = 10
p_arms = np.random.rand(n)
epsilon = 0.1

def reward(prob):
	reward = 0;
	for i in range(10):
		if random.random() < prob:
			reward += 1
	return reward


#init memory array; has 1 row defaulted to random action index
#action value
av_hist = np.array([np.random.randint(0, (n+1)), 0]).reshape(1,2)

#greedy method, selects best arm based on array of history
def bestArm(a):
	bestArm = 0 #default to 0
	bestMean = 0
	for u in a:
		#find mean reward for each action
		avg = np.mean(a[np.where(a[:,0] == u[0])][:, 1]) 
		if bestMean < avg:
				bestMean = avg
				bestArm = u[0]
	return bestArm


#main
plt.xlabel("Plays k")
plt.ylabel("Average Reward")
for i in range(500): 
	if random.random() > epsilon: #GO GREEDY
		choice = bestArm(av_hist)
		reward_i = reward(p_arms[choice])
		thisAV = np.array([[choice,reward_i]])		# 
		av_hist = np.concatenate((av_hist, thisAV), axis=0)
	else: # rando arm
		choice = np.where(p_arms == np.random.choice(p_arms))[0][0]
		r_i = reward(p_arms[choice])
		thisAV = np.array([[choice, r_i]])
		av_hist = np.concatenate((av_hist, thisAV), axis=0)
	#calculate % correct arm chosen to plot
	percent_correct = 100*(len(av_hist[np.where(av_hist[:,0] == np.argmax(p_arms))])/len(av_hist))
	#get mean reward 
	mean_from_running = np.mean(av_hist[:,1])
	plt.scatter(i, mean_from_running)
plt.show()






##from IPython import get_ipython
##get_ipython().run_line_magic('matplotlib', 'inline')