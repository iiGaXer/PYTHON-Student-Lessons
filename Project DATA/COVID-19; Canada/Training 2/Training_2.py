from matplotlib.legend import Legend
import numpy as np
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import matplotlib.pyplot as mpl
from numpy import arange
import csv
import os
import pandas as pd
import warnings

os.system("rm -rf *.*")
warnings.filterwarnings('ignore')

file_name = 'USA_COVID SHORT.csv'
file_2 = 'Y_true.csv'

data_epochs = []
data_loss = []

Test_csv = pd.read_csv(file_name)


def sigmoid(x):
  # Sigmoid activation function: f(x) = 1 / (1 + e^(-x))
  return 1 / (1 + np.exp(-x))

def deriv_sigmoid(x):
  # Derivative of sigmoid: f'(x) = f(x) * (1 - f(x))
  #* ^ Translated from math to programming
  fx = sigmoid(x)
  return fx * (1 - fx)

def tanh(x):
  return np.tanh(x)

def deriv_tanh(x):
  return 1.0 - tanh(x)**2

def mse_loss(y_true, y_pred):
  # Y_true and y_pred are numpy arrays of the same length.
  return ((y_true - y_pred) * 2).mean()

class OurNeuralNetwork:
 
  '''
  A neural network with:
    - 2 inputs
    - a hidden layer with 2 neurons (h1, h2)
    - an output layer with 1 neuron (o1)

  *** DISCLAIMER ***:
  The code below is intended to be simple and educational, NOT optimal.
  Real neural net code looks nothing like this. DO NOT use this code.
  Instead, read/run it to understand how this specific network works.
  '''
  
  def __init__(self):
    # Weights
    self.w1 = np.random.normal()
    self.w2 = np.random.normal()
    self.w3 = np.random.normal()
    self.w4 = np.random.normal()
    self.w5 = np.random.normal()
    self.w6 = np.random.normal()

    # Biases
    self.b1 = np.random.normal()
    self.b2 = np.random.normal()
    self.b3 = np.random.normal()

  def feedforward(self, x):
    # x is a numpy array with 2 elements.
    h1 = tanh(self.w1 * x[0] + self.w2 * x[1] + self.b1)
    h2 = tanh(self.w3 * x[0] + self.w4 * x[1] + self.b2)
    o1 = tanh(self.w5 * h1 + self.w6 * h2 + self.b3)
    return o1

  def train(self, data, all_y_trues):
    global data_epochs
    global data_loss
    global epochs
    
    '''
    - Data is a (n x 2) numpy array, n = # of samples in the sample data(dataset).
    - All_y_trues is a numpy array with n elements.
      Elements in all_y_trues correspond to those in data.
    '''
    learn_rate = 0.5
    #! Number of maximum epochs/trials/experiments 
    epochs = 1000 # number of times to loop through the entire dataset

    for epoch in range(epochs):
      for x, y_true in zip(data, all_y_trues):
        # --- Do a feedforward (we'll need these values later)
        sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
        h1 = tanh(sum_h1)

        sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
        h2 = tanh(sum_h2)

        sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
        o1 = tanh(sum_o1)
        y_pred = o1

        #! --- Calculate partial derivatives.
        #? --- Naming: d_L_d_w1 represents "partial L / partial w1"
        d_L_d_ypred = -2 * (y_true - y_pred)

        # Neuron o1
        d_ypred_d_w5 = h1 * deriv_tanh(sum_o1)
        d_ypred_d_w6 = h2 * deriv_tanh(sum_o1)
        d_ypred_d_b3 = deriv_tanh(sum_o1)

        d_ypred_d_h1 = self.w5 * deriv_tanh(sum_o1)
        d_ypred_d_h2 = self.w6 * deriv_tanh(sum_o1)

        # Neuron h1
        d_h1_d_w1 = x[0] * deriv_tanh(sum_h1)
        d_h1_d_w2 = x[1] * deriv_tanh(sum_h1)
        d_h1_d_b1 = deriv_tanh(sum_h1)

        # Neuron h2
        d_h2_d_w3 = x[0] * deriv_tanh(sum_h2)
        d_h2_d_w4 = x[1] * deriv_tanh(sum_h2)
        d_h2_d_b2 = deriv_tanh(sum_h2)

        #! --- Update weights and biases
        # Neuron h1
        self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
        self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
        self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

        # Neuron h2
        self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
        self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
        self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

        # Neuron o1
        self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
        self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
        self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

      # Calculating total loss at the end of each epoch/experiment/trial
      if epoch % 10 == 0:
        y_preds = np.apply_along_axis(self.feedforward, 1, data)
        loss = mse_loss(all_y_trues, y_preds)
        print("Epoch %d loss: %.3f" % (epoch, loss))
        data_epochs.append(epoch)
        data_loss.append(float("%.3f" % (loss)))


Data = np.array([
  [-105.75, -43.25],
  [-66.75, -22.25],
  [-15.75, 5.75],
  [188.25, 59.75],
])

all_y_trues = np.array([
  0, # 
  0, # 
  0, # 
  1, # 
])

Preds = np.array([496, 221])
Preds_2 = np.array([514, 285])


network = OurNeuralNetwork()
network.train(Data, all_y_trues)


print("Predictions: %.3f" % network.feedforward(Preds))
print("Predictions: %.3f" % network.feedforward(Preds_2))                           

def Graph():
  my_style = LS('#333366', base_style=LCS)
  my_config = pygal.Config()

  my_config.x_label_rotation = 70
  my_config.show_legend = False
  my_style.title_font_size = 24
  my_style.label_font_size = 14
  my_style.major_label_font_size = 18
  my_config.truncate_label = 15
  my_config.show_y_guides = False
  my_config.width = 1300

  chart = pygal.Line(my_config, style=my_style, x_title='Epochs done', y_title='MSE Calculated')
  chart.title = 'COVID: Training and MSE'
  chart.x_labels = data_epochs
  chart._x_title = "Number of Epochs"
  chart.add('Loss/MSE', data_loss)

  print(data_epochs)
  print(data_loss)

  chart.render_to_file('COVID Training 2.svg')

Graph()