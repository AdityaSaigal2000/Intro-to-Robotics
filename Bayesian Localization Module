import numpy as np
import matplotlib.pyplot as plt


x=np.array(range(2,14))
y=np.zeros(12)
state_prob=[[2,0.0909090909],[3,0.0909090909],[4,0.0909090909],[5,0.0909090909],[6,0.0909090909],
            [7,0.0909090909],[8,0.0909090909],[9,0.0909090909],[10,0.0909090909],[11,0.0909090909],
            [12,0.0909090909]]
control_inputs=[1,1,1,1,1,1,1,1,0,1,1,1]
color_inputs=['o','y','g','b','n','g','b','g','o','y','g','b']
measurement_model={'b':{'b':0.6,'g':0.2,'y':0.05,'o':0.05,'n':0.1},
                   'g':{'b':0.20,'g':0.60,'y':0.05,'o':0.05,'n':0.1},
                   'y':{'b':0.05,'g':0.05,'y':0.65,'o':0.15,'n':0.1},
                   'o':{'b':0.05,'g':0.05,'y':0.2,'o':0.60,'n':0.1}}
colors=[(2,'y'),(3,'g'),(4,'b'),(5,'o'),(6,'o'),(7,'g'),(8,'b'),(9,'o'),(10,'y'),(11,'g'),(12,'b')]
state_model=[[1,[1,0.85],[0,0.1],[-1,0.05]],
             [0,[0,0.9],[-1,0.05],[1,0.05]],
             [-1,[-1,0.85],[0,0.10],[1,0.05]]]
prediction=state_prob

for i in range (0,11):
    y[i]=state_prob[i][1]
for i in range (0,12):
    prediction=[[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0]]
    accum=0
    for j in range (0,11):
        prediction[j][1]=0
        for k in range (0,11):
            if(abs(prediction[k][0]-prediction[j][0])>abs(control_inputs[i])):
                prediction[j][1]=prediction[j][1]
            elif(control_inputs[i]==prediction[j][0]-prediction[k][0]):
                prediction[j][1]=(prediction[j][1]+state_model[-1*control_inputs[i]+1][1][1]*state_prob[k][1])
            elif(control_inputs[i]==prediction[k][0]-prediction[j][0]):
                prediction[j][1]=(prediction[j][1]+state_model[-1*control_inputs[i]+1][3][1]*state_prob[k][1])
            elif(control_inputs[i]==0):
                prediction[j][1]=prediction[j][1]+0.1*state_prob[k][1]
            if(k==0 and j==10):
                if(control_inputs[i]==-1): 
                    prediction[j][1]=(prediction[j][1]+state_model[-1*control_inputs[i]+1][1][1]*state_prob[k][1])
                if(control_inputs[i]==1):
                    prediction[j][1]=(prediction[j][1]+state_model[-1*control_inputs[i]+1][3][1]*state_prob[k][1])
                if(control_inputs[i]==0):
                     prediction[j][1]=prediction[j][1]+0.1*state_prob[k][1]
            elif(k==10 and j==0):
                if(control_inputs[i]==1): 
                    prediction[j][1]=(prediction[j][1]+state_model[-1*control_inputs[i]+1][1][1]*state_prob[k][1])
                if(control_inputs[i]==-1):
                    prediction[j][1]=(prediction[j][1]+state_model[-1*control_inputs[i]+1][3][1]*state_prob[k][1])
                if(control_inputs[i]==0):
                     prediction[j][1]=prediction[j][1]+0.1*state_prob[k][1]
    for j in range (0,11):
        color=colors[j][1]
        accum=accum+measurement_model[color][color_inputs[i]]*prediction[j][1]
        
    for j in range (0,11):
        color=colors[j][1]
        state_prob[j][1]=measurement_model[color][color_inputs[i]]*prediction[j][1]/accum
    
    for j in range (0,11):
        y[j]=state_prob[j][1]
    bars = range(2,12)

    title="State Estimate after " + str(i+1) + " Measurements"
    fig, axs =plt.subplots()
    axs.bar(x,y,color=['yellow', 'green', 'blue', 'orange', 'orange', 'green', 'blue', 'orange','yellow','green','blue'], edgecolor='black')
    plt.xticks(x, bars)
    axs.set_title(title)
    axs.set_xlabel("Colour Index")
    axs.set_ylabel("Probability")     

    fig_size = plt.rcParams["figure.figsize"]
 
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 6
    fig_size[1] = 4
    plt.rcParams["figure.figsize"] = fig_size 
