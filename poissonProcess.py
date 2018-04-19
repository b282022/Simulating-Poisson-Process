import numpy as np
import matplotlib.pyplot as plt

def poissonProcess(t, rate, h):
    timeArray = np.linspace(0, t, int((t - 0) / h) + 1)
    numberOfEvents = np.zeros(len(timeArray))
    for i in range(len(timeArray) - 1):
        if np.random.rand() <= rate * h:
            numberOfEvents[i + 1] = numberOfEvents[i] + 1
        else:
            numberOfEvents[i + 1] = numberOfEvents[i]
    return timeArray, numberOfEvents

def generateDistributionOfPoissonProcess(t, rate, experiments=100, h=0.01):
    numberOfEventsAtT = np.zeros(experiments)

    for i in range(experiments):
	timeArr, numberOfEventsArr = poissonProcess(t, rate, h)
	numberOfEventsAtT[i] = numberOfEventsArr[-1]

    plt.hist(numberOfEventsAtT, normed=True, bins=np.arange(
	np.min(numberOfEventsAtT), np.max(numberOfEventsAtT), 1.0), label=r'Distribution of $N(t)$')
    plt.axvline(t * rate, color='r', label='Mean of Poisson Random variable')

    plt.xlabel(r'$N(t)$')
    plt.ylabel('Normalized frequency')
    plt.legend()

    plt.savefig("DistributionOfN(t)ForPoissonProcess_step_" + str(h) + 
	"_experiments_" + str(experiments) + ".png", dpi=300)
    plt.show()

generateDistributionOfPoissonProcess(100, 0.1, 100000, 0.1)
