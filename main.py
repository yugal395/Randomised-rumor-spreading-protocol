import random  #importing the random module
import matplotlib.pyplot as plt #importing the matplotlib.pyplot module for plotting


# now we will create a function to simulate
def simulate_push(n):
#1: only one person knows the rumour initially
    informed={0}   # we are labelling different informed people with number starting from 0 to n-1
    rounds=0

    #2: continue until everyone knows the rumour
    while(len(informed)<n):
       new_informed=set(informed)# here we are copying the people who already know the rumour and putting it in a new set as we dont want repetition of people
       for u in informed:
           v=random.randint(0,n-1) # so loop over the informed people and selects a random person v from the population
           new_informed.add(v) # add v to the new informed set
       informed=new_informed # update the informed set to the new informed set
       rounds+=1 # increment the round count
       
    return rounds # return the total number of rounds taken to inform everyone
   # so till here we have created a function to simulate the push model of rumour spreading


print(simulate_push(10)) # testing the function with n=10 


def simulate_pull(n):
    informed={0}
    rounds =0

    #2. continue until everyone knows the rumour
    while(len(informed)<n):
        new_informed=set(informed)
        for u in range(n):
         v=random.randint(0,n-1)
         if v in informed:
                new_informed.add(u)
        informed=new_informed
        rounds+=1
    return rounds     


print(simulate_pull(10)) # testing the function with n=10


def simulate_push_pull(n):
    informed={0}
    rounds=0

    while(len(informed)<n):
        new_informed=set(informed)
        for u in range(n):
            v=random.randint(0,n-1)
            if u in informed:
                new_informed.add(v)
            elif v in informed:#if anybody is informed the other gets informed as well
                new_informed.add(u)
        informed=new_informed
        rounds+=1        

    return rounds


print(simulate_push_pull(10)) # testing the function with n=10


# Now we will do a simulation campaign here

n_values=[10,50,100,500,1000,5000]
push_results=[]
pull_results=[]     
push_pull_results=[]

for n in n_values:
    print(f"Simulating for n={n}")
    push_rounds=[]
    pull_rounds=[]
    push_pull_rounds=[]
    
    push_rounds=simulate_push(n)
    pull_rounds=simulate_pull(n)
    push_pull_rounds=simulate_push_pull(n)

    push_results.append(push_rounds)
    pull_results.append(pull_rounds)        
    push_pull_results.append(push_pull_rounds)

    print(f"Push: {push_rounds} rounds, Pull: {pull_rounds} rounds, Push-Pull: {push_pull_rounds} rounds")
    



    #Interesting things here are that push-pull is generally faster than either push or pull alone.
    #using 10^9 agents would freeze the computer so avoided that





#visulaization of results

plt.plot(n_values, push_results, label='Push', marker='o')
plt.plot(n_values, pull_results, label='Pull', marker='s')
plt.plot(n_values, push_pull_results, label='Push-Pull', marker='^')
plt.xlabel('Number of Agents (n)')
plt.ylabel('Number of Rounds to Inform All')