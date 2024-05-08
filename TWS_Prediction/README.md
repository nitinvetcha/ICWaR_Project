Data.txt contains the values of 6 predictor variables as well as the target TWS variable from 2002-07-31 to 2016-02-29 with a monthly timestamp. Train : Test split used is 60 : 40. performance_metrics.py contains the evaluation methods used, which are RMSE, NRMSE, NSE and Kling Gupta Efficiency.
# ML / DL Methods Implemented
### 1. Partial Least Squares Regression
### 2. Neural Network Regression
As the name suggests, we use neural networks for regression except that the output layer is now modified i.e., when used for classification, it was normally a softmax layer giving normalized probabilities for each of the class involved. Data containing the 6 predictor variables would be flattened and given to the input layer, which is then processed to a hidden layer before finally resulting in the output. The involved weight matrices and biases would be learned using backpropagation using stochastic graident descent.
<p align="center">
<img src = https://github.com/nitinvetcha/ICWaR_TWS_Prediction/assets/118665106/6d75b9f1-229e-4649-a87d-d63d5301716e />
</p>
<br />The implementation in NNR.ipynb contains a neural network with one hidden fully connected layer of 32 neurons with ReLU activation. The loss function for computing gradients was the standard mean squared error and optimization was performed using Adam's method.

### 3. LSTM
For sequence modelling, recurrent neural networks have been proven to be a very promising architecture. However, it suffers from exploding gradient problem (which can be resolved using clipping) and vanishing gradient problem. To solve the latter, LSTM's and GRU's have been developed which overcome the problem using gates. Our data inherently has a timestamp component, thereby facilitating the implementation of these architectures. Below is an image (from Stanford CS:230) of a cell from the LSTM block, which consists of 4 gates - update, relevance, forget and output. 
<p align="center">
<img src = https://github.com/nitinvetcha/ICWaR_Project/assets/118665106/740b840f-acd9-4f80-a013-de5e5cc96fe5 width="400" />
</p>
<br /> The implementation of LSTM in LSTM.ipynb file contains 2 LSTM layers and 2 dense layers of 32 neurons and 1 neuron to compute the prediction. The loss function for computing gradients was the standard mean squared error and optimization was performed using Adam's method.
