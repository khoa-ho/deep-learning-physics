# Progress Report

[//]: # (Image References)

[image0]: ./image/mass-spring1.png "Mass-on-spring"
[image1]: ./image/generic_sine_training.png "Visualization of training data for generic sine"
[image2]: ./image/lorentz_attractor.png "Lorenz attractor"
[image3]: ./image/lorentz_z_test.png "Prediction of Lorentz z-axis"
[image4]: ./image/double_pendulum1.png "Double pendulum during 'regular' chaos"

### 02-21-2018
- Learned about the deployment options for Jupyter Notebooks at scale on XSEDE resources. [Webinar](https://www.youtube.com/watch?v=BE6tRuJtq8c "ECSS Symposium December 19 2017")
- Learned about PSC's support for the deep learning package TensorFlow (the backend of Keras). [Webinar](https://www.youtube.com/watch?v=c5ItG-vg39s "ECSS Symposium February 2018")


### 02-28-2018
#### Added
- A decaying exponential term in the function expression. This would mimics damping in all physical systems.

#### Changed
- Updated the syntax for Keras 2

#### Known issues
- The current implementation only works for small exponential decay constant, less than or equal to 0.001.
- The prediction tends to follow the data to closely, including all the small fluctuation of noise. Ideally, we want the network to learn the general function that describes the data as opposed to 'memorizing' the data.


### 03-05-2018
#### Added
- The function is now the product of two sine waves with different period. This mimics the period doubling of nonlinear dynamical system.
- The model now employs Bidirectional LSTM architecture that has been shown to be more effective at learning sequential data (specifically natural language sentences)

#### Changed
- Used `CuDNNLSTM` layer instead of the default `LSTM` version. This is a fast LSTM implementation backed by CuDNN (NVIDIA CUDA® Deep Neural Network library), a GPU-accelerated library of primitives for deep neural networks. On GPU-enabled machine, this change really speeds up training and inference.

#### Fixed
- I found the cause for the failure of the model at high exponential decay constant:
    - If noise is not modulated by the exponential function, it will overwhelm the signal near the end of the data sequence which is where test data is picked from. We can modulate it in simulated environment but in physical experiments, we may have to discard data near the end of the motion.
    - So in the current implementation, the noise will also decay exponentially. This allows the model to learn at much higher level of decaying.

#### Known issues
- The prediction tends to follow the data to closely, including all the small fluctuation of noise. Ideally, we want the network to learn the general function that describes the data as opposed to 'memorizing' the data.


### 03-07-2018
#### Added
- Made the period much more complex. The network is still able to capture the data well.

#### Changed
- Drastically reduced the complexity of the model (from 3 layers to 1, from 300 LSTM units to 10). Apparently, this makes the prediction look much more like a pure function (less noisy). So since the function behind the simulated data is simple, a simple neural network is better at capturing that. A more complex network will just follow the noise more closely, which is undesirable for our purpose.

#### To try
- 2-dimensional data, non linear data
- Experimental data from Chad's mass-on-spring system


### 03-10-2018
#### Added
- Replaced simulated data with experimental mass-spring data
    - The network seems to capture the experimental data very well
    ![alt text][image0]
- Moving-average function to smooth data if necessary

#### To do
- change the generator function from capturing/partial predicting to complete predicting
- 2-dimensional data, non linear data


### 04-06-2018
#### Changed
- Reducing the number of neurons in the LSTM layer. It turned out that 5 was the smallest number of neurons that allowed the network to generalize without compromising the accuracy.


### 04-11-2018
#### Added
- Implemented the preprocessing steps and network architecture to perform prediction on generic sinusoidal waves with the same amplitude but varying period. More specifically, during the training step, the network was exposed to the time series of waveforms of different frequencies. Its predictive capability was then tested using a new waveform with unfamiliar (i.e. the network wasn't trained on) period.
- Following is the visualization of the training dataset
![alt text][image1]


### 04-18-2018
#### Added
- Tested the network on the Lorentz system (one dimension at a time)
- 3D plot of the Lorentz system
![alt text][image2]
- The network demonstrated its ability to predict effectively the each dimension of the Lorentz system. Following is the result on the test dataset of z-axis.
![alt text][image3]


### 04-25-2018
#### Added
- Tested the network on simulated double pendulum data (both dimensions)
- The network's prediction was decent for the 'regular' chaos regime where one of the arm doesn't spin too many rounds in-place.
![alt text][image4]
