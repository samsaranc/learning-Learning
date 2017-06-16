import numpy as np
from scipy import stats
import random
import matplotlib.pyplot as plt
#2D plotting

n = 10
p_arms = np.random.rand(n)
epsilon = 0.1


#init memory array; has 1 row defaulted to random action index
#action value
av_hist = np.ones(n)
a_counts = np.zeros(n)

def reward(prob):
	rwd = 0;
	for i in range(n):
		if random.random() < prob:
			rwd += 1
	return rwd



#greedy method, selects best arm based on array of history
def bestArm(a):
	return np.argmax(a) #returns index of elt with greatest val


#main
plt.xlabel("Plays k")
plt.ylabel("Average Reward")
for i in range(500): 
	if random.random() > epsilon: #GO GREEDY
		choice = bestArm(av_hist)
		a_counts[choice]+=1
		k = a_counts[choice]
		reward_i = reward(p_arms[choice])
		old_avg = av_hist[choice]
		new_avg = old_avg + (float)(1/k)*(reward_i - old_avg)
		av_hist[choice] = new_avg 
	else: # rando arm
		choice2 = np.where(p_arms == np.random.choice(p_arms))[0][0]
		a_counts[choice2]+=1
		k = a_counts[choice2]
		r_i = reward(p_arms[choice2])
		old_average = av_hist[choice2]
		new_average = old_average + (1/k)*(r_i - old_average)
		av_hist[choice2] = new_average 
	#have to use np.average and supply the weights to get a weighted average 
	mean_from_running = np.average(av_hist, weights=np.array([a_counts[i]/np.sum(a_counts) for i in range(len(a_counts))]))
	plt.scatter(i, mean_from_running)
plt.show()





##from IPython import get_ipython
##get_ipython().run_line_magic('matplotlib', 'inline')