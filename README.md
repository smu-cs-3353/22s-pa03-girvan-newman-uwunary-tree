# Medium Articles

We wrote articles discussing the theory behind these implementations! Please read:
- Part One: [Why Girvan-Newman](https://medium.com/@trevordohm/why-girvan-newman-68506e824e93) </br>
- Part Two: [Community Detection With Neural Networks](https://gmongaras.medium.com/community-detection-with-neural-networks-2e6c79a28d0c)

# Contents

- [General Project Information](#general-project-information)
- [Project Description](#project-description)
  - The Problem
  - The Implementation
    - Community Detection
    - Girvan Newman
    - Neural Network
  - Example Output
    - Girvan Newman - Football
    - Girvan Newman - Dataset 4
    - Neural Network Note
    - Neural Network - Dataset 4
  - Final Results
    - Algorithm Time
    - Algorithm Accuracy Aginst Each Other
    - Algorithm Accuracy Aginst The Graph Structure
- [Installation, Configuration, Execution](#installation-configuration-execution)
  - Project Installation
  - Cpp Project Configuration
  - Cpp Main Project Execution
  - Python Project Configuration
  - Python Main Project Execution
    - All Script Parameters
    - Neural Network Parameters
    - Girvan Newman Parameters
  - Network Training
  - Network Data Generation
    - Model Configuration
  - Data Generation
  - GML To GraphML Conversion
- [References](#references)

# General Project Information

**Title:** Project 3 - [Community Detection in Networks](https://docs.google.com/document/d/1kzxZlTZV8M57DKrXZFGYVOAaDaBW9JjPwcKYHjFEC04/edit)</br>
**Department:** Computer Science</br>
**Professor:** Dr. Fontenot</br>

**Names:** Gabriel Mongaras and Trevor Dohm</br>
**Date:** 4 / 11 / 2022</br>

**Course:** Fundamentals of Algorithms</br>
**Section:** CS 3353-001</br>

# Project Description

## The Problem

In this project, we aim to implement the community detection algorithm proposed by Girvan and Newman, otherwise known as the Girvan-Newman Algorithm, for undirected, unweighted graphs. We implement community detection in both Cpp and Python, including a Neural Network to predict the solution to this problem.

## The Implementations

### Community Detection

Before discussing the implementations of community detection seen in this repository, let us first identify the problem at hand. Community Detection refers to the automated discovery of highly interconnected collections of nodes in a graph. For example, when looking at American Football Conferences, one would expect clear patterns, or communities, to emerge, since certain teams are more inclined to play against each other. The methods below attempt to solve this problem.

### Girvan Newman

The first method we looked at in order to solve the communty detection problem was the Girvan-Newman Algorithm, per the requirements in the project description linked above. The Girvan-Newman Algorithm relies on repeatedly calculating edge betweenness, a value for each edge which represents the number of shortest paths between all pairs of nodes that travel through said edge. After calculating betweenness for all edges, the edge with the highest credit is removed, and betweenness is recalculated for all remaining edges.
To know when to stop removing edges, a value known as Modularity is calculated, and when the Modularity increases and immediately sharply decreases, we stop the program and take the graph at best Modularity in order to achieve optimal community detection. In other words, this calculation allows us to optimize our program.
If you would like to learn more about the implementation, you can read this [medium article](https://medium.com/@trevordohm/why-girvan-newman-68506e824e93).

### Neural Network

The second method we used to solve the community detection problem was through the use of a nueral network. Instead of using the graph structure, the graph is encoded to an <i>N</i>x<i>N</i> matrix where <i>N</i> is the number of nodes in the graph. This matrix encodes how each node relates to each other node in the graph and is called the modularity matrix. This matrix is computed as follows:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\color{white}\Large\B_{ij} = A_{ij} - \frac{k_i k_j}{2m}"></br>
</p>
- A_ij - Number of edges between node i and j (usually 0 or 1)</br>
- k_i - Degree of node i</br>
- k_j - Degree of node j</br>
- m - Number of edges in the old graph</br>
</br>
This matrix is then fed through a neural network which encodes the matrix into a <i>d</i>x<i>N</i> matrix where <i>d</i> is a new size to encode each row in the matrix. We can then use a clustering algorithm like <i>k</i>-means clustering to classify each node into <i>k</i> number of communities and use these communities as the predicted communities.

If you would like to learn more about the implementation, you can read this [medium article](https://gmongaras.medium.com/community-detection-with-neural-networks-2e6c79a28d0c).

## Example Output

Below is example output from both algorithms. Each output is split into two parts:
1. The graphical representation of the groups
2. Each group and the nodes in them

### Girvan Newman - Football
<img src="https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/blob/main/README_data/Python/GN_Football_Graph.png"></br>

```
Class 0: NewMexico, BrighamYoung, SanDiegoState, Wyoming, Utah, ColoradoState, AirForce, NevadaLasVegas
Class 1: NorthCarolinaState, FloridaState, Virginia, GeorgiaTech, Duke, NorthCarolina, Clemson, WakeForest, Maryland
Class 2: PennState, Iowa, Northwestern, Wisconsin, Michigan, OhioState, Purdue, Minnesota, Illinois, MichiganState, Indiana
Class 3: Kansas, KansasState, IowaState, Baylor, TexasTech, Nebraska, Oklahoma, TexasA&M, Colorado, Texas, Missouri, OklahomaState
Class 4: ArizonaState, SouthernCalifornia, UCLA, Arizona, Washington, Oregon, WashingtonState, Stanford, OregonState, California
Class 5: ArkansasState, NorthTexas, UtahState, BoiseState, Idaho, NewMexicoState
Class 6: EasternMichigan, NorthernIllinois, Toledo, BallState
Class 7: Alabama, Auburn, Florida, Kentucky, Vanderbilt, SouthCarolina, MississippiState, Mississippi, Georgia, Tennessee, LouisianaState, Arkansas
Class 8: Buffalo, Akron, Kent, BowlingGreenState, MiamiOhio, Ohio, Marshall
Class 9: BostonCollege, VirginiaTech, WestVirginia, Syracuse, Pittsburgh, Temple, Rutgers, MiamiFlorida
Class 10: Houston, EastCarolina, Louisville, SouthernMississippi, Memphis, Tulane, Cincinnati, AlabamaBirmingham, Army
Class 11: Rice, FresnoState, SouthernMethodist, Nevada, SanJoseState, TexasElPaso, Tulsa, TexasChristian, Hawaii
Class 12: WesternMichigan, CentralFlorida, CentralMichigan, Connecticut, LouisianaTech, LouisianaMonroe, MiddleTennesseeState, Navy, NotreDame, LouisianaLafayette
Accuracy: 0.8608695652173913
```

### Girvan Newman - Dataset 4
<img src="https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/blob/main/README_data/Python/GN_dataset4.png"></br>

```
Class 0: Teri Holstein, Franklin Davis, Jennifer Morris, Bonnie Aman, Spencer Patrick, Ralph Carradine, Sarah Ramirez, Edwin Morley, Alfredo Petty, Vada Isom, Thomas Franko, Robert Coleman, Michael Farr, Alexandra Livingston, Ella Johnson, Irene Robinson, Robert Roller, James Sindorf, Allen Poole, Thelma Wiggins, Dianna Spencer, Samantha Stone, Lillian Canales, Connie Funk, Curt Ritter, Daniel Montoya, Susanne Rivas, Eric Dietz, Tommie Lutes, James Mauk, Victor Fry, Robert Castro, Idell Nixon, Shawn Worrell, Roy Larmon, Jamie Evans, Janet Savitts, Duane Edwards, Amy Pratt, Rhonda Marshall, Miguel Hibbs, John Wiederwax, George Nehring, David Shaw, Denise Moller, Angelina Gordon, James Smith, Robert Meade, Josefina Orear, Alexander Landis, Theresa Taylor, Alexander Lloyd, Sussy Baka, Laura Escudero, Ben Sullivan, Jennifer Hunter, Ginger Dower, Donte Bringle, Melissa Gibson, Sue Eby, Fred Foster, Kenneth Gleaton, Gary Cox, Ben Nevarez, Florence Lydon, Debra Kilday
Class 1: Jill Dodson, Betsy Lopez, Patricia Thompson, Tommy Stephens, Cynthia Horton, Donald Olivares, Wanda Fennell, Amanda Scott, Keely Campbell, Teresa Jackson, Paul Finn, Joseph Salcido, Stacy Hawke, Arlene James, Annette Parker, Keith Fonte, Teresa Walbridge, John Hunter, Elizabeth Varnado, William Llewellyn, Traci Fulks, Rubye Hamlin, Twyla Hernandez, Nancy Perez, Penelope Mckeown
Class 2: Michael Earvin, Kandace Murphy, Jon Rager, Wayne Paredes, Jacqueline Quintana, Guy Hirko, John Matas, Gerald Mattox, Frank Hurtado, Sean Gravina, Brittany Rogers, Lillian Hollis, Luis Shutt, John Foster, Harold Burns, Mario Fletcher, Amy Davis, Delbert Paulin, David Golding, Mark Tate, Donald Benoit, Aaron Olivia
Class 3: Dorothy Lewis, Jo Baza, Katherine Monroe
Class 4: Sarah Rhim, Danny Perez
Class 5: Susan Garcia, Michelle Mushrush, Brett Oneil, Mary Mariani, Lee Bow, Ron Ewing, Peter Vincent, Ha Cook, Johnny Fettig, Johnny Covington
Accuracy: 0.609375
```


### Neural Network Note

Note: Since the neural network has a set input, we did not test it with the football dataset, but if we did, we are confident it will be able to classify the teams with a high accuracy due to the results on the other datasets.

### Neural Network - Dataset 4
<img src="https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/blob/main/README_data/Python/NN_dataset4.png"></br>

```
Class 0: Donte Bringle, Jamie Evans, Duane Edwards, Miguel Hibbs, David Shaw, Laura Escudero, Janet Savitts, John Wiederwax, Denise Moller, Amy Pratt, Gary Cox, Michelle Mushrush, Robert Meade, James Smith, Alexander Landis, Jennifer Hunter, Shawn Worrell, Rhonda Marshall, Roy Larmon, Ben Nevarez, Spencer Patrick, Mary Mariani, Alexander Lloyd, Ben Sullivan, Kenneth Gleaton, Fred Foster, George Nehring, Josefina Orear, Angelina Gordon, Ginger Dower, Theresa Taylor, Sussy Baka
Class 1: Kandace Murphy, Wayne Paredes, Luis Shutt, Jacqueline Quintana, Susan Garcia, Sean Gravina, Melissa Gibson, Sue Eby, John Foster, Brittany Rogers, Vada Isom, Michael Earvin, Lillian Hollis, Frank Hurtado, Donald Benoit, Delbert Paulin, Harold Burns, Guy Hirko, Jon Rager, Aaron Olivia, Brett Oneil, David Golding, Twyla Hernandez, Peter Vincent, Amy Davis, Mario Fletcher, Dorothy Lewis, John Matas, Gerald Mattox, Mark Tate, Penelope Mckeown
Class 2: Robert Roller, Betsy Lopez, Donald Olivares, Jo Baza, Tommy Stephens, Keely Campbell, Teresa Walbridge, Paul Finn, Joseph Salcido, Amanda Scott, Danny Perez, Arlene James, Wanda Fennell, Rubye Hamlin, Cynthia Horton, Teresa Jackson, Annette Parker, Elizabeth Varnado, William Llewellyn, Jill Dodson, Nancy Perez, Keith Fonte, Samantha Stone, Ron Ewing, Ha Cook, Patricia Thompson, Sarah Rhim, Katherine Monroe, Johnny Fettig, Traci Fulks, Johnny Covington, John Hunter
Class 3: Franklin Davis, Alfredo Petty, Sarah Ramirez, Alexandra Livingston, Bonnie Aman, Dianna Spencer, Teri Holstein, Thelma Wiggins, Ella Johnson, Edwin Morley, Stacy Hawke, Robert Coleman, Tommie Lutes, Michael Farr, Irene Robinson, Daniel Montoya, James Sindorf, Ralph Carradine, Victor Fry, Jennifer Morris, Susanne Rivas, Connie Funk, Curt Ritter, Allen Poole, Robert Castro, Thomas Franko, James Mauk, Lee Bow, Idell Nixon, Lillian Canales, Florence Lydon, Debra Kilday, Eric Dietz
Accuracy: 0.984375
```


## Final Results

The neural network algorithm tended to show more accuracte results and took significantly less time than the Girvan Newman algorithm after the network was trained. Note: The data for this section can be found in [this spreadsheet](https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/blob/main/README_data/Python/Time_Acc_Data.xlsx)

Second note: Neural networks in the data are represented by the number of nodes in each layer. So, the algorithm labelled as 256,128 is a neural network with 2 layers where the first layer has 256 nodes and the second has 128 nodes.

Third note: The 80% part on the Girvan Newman algorithm means we used an 80% sample when calculating the betweeness for the Girvan Newman algorithm which sped up the computation and gave us results in a quicker time with a very slight decrease in accuracy.

### Algorithm Time

First, let's take a look at how long it took each algorithm to make its final prediction:

<img src="https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/blob/main/README_data/Python/Algorithm%20Predicting%20Speeds%20on%20Datasets.png"></br>

Clearly the Girvan Newman algorithm took the longest to run on every dataset. This is the expected behavior since the Girvan Newman algorithm is an iterative method while the neural network is a function transformation. Let's see how the neural networks did against each other time-wise:

<img src="https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/blob/main/README_data/Python/Algorithm%20Predicting%20Speeds%20on%20Datasets%20(GN%20Removed).png"></br>

None of the neural networks seemed to show a signifiacant time change on any of the datasets (besides the one outlier which was a neural network with nodes 128,64,32). This is the expected behavior since all the neural networks have about the same number of layers and take about the same number of computations to compute the final result.

### Algorithm Accuracy Aginst Each Other

Now let's take a look at the accuracy between the neural network and the Girvan Newman algorithm:

<img src="https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/blob/main/README_data/Python/Algorithm%20Accuracy%20on%20Datasets.png"></br>

<img src="https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/blob/main/README_data/Python/Average%20Accuracy%20By%20Algorithm.png"></br>

Looking at the data, we can see that the Girvan Newman algorithm was usually the second worst algorithm. The Girvan Newman algorithm likely performed as almost the worst algorithm due to it being a very naive approach at the Community Detection problem.

Interestingly, the neural network with layers 64,32,16,8 had the worst accuracy which is likely because of how small the dimensions of the latent space are (the latent space is 8-dimensional).

The best algorithm was the neural network with layers 256,128 and this algorithm performed significantly better than the Girvan Newman. On average over all the datasets, this algorithm was over 20% more accurate than the Girvan Newman algorithm.

### Algorithm Accuracy Aginst The Graph Structure

Finally, we will examine the accuracy of the algorithms in relation to the structure of the graph.

The metric of the graph we will examine is the average out degree of each node. The out-degree of a node is the number of neighbors the node has that are outside it's community.

Below are the results for each algorithm:

<img src="https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/blob/main/README_data/Python/Average%20Out%20Degree%20Count%20Vs.%20Algorithm%20Accuracy.png"></br>

The data shows a very clear negative slope, meaning as the number of out-degrees in the graph increase so does the accuracy of the algorithm. Let's take a look at the average accuracy between all algorithms:

<img src="https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/blob/main/README_data/Python/Average%20Out%20Degree%20Count%20Vs.%20Average%20Accuracy%20Across%20Algorithms.png"></br>

The graph shows a negative quadtratic relationship between the average node out-degree and the average accuracy of all algorithms on that graph. So, communities with high out-degrees give both of these algorithms trobule.

# Installation, Configuration, Execution

## Project Installation

First, clone the project from GitHub onto your local machine by pressing the green "code" button on the repository page. There are multiple methods of cloning, but use whatever method you are most comfortable with: </br>

- [GitHub Desktop](https://desktop.github.com/)
- Git (Bash)
- Unzip File

Once you have the repository on your machine, make sure that you locate the folder and know the path.

## Cpp Project Configuration

In this section, we look at building, linking, and creating the executable for this project. Note that you must have cmake, a compiler, such as gcc, and an environment, such as wsl on your machine. Information about these necessary installations will be listed here:

- [CMAKE](https://cmake.org/)
- [GCC](https://gcc.gnu.org/)
- [WSL](https://docs.microsoft.com/en-us/windows/wsl/about)

If you have an IDE available, you may open the project folder in the IDE and build in the application. This will create the cmake-build-debug directory and add the necessary files for you. [Clion](https://www.jetbrains.com/clion/features/?source=google&medium=cpc&campaign=11960745263&gclid=Cj0KCQiA6NOPBhCPARIsAHAy2zBRVCJK1PdQabj8I-gOpo-iyXsYsDuNjyX9pUvGl5YcFkaTbC-0W9oaAs5BEALw_wcB) and [Eclipse](https://www.eclipse.org/downloads/) are both good choices.

Otherwise, a step-by-step procedure for doing so in the terminal can be found below:

1. Open terminal, type wsl, and navigate into the folder using the path specified by the cloning process.
2. Once you are in the folder, create a directory entitled "cmake-build-debug." 
3. Then, type:

```bash
cmake -S [Project Directory Path] -B [cmake-build-debug path]
```

If you are in the project directory, it will look something like this:

```bash
cmake -S ../22s-pa03-girvan-newman-uwunary-tree -B cmake-build-debug
```

4. You will see some messages about compiler information and configuration. You can check the cmake-build-debug folder to make sure it has been populated with the necessary files.
5. You can now build and link the project to create the executable. Type:

```bash
cmake --build [cmake-build-debug path]
```

If you are in the project directory, it will look something like this:

```bash
cmake --build cmake-build-debug
```

Once finished with this process, the cmake-build-debug folder should have the executable in it. Check to make sure the data folder and output folder have been pushed into the folder. If they haven't copy and paste them into the cmake-build-debug directory.

## Cpp Main Project Execution - <i>(main.cpp)</i>

The following command can be used to run the project: </br>

```bash
./22s-pa03-girvan-newman-uwunary-tree [graphml path] [value type]
```

To find the value type, search the specified grapml file for the "attr.name" node attribute and set it equal to that.

## Python Project Configuration

In this section, we look at downloading and using a python interpreter. This can be done in multiple ways, and it depends on your machine. For example, with homebrew or ubuntu, one may install by simply looking up the install command and running it. But for those who don't have either, [here](https://www.python.org/downloads/) is the official download from python's website.

After doing so, you may use terminal or an IDE to run the project scripts, similarly to how it worked previously. We used Visual Studio Code, but anything works.

## Python Main Project Execution - <i>(communityDetection.py)</i>

The following command can be used to run the project: </br>

```bash
python communityDetection.py
```

### All Script Parameters

These parameters can be changed and will effect both the Girvan Newman algorithm and the Neural Network algorithm

<b>mode</b> - Options: "NN" or "GN"
- Use "NN" to evaluate the graph using the Neural Network model.
- Use "GN" (or any other string) to evaluate the graph using the Girvan Newman algorithm.

<b>Note: </b>
- If "NN" is used, make sure to change the parameters in [Neural Network Parameters](https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/edit/main/README.md#neural-network-parameters)
- If "GN" is used, make sure to change the paramters in [Girvan Newman Parameters](https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/edit/main/README.md#girvan-newman-parameters)

<b>commName</b> - A string defining the name of the community in the graphML file.
- The commName can be found at the top of the .graphml file.
- Example:

  <img width="455" alt="commName example" src="https://user-images.githubusercontent.com/43501738/161797078-eda078fa-ea8f-428c-98a4-f79580ab0710.png">
  
  In this case the commName would be "community"
 
<b>inFile</b> - The graphml data file to load in to test the algorithm
- This file is a .graphml file and stores a graph we want the model to analyze

### Neural Network Parameters

<b>configFileName</b> - The yaml configuration file name used to configue the neural network
- Example: In this repo, the default file name is ```"./networkParams.yml"```
- For more information on the configuration file, go to [the following section](https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/edit/main/README.md#network-configuration)

<b>modelFileName</b> - The file name to the model to load in.
- In this repo, we have pretrained models which can be found in the ```models/``` directory. For example, to load in the ```64,32,16,8``` file, the modelFileName would be ```"64,32,16,8"```.

<b>NOTE:</b> The configuration file should have the same configuration as the model being loaded in.
- For example, if the `modelFileName` is ```"64,32,16,8"```, then the configuartion file would look like the following:
```
inDim: 128
Encoder:
    layerNodes: [64,32,16,8]
    activation: "ReLU"
Decoder:
    layerNodes: [8,16,32,64]
    activation: "ReLU"
```

<b>numClasses</b> - The number of classes for the model to classify nodes into.
- By default, this value is set to 4 since the test data found in `data/` has 4 classes.
- If numClasses is changed to a value that is not 4, new test data will have to be created using the [Data Generation Script](https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/edit/main/README.md#data-generation)


### Girvan Newman Parameters

<b>nodeSubsetPercent</b> - The percent of random nodes to pick in the betweeness algorithm
- Values can between (0, 1]
- When the GN algorithm runs, it calculates the betweeness for a set percentage of nodes as opposed to doing all the nodes
- A higher percetage makes the algorithm more accurate, but also makes the algorithm take longer


## Network Training (trainNetwork.py)

To make predictions on the classes in the graph, first the model has to be trained.

<b>Notes:</b>
- The neural network has a set input size which is the number of nodes in the graph. So, the data it is trained on must also have the same number of nodes.
- Our pretrained models were trained on 128 nodes, meaning the data also had 128 nodes. To use a graph with a different number of nodes, new data will have to be generated using that number of nodes. Instructions to generate new data can be found in the [Network Data Generation](https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/edit/main/README.md#network-data-generation) section.

<b>configFileName</b> - The yaml configuration file name used to configue the neural network
- Example: In this repo, the default file name is ```"./networkParams.yml"```
- For more information on the configuration file, go to [the following section](https://github.com/smu-cs-3353/22s-pa03-girvan-newman-uwunary-tree/edit/main/README.md#network-configuration)

<b>dataDir</b> - Directory in which the data to train the model can be found
- In this repo, the default directory is `networkTrainData/`

<b>numEpochs</b> - The number of epochs to train the model
- The higher this value, the longer the model will train for, but that does not necessarly mean it will be better.
  
<b>trainPercent</b> - The percent of data to train the model on.
- Values can between (0, 1]

<b>saveFileName</b> - The file to save the model to when the model is finished training


## Network Data Generation (networkDataGeneration.py)

The network needs a significant amount of data in order to learn useful representations of the data. The data we need is a matrix which has the following dimesnions:

  (NxN) where N is the number of nodes in the graph (numNodes)
  
The data is called a modularity matrix which is represented as B_ij and can be obtained from the following formula:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\color{white}\Large\B_{ij} = A_{ij} - \frac{k_i k_j}{2m}"></br>
</p>
- A_ij - Number of edges between node i and j (usually 0 or 1)</br>
- k_i - Degree of node i</br>
- k_j - Degree of node j</br>
- m - Number of edges in the old graph</br>
</br>
Fotunately, the input and output to the network is the same, so we only need to worry about generating these matricies for both the input and output to the network.


Parameters:
- <b>dirName</b> - The name of the directory to save the data arrays to
- <b>numNodes</b> - The number of nodes in the graph
- <b>percentFunc</b> - Function to get a random number between the two numbers in random.uniform. These values should be between 0 and 1
- <b>numGraphs</b> - Number of graphs to generate. This value is also the number of data arrays to generate.



### Model Configuration (networkParams.yml)

The network configuration can be found in the `networkParams.yml` file. This file is written using the yaml style with the following parts:
- inDim: The size of input into the neural network (this value is the same as the number of nodes in the graph)
- Encoder: Information on the encoder network
  - layerNodes: Array storing the size of each layer in the encoder network.
    - Example: [1024,512,128]</br>
      In this case, the encoder would have three layers with 1024 nodes in the first layer, 512 in the second, and 128 in the third.
  - activation: The activation function for the encoder network (Can be one of the following: "ReLU", "Sigmoid", "Tanh")
- Decoder: Information on the decoder network
  - layerNodes: Array storing the size of each layer in the decoder network.
    - Example: [128,512,1024]</br>
      In this case, the decoder would have three layers with 128 nodes in the first layer, 512 in the second, and 1024 in the third.
    - Note: This value should probably be the reverse of the encoder layerNodes value
  - activation: The activation function for the decoder network (Can be one of the following: "ReLU", "Sigmoid", "Tanh")


## Data Generation (dataGenerator.py)

To test the algorithms, this script can be used to generate datasets. This script will generate a GraphML file that stores a graph with a class for each node. The scipt has the following parameters:
- <b>outFile</b> - File name to save the generated graph to
- <b>vertices</b> - The number of vertices in the generated graph
- <b>communities</b> - Number of communities to classify nodes into
- <b>communitySize</b> - (Automatically calculated) The size of each community
- <b>rand</b> - If True, random numerical values will be used to name each node. If False, sequential values will be used to name each node.
- <b>names</b> - If True, <b>rand</b> is ignored and random names will be generated to name each node. If False, <b>rand</b> will be used and numbers will be used to name the nodes.
- <b>P_out</b> - Probability of an edge to be generated which connects nodes between communities
  - Note: This value should be between 0 and 0.06 due to the range of P_in forcing the average number of edges to be 16
- <b>P_in</b> - (Autmoatically calculated) Probability of an edge to be generated which connects nodes within communities
- <b>stats</b> - True to show stats on the graph after generation. False to not show stats on the graph after generation

Example of the output can be found in the `data/` directory.


## GML To GraphML Conversion (gml_to_graphml.py)

This script converts a GML graph file to a GraphML graph file. The input is a .gml file and the output is the corresponding .graphml file. The parameters are as follows:
- <b>inFile</b> - The .gml graph file to convert to a .graphml graph file
- <b>outFile</b> - The name of the .graphml output file to write to

# References

[1] M. Girvan and M. E. J. Newman, ???Community structure in social and biological networks,??? Proceedings of the National Academy of Sciences, vol. 99, no. 12, pp. 7821???7826, Jun. 2002, doi: 10.1073/pnas.122653799.

Girvan Newman Algorithm: https://www.pnas.org/doi/epdf/10.1073/pnas.122653799

Modulatiry function (Q Function): https://www.pnas.org/doi/full/10.1073/pnas.0601602103

Breadth First Search (BFS): http://infolab.stanford.edu/~ullman/mmds/book0n.pdf (10.2 - page 361 (page 381 in PDF))

Neural Network Algorithm: https://www.ijcai.org/Proceedings/16/Papers/321.pdf
