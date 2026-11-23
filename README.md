# CSS113 Mini Project — Graph Algorithms

**A Python-based graph processing application implementing fundamental graph traversal and minimum spanning tree algorithms.**

![Python](https://img.shields.io/badge/Python-3.14.0-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%2011-blue?logo=windows)
![Status](https://img.shields.io/badge/Status-Development-orange)
![Algorithms](https://img.shields.io/badge/Algorithms-5-green)

---

# Table of Contents

1. [Introduction](#1-introduction)
   - [1.1 Project Overview](#11-project-overview)
   - [1.2 Problem Statement](#12-problem-statement)
   - [1.3 Objectives](#13-objectives)
   - [1.4 Project Scope](#14-project-scope)
2. [Development Environment, Libraries & Version Control](#2-development-environment-libraries--version-control)
   - [2.1 Software](#21-software)
   - [2.2 Programming Language](#22-programming-language)
   - [2.3 Libraries](#23-libraries)
3. [Installation and Environment Setup](#3-installation-and-environment-setup)
   - [3.1 Prerequisites](#31-prerequisites)
   - [3.2 Source Code Setup](#32-source-code-setup)
   - [3.3 Environment Configuration](#33-environment-configuration)
   - [3.4 Running the Application](#34-running-the-application)
4. [Limitations and Regulations](#4-limitations-and-regulations)

---

# 1. Introduction

## 1.1 Project Overview

This project is designed to process graph data provided by users and execute various graph algorithms to produce the expected results.

## 1.2 Problem Statement

The project aims to develop and implement the following graph algorithms:

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Dijkstra's Algorithm
- Prim's Algorithm
- Kruskal's Algorithm

## 1.3 Objectives

The application processes user-provided graph data and produces the following results:

| Algorithm | Expected Output |
|:---|:---|
| DFS | Visited order and traversal path |
| BFS | Visited order and traversal path |
| Dijkstra | Shortest path between the specified start and destination nodes, including total weight |
| Prim | Minimum Spanning Tree (MST) connections and total weight |
| Kruskal | Minimum Spanning Tree (MST) connections and total weight |

## 1.4 Project Scope

The application is designed to process undirected, weighted graphs.

Input data must comply with the following regulations:

- The graph must be undirected.
- Every edge must have an associated weight.
- Duplicate edges between the same pair of vertices are not permitted.

---

# 2. Development Environment, Libraries & Version Control

## 2.1 Software

The project is developed and tested by a team of three developers. Their respective development environments are listed below.

| Software | Developer 1 | Developer 2 | Developer 3 |
|:---|:---|:---|:---|
| Operating System | Windows 11 | Windows 11 | Windows 11 |
| IDE | VS Code 1.146.0 | VS Code 1.146.0 | VS Code |
| Version Control | Git 2.52.0 | Git 2.56.1 | Git |

## 2.2 Programming Language

| Language | Version |
|:---|:---|
| Python | 3.14.0 |

## 2.3 Libraries

The project utilizes the following Python standard libraries:

| Library | Purpose |
|:---|:---|
| `collections` | Provides queue-related data structures for graph traversal |
| `heapq` | Provides priority queue functionality for efficient node selection |
| `re` | Provides regular expression functionality for matching and processing input data |

**Note:** All libraries listed above are included in Python's standard library. No additional `pip install` commands are required.

---

# 3. Installation and Environment Setup

## 3.1 Prerequisites

To ensure the application works properly, install the following software on Microsoft Windows 11:

1. **Python 3.14.0**
2. **Visual Studio Code 1.146.0**
3. **Git for Windows 2.52.0 or above**

### 3.1.1 Verify Python Installation

Open a terminal and execute the following command:

```bash
python --version
```

Expected output:

```text
Python 3.14.0
```

If the command does not work, check that Python is installed correctly and added to the system PATH. Restart the terminal after making changes.

### 3.1.2 Verify Visual Studio Code Version

1. Open Visual Studio Code.
2. Navigate to **Help**.
3. Select **About**.
4. Verify that the installed version is `1.146.0`.

### 3.1.3 Verify Git Installation

Open a terminal and execute:

```bash
git --version
```

Ensure that the installed version is Git 2.52.0 or above.

## 3.2 Source Code Setup

The project source code is hosted on GitHub:

**[CSS113 Mini Project Repository](https://github.com/thissanach1231/CSS113-Mini-Project)**

Follow these steps to obtain the source code:

1. Navigate to the GitHub repository provided above.
2. Click **Fork**.
3. Select **Create fork**.
4. Open Visual Studio Code.
5. Navigate to **File → Open Folder**.
6. Select your preferred directory for storing the project.
7. Open the terminal using **Terminal → New Terminal**.
8. Execute the following command:

```bash
git clone https://github.com/YourGitHubUsername/CSS113-Mini-Project.git
```

> **Important:** Replace `YourGitHubUsername` with your actual GitHub username.

9. Navigate into the cloned project directory:

```bash
cd CSS113-Mini-Project
```

## 3.3 Environment Configuration

The application supports input files in `.txt` format only.

All input data must comply with the graph regulations described in [Section 4](#4-limitations-and-regulations).

Ensure that the input file follows the required format before executing the application.

## 3.4 Running the Application

After completing the installation and environment configuration:

1. Open the project directory in Visual Studio Code.
2. Open the integrated terminal.
3. Navigate to the project directory.
4. Execute the application's main Python file.

For example, if the entry point is `main.py`:

```bash
python main.py
```

5. Provide the required input data according to the application's instructions.
6. The program will process the graph and display the corresponding algorithm results in the terminal.

---

# 4. Limitations and Regulations

The application enforces the following input restrictions:

### 4.1 Node Naming Convention

Nodes must be represented using non-negative integers, starting from `0` and increasing sequentially by `1`.

For example:

```text
0, 1, 2, 3, 4, ...
```

Alphabetical node identifiers are not supported.

If the original graph uses alphabetical identifiers, they must be converted into numerical identifiers before being processed.

### 4.2 Graph Restrictions

- Only undirected graphs are supported.
- Every edge must have an associated weight.
- Multiple edges connecting the same pair of vertices are not allowed.
- Input files must use the `.txt` extension.

### 4.3 Algorithm Considerations

- Dijkstra's Algorithm requires non-negative edge weights.
- Prim's and Kruskal's algorithms are intended to calculate a Minimum Spanning Tree for a connected graph.
- For disconnected graphs, a complete Minimum Spanning Tree does not exist.

---

<div align="center">

**CSS113 Mini Project**

Developed by Team 3

*Graph Algorithms Implementation using Python*

</div>
