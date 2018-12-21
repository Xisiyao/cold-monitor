import math

class Environment:
    def __init__(self):
        self.action_space = ['（-1，-1）', '（0，-1）', '（+1，-1）','（-1，0）', '（0，0）', '（+1，0）','（-1，+1）', '（0，+1）', '（+1，+1）']
        self.n_actions = len(self.action_space)

    def reward(self,T,n_on,n_off,illtime):
        energy=n_on/(n_on+n_off)
        if T<=illtime<T+1:
            for m in range(3600):
                if (n_on+n_off)*m<=(illtime-T)*3600<(n_on+n_off)*(m+1):
                    if (n_on+n_off)*m<=(illtime-T)*3600<(n_on+n_off)*m+n_on:
                        delay=0
                    else:
                        delay=(n_on+n_off)*(m+1)-(illtime-T)*3600
                    break
            '''delay=math.log(delay+1, math.exp(1))
            r = 2*energy-delay'''
            if delay<=2:
                r=1-energy
            else:
                r=-1
        else:
            r=0.5-energy
        return r

    def change(self, n_on,n_off,action):
        if action == 0:n_on=n_on-1;n_off =n_off - 1
        if action == 1:n_on = n_on;n_off =n_off - 1
        if action == 2:n_on = n_on +1;n_off =n_off - 1
        if action == 3:n_on=n_on-1;n_off =n_off
        if action == 4:n_on = n_on;n_off =n_off
        if action == 5:n_on = n_on +1;n_off =n_off
        if action == 6:n_on=n_on-1;n_off =n_off + 1
        if action == 7:n_on = n_on;n_off =n_off +1
        if action == 8:n_on = n_on +1;n_off =n_off +1
        if n_on<=0:n_on=1
        if n_on >=3600: n_on = 3599
        if n_off<=0:n_off=1
        if n_off >=3600: n_off = 3599

        return n_on,n_off
