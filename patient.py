import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

class ColdTime:
    def __init__(self,number):
        np.random.seed(0)
        self.number=number
        #上午
        self.mu = 12  # mean of distribution
        self.sigma = 1  # standard deviation of distribution
        self.xl_mor=[0]*self.number
        for n in range(self.number):
            while True:
                data = np.random.normal(self.mu, self.sigma, 1)
                if 9 <= data[0] <15:
                    data[0]=round(data[0], 4)
                    if data[0] != 15:
                        self.xl_mor[n] = data[0]
                        break

        #下午
        self.mu1 = 18  # mean of distribution
        self.sigma1 = 1  # standard deviation of distribution
        self.xl_aft = [0] * self.number
        for n in range(self.number):
            while True:
                data = np.random.normal(self.mu1, self.sigma1, 1)
                if 15 <= data[0] < 21:
                    data[0] = round(data[0], 4)
                    if data[0]!=21:
                        self.xl_aft[n] = data[0]
                        break

    def getfre(self):
        fre=[0]*12
        for m in range(6):
            num_mor = 0
            num_aft = 0
            for n in range(self.number):
                if m+9<=self.xl_mor[n]<m+10:
                    num_mor+=1
                if m+15<=self.xl_aft[n]<m+16:
                    num_aft+=1
            fre[m]=num_mor/self.number
            fre[m+6]=num_aft/self.number
        return fre


    def getilltime_m(self):
        return self.xl_mor

    def getilltime_a(self):
        return self.xl_aft

    def drawing(self):
        num_bins = 12
        fig, ax = plt.subplots(2)

        # the histogram of the data
        xl=[0]*self.number*2
        xl=self.xl_mor+self.xl_aft
        n, bins, patches = ax[0].hist(xl, num_bins, normed=0)
        ax[0].set_xlabel('time')
        ax[0].set_ylabel('Number of episodes')
        ax[0].set_title(r'when will a patient get cold in the morning')

        # add a 'best fit' line
        y = mlab.normpdf(bins, self.mu, self.sigma)
        y1 = mlab.normpdf(bins, self.mu1, self.sigma1)
        yy=y+y1
        ax[1].plot(bins, yy, '--')
        ax[1].set_xlabel('time')
        ax[1].set_ylabel('Probability density')
        ax[1].set_title(r'Curve Fitting')

        # Tweak spacing to prevent clipping of ylabel
        fig.tight_layout()

