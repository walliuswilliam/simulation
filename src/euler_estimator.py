# import matplotlib.pyplot as plt

class EulerEstimator:
  def __init__(self, derivative):
    self.derivative = derivative

  def calc_derivative_at_point(self, point):
    return {key:self.derivative(point[0]) for key in self.derivative}
  
  def step_forward(self, point, step_size):
    point1 = point[0]+step_size
    deriv = self.calc_derivative_at_point(point)
    point2 = point[1]+deriv*step_size
    return (point1, point2)
  
  def calc_estimated_points(self, point, step_size, num_steps):
    output_list = []
    output_list.append(point)
    curr_point = point
    for num in range(num_steps):
      curr_point = self.step_forward(curr_point, step_size)
      output_list.append(curr_point)
    return output_list

  # def plot(self, point, step_size, num_steps):
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

