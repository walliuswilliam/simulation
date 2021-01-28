import matplotlib.pyplot as plt

class EulerEstimator:
  def __init__(self, derivative):
    self.derivative = derivative

  def calc_derivative_at_point(self, point):
    return {key:self.derivative[key](point[0], point[1]) for key in self.derivative}
  
  def step_forward(self, point, step_size):
    point1 = point[0]+step_size
    deriv = self.calc_derivative_at_point(point)
    point2 = {key:point[1][key]+deriv[key]*step_size for key in deriv}
    return (point1, point2)
  
  def calc_estimated_points(self, point, step_size, num_steps):
    output_list = []
    output_list.append(point)
    curr_point = point
    for num in range(num_steps):
      curr_point = self.step_forward(curr_point, step_size)
      output_list.append(curr_point)
    for point in output_list:
      new_point = {key: round(value, 5) for key, value in point[1].items()}
      point = (point[0], new_point)
    return output_list

  def plot(self, point, step_size, num_steps):
    points = self.calc_estimated_points(point, step_size, num_steps)
    legend = []
    for variable in points[0][1]:
      x_list = [x[0] for x in points]
      y_list = [y[1][variable] for y in points]
      plt.plot(x_list, y_list)
      legend.append(variable)

    plt.legend(legend)
    plt.style.use('bmh')
    plt.title('Euler Estimator')
    plt.savefig('euler.png')

