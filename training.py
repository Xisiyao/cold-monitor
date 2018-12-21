from patient import ColdTime
from qlearning import q_learning_model
from environment import Environment
import numpy as np
import matplotlib.pyplot as plt
import math

def update(number):
    s_ = np.zeros((1, 3), int)
    number_time=0
    Eva = [0] * 6
    for n in range(0,12):
        s[n]=[n+9,5,5]
    for episode in range(0,number):
        for n in range(0,6):
            s_[0] = [n+9,0,0]
            while True:
                # 选择一个动作
                action = RL.choose_action(str(s[n]))

                # 执行这个动作得到反馈（下一个状态s 奖励r ）
                s_[0][1],s_[0][2]= env.change(s[n][1],s[n][2],action)
                r=env.reward(n+9,s_[0][1],s_[0][2],illtime[0][episode])

                # 更新状态表
                RL.rl(str(s[n]), action, r, str(s_[0]))

                s[n][1] = s_[0][1]
                s[n][2] = s_[0][2]
                break

        for n in range(6,12):
            s_[0] = [n+9,0,0]
            while True:
                # 选择一个动作
                action = RL.choose_action(str(s[n]))

                # 执行这个动作得到反馈（下一个状态s 奖励r ）
                s_[0][1],s_[0][2]= env.change(s[n][1],s[n][2],action)
                r=env.reward(n+9,s_[0][1],s_[0][2],illtime[1][episode])

                # 更新状态表
                RL.rl(str(s[n]), action, r, str(s_[0]))

                s[n][1] = s_[0][1]
                s[n][2] = s_[0][2]
                break
        print(episode)

        if (episode+1)%300==0:
            eva = 0
            for n in range(0, 12):
                eva = eva + (f[n] - s[n][1]/(s[n][1]+s[n][2])) ** 2
            Eva[number_time]=math.sqrt(eva)
            number_time+=1
    return Eva

if __name__ == "__main__":
    number=720
    coti = ColdTime(number)
    env=Environment()
    illtime=np.zeros((2,number))
    RL= q_learning_model(actions=list(range(env.n_actions)))
    illtime[0] = coti.getilltime_m()
    illtime[1] = coti.getilltime_a()
    s = np.zeros((12, 3),int)
    f = coti.getfre()

    Evaluation=update(number)

    #画学习结果
    x= np.zeros((1, 12))
    y = np.zeros((1, 12))
    for n in range(0,12):
        x[0][n]=s[n][0]
        y[0][n]=s[n][1]/(s[n][1]+s[n][2])
    plt.plot(x[0],y[0])

    #画评价函数




    #画病人发病时间
    coti.drawing()

    plt.show()
    xbox=0
    xbox=xbox




