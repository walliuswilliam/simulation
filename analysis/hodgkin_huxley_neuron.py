import sys
sys.path.append('src')
from euler_estimator import EulerEstimator
import math
import matplotlib.pyplot as plt



def s(t):
  points = [[10,11],[20,21],[30,40],[50,51],[53,54],[56,57],[59,60],[62,63],[65,66]]
  for point in points:
    if point[0] <= t <= point[1]:
      return 150
  return 0


def g_na(V,m,h):
  gna = 120
  return gna*(m**3)*h

def g_k(V,n):
  gk = 36
  return gk*(n**4)

def g_l(V):
  gl = 0.3
  return gl



def I_na(V,m,h):
  V_na = 115
  return g_na(V,m,h)*(V-V_na)

def I_k(V,n):
  V_k = -12
  return g_k(V,n)*(V-V_k)

def I_l(V):
  V_l = 10.6
  return g_l(V)*(V-V_l)


def beta_n(V):
  return 0.125*math.exp(-V/80)

def beta_m(V):
  return 4*math.exp(-V/18)

def beta_h(V):
  return 1/(math.exp(0.1*(30-V))+1)


def alpha_n(V):
  return (0.01*(10-V))/(math.exp(0.1*(10-V))-1)

def alpha_m(V):
  return (0.1*(25-V))/(math.exp(0.1*(25-V))-1)

def alpha_h(V):
  return 0.07*math.exp(-V/20)



def dV_dt(t,x):
  V = x['V']
  n = x['n']
  m = x['m'] 
  h = x['h']
  c = 1
  return (1/c)*(s(t)-I_na(V,m,h)-I_k(V,n)-I_l(V))

def dn_dt(t,x):
  V = x['V']
  n = x['n']
  return alpha_n(V)*(1-n)-beta_n(V)*n

def dm_dt(t,x):
  V = x['V']
  m = x['m']
  return alpha_m(V)*(1-m)-beta_m(V)*m

def dh_dt(t,x):
  V = x['V']
  h = x['h']
  return alpha_h(V)*(1-h)-beta_h(V)*h


derivatives = {
  'V': dV_dt,
  'n': dn_dt,
  'm': dm_dt,
  'h': dh_dt}
euler = EulerEstimator(derivative = derivatives)

initial_values = {
  'V': 0,
  'n': (alpha_n(0))/(alpha_n(0)+beta_n(0)),
  'm': (alpha_m(0))/(alpha_m(0)+beta_m(0)),
  'h': (alpha_h(0))/(alpha_h(0)+beta_h(0)),}


initial_point = (0, initial_values)

def hodgkin_plot(euler, point, step_size, num_steps):
  plt.style.use('bmh')
  points = euler.calc_estimated_points(point, step_size, num_steps)
  legend = []
  for variable in points[0][1]:
    if variable == 'V':
      x_list = [x[0] for x in points]
      y_list = [y[1][variable] for y in points]
      plt.plot(x_list, y_list)
  
  t_values = [step_size*t for t in range(num_steps)]
  s_values = [s(t) for t in t_values]

  plt.plot(t_values, s_values)
  plt.legend(['Voltage', 'Stimulus'])
  plt.savefig('hodgkin_huxley.png')

hodgkin_plot(euler, initial_point, 0.01, 8000)

print('done')