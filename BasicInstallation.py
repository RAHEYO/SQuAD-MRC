# prompt: install tensorflow, pennylane, and all the related libraries that may be needed to use those two libraries.

!pip install autograd tensorflow jax jaxlib 
!pip install pennylane
!pip install pennylane-lightning pennylane-lightning[gpu]
!pip install numpy


# prompt: import tensorflow and pennylane

def import():
  import tensorflow as tf
  import pennylane as qml
  import numpy as np
