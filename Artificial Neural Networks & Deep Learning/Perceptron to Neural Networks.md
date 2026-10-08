### Where it started
In the 1940s researcher were trying to use the model of the brain as a computation for computers. It contains $10^{11}$ neurons, which would be the computational units, and multiple thousand of interconnections for each neurons called synapses.
The computational model of the brain is:
- Distributed among simple non linear units
- Redundant and thus fault tolerant
- Intrinsically parallel
The invention can't be attributed to any particular research as there were many that added and refined it. 
### Perceptron
What ended up modeling a neuron is the so called Perceptron. The Perceptron is a simple mathematical function that takes multiple data points as input and produces an output.

It is composed of:
- Multiple input data, but always fixed size; called $x$
- A weight value for each of these inputs, they are used to scale the input by multiplication; called $w$
- An accumulation of the scaled inputs
- A bias that adds a fixed shift independent of inputs; called $b$
- An activation function that allows to obtain a simple result from the rest of the operations; called $h$

The resulting formula is:
$h(x|w,b) = h(\sum_{i=1}^{I} w_i x_i - b) = h(\sum_{i=0}^{I} w_i x_i) = h(w^Tx)$
where we adjusted the $w$ and $x$ vector to account for the bias like this:
- The first weight is the bias $w = (-b,w_1,w_2,...,w_I)$;
- The first input is 1 $x = (1,x_1,x_2,...,x_I)$.

The Perceptron is a malleable tool, it can be used to represent any logic gates by just tuning the values of the weights or many complex mathematical functions, useful for separating regions in spaces for classification.

#### Hebbian Learning
*"The strength of a synapse increases according to the simultaneous activation of the relative input and the desired target" (Donald  Hebb, 1949)*

Hebbian learning is a model invented by Donald Hebb that is able to train a Perceptron and make it learn *online*.
It can be summarized by the following:
- Start from a random initialization of the weights $w^0$
- Adjust the weights at each step $k$, $w_i^{k+1} = w_i^{k} + \Delta w_i^{k}$
- Update the gradient $\Delta w_{i}^k = \eta \cdot x_{i}^k \cdot t^k$
  Where we have:
	- $\eta$: learning rate
	-  $x_i^k$: the $i^{th}$ perceptron input at time $k$
	- $t^k$: the desired output at time $k$
This procedure always converges, but not to the same weights because it stops when there are not more errors and, depending on the initial value of the weights, that state could differ.
It will be later generalized and called Gradient Descent.

### Feed Forward Neural Networks
Stacking multiple layers of Perceptrons that feed into each other, allows to create more complex mathematical functions. 
For example with a certain number of layers we can have:
- 1 layer: half bounded by hyperplanes
- 2 layers: convex open or limited regions
- 3 or more layers: arbitrary regions (complexity limited by the number of nodes)

#### Structure
FFNN are a composed of multiple perceptrons arranged in layers, where each layer can also have multiple perceptrons, and every element of each layer is intraconnected to every other adjecent element.
The layers are categorized as:
- Input layer: inputs and initial bias are fed to every perceptron of the next layer
- Multiple hidden layers: the number can vary
- Output layer: final activation function that return a finite result

#### Activation Function
For activation function there are multiple choice that would influence the functionality of the network, the most common ones historically are:
- Linear:
	- $g(a) = a$
	- $g'(a) = 1$
- Sigmoid:
	- $g(a) = \frac{1}{1 + e^{-a}}$
	- $g'(a) = g(a)(1 -  g(a))$
- Tanh:
	- $g(a) = \frac{e^a - e^{-a}}{e^a + e^{-a}}$
	- $g'(a) = 1 - g(a)^2$
The choice of activation function is based on the result obtained, but also on how simple is the derivate, for example linear is just 1.

For the activation function in the output layer, the choice depends on what the task is:
- In Regression the output spans the whole $\mathbb{R}$ domain:
	- Use a linear activation function for the output neuron
- In Classification with two classes, choose according to their coding:
	- Two classes $\{\Omega_{0} = -1, \Omega_{1} = +1\}$ then use Tanh output function
	- Two classes $\{\Omega_{0} = 0, \Omega_{1} = 1\}$ then use Sigmoid output function (it can be interpreted as class posterior probability)
- When dealing with multiple classes ($K$) use as many neuron as classes:
	- Classes are coded as $\{\Omega_{0} = [0\space 0\space 1], \Omega_{1} = [1\space 0\space 0]\}$ 
	- Output neurons use a softmax unit $y_{k} = {\frac{e^{z_{k}}}{\sum_{k} e^{z_{k}}}}$  

#### Universal approximation theorem
*"A single hidden layer feedforward neural network with S shaped activation functions can approximate any measurable function to any desired egree of accuracy on a compact set"*

This is the formulation of the Universal approximation theorem (Kurt Hornik, 1991)

It means that regardless of the function we are learning, a single layer can represent it, but:
- It does not mean a learning algorithm can find the necessary weights
- In the worst case, an exponential number of hidden units may be required
- The layer may have to be an unfeasible large size and may fail to learn and generalize

### Supervised Learning
