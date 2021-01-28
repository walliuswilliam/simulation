import sys
sys.path.append('src')
from euler_estimator import EulerEstimator
import matplotlib.pyplot as plt





# def plot_sir(self, point, step_size, num_steps):
    


    
#   points = self.calc_estimated_points(point, step_size, num_steps)
#   x_list = []
#   y_list = []
#   for pair in points:
#     x_list.append(pair[0])
#     y_list.append(pair[1])
#   plt.style.use('bmh')
#   plt.plot(x_list, y_list)
#   plt.title('Euler Estimator')
#   plt.savefig('euler.png')


derivatives = {'S': (lambda t,x: -0.0003*x['S']*x['I']),'I': (lambda t,x: 0.0003*x['S']*x['I'] -0.02*x['I']),'R': (lambda t,x: 0.02*x['I'])}
euler = EulerEstimator(derivative = derivatives)

initial_values = {'S': 1000, 'I': 1, 'R': 0}
initial_point = (0, initial_values)

euler.plot(point=initial_point, step_size=1, num_steps=300)