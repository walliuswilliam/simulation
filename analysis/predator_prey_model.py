import sys
sys.path.append('src')
from euler_estimator import EulerEstimator


derivatives = {'deer': (lambda t,x: 0.6*x['deer']-0.05*x['wolves']*x['deer']),'wolves': (lambda t,x: -0.9*x['wolves']+0.02*x['wolves']*x['deer'])}
euler = EulerEstimator(derivative = derivatives)

initial_values = {'deer': 100, 'wolves': 10}
initial_point = (0, initial_values)

euler.plot(point=initial_point, step_size=0.001, num_steps=100000)