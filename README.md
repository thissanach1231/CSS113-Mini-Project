1. Introduction

1.1 Project Overview
	Process graph data from the user to determine the result.
1.2 Problem Statement
	Develop the following algorithm
	- Depth First Search (DFS) & Breadth First Search (BFS)
	- Dijkstra
	- Prim
	- Kruskal
1.3 Objective
	Process data from the user and produce the following expected result.
	- DFS & BFS = Visited order and path.
	- Dijkstra = Path from start to end with least total weight.
	- Prim = MST connection and total weight
	- Kruskal = MST connection and total weight
1.4 Scope
	Input data will be required to follow the following regulation.
	- Must be undirected graph
	- Each edge must have its own weight
	- No such connection that would be sharing the same set of vertex


2. Developing Environment, Library & Version Controls

2.1 Software
	Our team includes 3 developers who develop and test the project. Each developer developing environment software will be specified below.
Developer 1
		OS = Windows 11
		IDE = Visual Studio Code 1.146.0
		VCS = Git 2.52.0
	Developer 2
		OS = Windows 11
		IDE = Visual Studio Code 1.146.0
		VCS = Git 2.56.1
Developer 3
OS = Windows 11
IDE = Visual Studio Code 
VCS = Git 

2.2 Programming Languages
	Python 3.14.0

2.3 Libraries
collections	for queue
re		for match
heapq	for priority queue


3. Installation and Environment Setup

3.1 Prerequisites
	Follow the following steps to ensure that the program will work properly. (Microsoft Windows 11)
	3.1.1 Install Python version 3.14.0
	3.1.2 Install Visual Studio Code version 1.146.0
3.1.3 Install Git for Windows version 2.52.0 or above
3.1.4 Ensure the Python installation works properly by opening the terminal and type the following command “ python --version ”. The expected output will be “ Python 3.14.0 ”.
If errors appear, please restart your device and try to enter the command once your device finishes restarting.
3.1.5 Ensure Visual Studio Code version is correct by opening Visual Studio Code -> click “ Help ” -> click “ About ”. There should be pop up that has current version of the Visual Studio Code which should be 1.146.0

3.2 Source Code
	Source code will be provided at 
https://github.com/thissanach1231/CSS113-Mini-Project
The following steps are source code set up and will be essential to receive the correct set of source code
3.2.1 Goes to endpoint provided above
3.2.2 Click “ fork ”
3.2.3 Click “ Create fork ”
3.2.4 Open Visual Studio Code
3.2.5 Click “ File ”
3.2.6 Click “ Open folder ” and select your preferred folder
3.2.7 Click “ Terminal ”
3.2.7 Click “ New Terminal ”
3.2.8 Type “ git clone https://github.com/YourGitHubUsername/CSS113-Mini-Project ” .
 *Replace YourGitHubUsername with your Github username.

	
3.3 Environment Configuration
	The application will only have a capability to read .txt format and content contained inside must follow standard regulation in the regulation section.
	
3.4 Initialize Application
Input data set following terminal command recommendation. The output will be shown in the terminal.


Limitations & Regulation
	
Nodes can only be numbers which are required to start from 0 and continue by 1. For example, 0 => 1 => 2 => 3 => … . 
Therefore, if the data contains the alphabet, then the alphabet must be changed to numbers following the regulation.
