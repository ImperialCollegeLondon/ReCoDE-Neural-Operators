# Neural Operators Learning

## Description

[Neural operators (NOs)](https://arxiv.org/pdf/2108.08481) are neural networks (NNs) designed to learn mappings between infinite-dimensional function spaces. In this project, we will use a popular NO architecture, the Deep Operator Network (DeepONet) to solve Partial Differential Equations (PDEs) with the JAX library. In particular, we will solve the heat equation for different initial conditions to demonstrate the effectiveness of using NO networks for learning the dynamics of PDEs from data.

## Learning Outcomes

- What are PDEs and their relationship to science and engineering
- What are different numerical integration methods
- How to solve PDEs using numerical integration, particular finite differences
- How neural networks and neural operators work
- Key differences between traditional NNs and NOs
- How to solve PDEs using NOs

| Task              | Time       |
| ----------------- | ---------- |
| Reading           | 8 hours    |
| Running Notebooks | 6-12 hours |
| Practising        | 5+ hours   |

## Requirements

### Academic

- Knowledge of calculus, specifically differentiation
- Basic Python programming, including NumPy
- Basic knowledge in Deep Learning

### System

- Python 3.10 or newer
- A laptop with a CUDA-capable GPU (for training networks)

## Getting Started

### Python Installation and Environments

1. Install [Python 3.10 or newer](https://www.python.org/downloads/)
2. Create a [Python virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments) for installing the repo's modules and library dependencies
3. Install the repo dependencies using the command `pip install -r requirements.txt`
4. The Movie Writer, [ffmpeg](https://ffmpeg.org/download.html), is required for visualizing the solution of our PDE and must be installed

### How to Use the Repo

1. Start by reading `00-Intro-to-PDEs.ipynb` and running the code blocks for the concepts behind PDEs
2. Study `01-Solving-a-PDE.ipynb` for solving PDEs using numerical methods
3. Attempt `Example 1` and `Example 2` by filling in the blanks marked by empty strings, `""`
4. Solutions to the above can be found in the director `solutions`
5. Read `02-Intro-to-Neural-Operators.ipynb` for key concepts on neural operators and operator learning
6. Walkthrough `03-Dataset-Generation.ipynb` to generate the dataset for training our DeepONet
7. Walkthrough `04-Tutorial-00.ipynb` for training our DeepONet and visualising our results

## Project Structure

```log
.
├── notebooks
|   ├── 00-Intro-to-PDEs.ipynb
|   ├── 01-Solving-a-PDE.ipynb
|   ├── 02-Intro-to-Neural-Operators.ipynb
|   ├── 03-Dataset-Generation.ipynb
|   ├── 04-Tutorial-00.ipynb
|   ├── ...
│   └── data
├── docs
├── ...
└── requirements.txt
```

## License

This project is licensed under the [BSD-3-Clause license](LICENSE.md)
