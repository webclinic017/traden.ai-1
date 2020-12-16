from models import *
from simulation import Simulation
import matplotlib.pyplot as plt


class ComparingSimulations:
    def __init__(self, list_of_simulations, executed=False):
        self.simulations = list_of_simulations
        self.executed = executed

    def execute(self, no_executions=1):
        for simul in self.simulations:
            simul.execute(no_executions)
        self.executed = True
 
    def get_expected_metric(self, metric="profit"):
        if not self.executed:
            self.execute()
        return [sum(map(lambda x: float(x[metric]), simul.get_results())) / len(simul.get_results()) for simul in self.simulations]

    def get_best_simulation_by_metric(self, metric="profit"):
        if not self.executed:
            self.execute()
        expected_metric_values = self.get_expected_metric(metric=metric)
        return self.simulations[expected_metric_values.index(max(expected_metric_values))]

    def get_worst_simulation_by_metric(self, metric="profit"):
        if not self.executed:
            self.execute()
        expected_metric_values = self.get_expected_metric(metric=metric)
        return self.simulations[expected_metric_values.index(min(expected_metric_values))]
    
    def get_graph_comparison(self, mode="daily"):
        plt.xlabel("Time ({})".format(mode))
        plt.ylabel("Capital")    
        for simul in self.simulations:
            X = []
            Y = []
            for el in simul.get_evaluations(mode=mode):
                Y.append(sum(el[1]) / len(el[1]))
            X = range(1,len(Y) + 1)
            plt.plot(X,Y, label="Simulation {}".format(str(simul.get_id())))
        plt.legend(loc='best')
        plt.show()

if __name__=="__main__":
    simul1 = Simulation(1,4000,["AMZN"],"2019-01-01","2020-10-01",buyAll)
    simul2 = Simulation(2,4000,["AMZN"],"2019-01-01","2020-10-01",buyRandom)
    comp = ComparingSimulations([simul1,simul2])
    comp.execute(no_executions=1)
    print(comp.get_expected_metric(metric="profit_percentage"))
    print(comp.get_graph_comparison())

    
