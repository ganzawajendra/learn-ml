# Machine Learning Foundation with Python

Welcome to the **Machine Learning Foundation** repository! 

> **Note:** This repository serves as my personal learning log and workspace as I dive into Machine Learning with Python. It is **not** intended to be a polished, comprehensive tutorial for others to learn from, but rather a living reflection of my own ongoing learning journey. The contents here will be continually updated and evolve alongside my progress.

While it is primarily for my personal tracking, it documents my exploration of the fundamental concepts required for Machine Learning. It covers everything from basic Python data structures and Object-Oriented Programming (OOP) to essential data science libraries like NumPy and Pandas.

## 📖 Table of Contents
- [Overview](#overview)
- [Folder Structure](#folder-structure)
  - [1. Data Structured (`/data-structured`)](#1-data-structured-data-structured)
  - [2. Object-Oriented Programming (`/object-oriented-programming`)](#2-object-oriented-programming-object-oriented-programming)
  - [3. NumPy (`/numpy`)](#3-numpy-numpy)
  - [4. Pandas (`/pandas`)](#4-pandas-pandas)
- [Prerequisites & Setup](#prerequisites--setup)
- [How to Use This Repository](#how-to-use-this-repository)
- [Contributing](#contributing)

---

## 📂 Folder Structure

The repository is organized logically into fundamental concepts, building up to data science libraries.

### 1. Data Structured (`/data-structured`)
This directory contains scripts that demonstrate how to use built-in Python data structures effectively.
- `list.py`: Working with Python Lists (creation, appending, slicing, list comprehensions).
- `dictionary.py`: Managing key-value pairs, iterating through dictionaries, and dictionary comprehensions.
- `tuple.py`: Understanding immutable sequences and unpacking.
- `set.py`: Handling unique elements, set operations (union, intersection, difference).

### 2. Object-Oriented Programming (`/object-oriented-programming`)
Understanding OOP is crucial for writing modular and reusable code in Machine Learning.
- `class_object.py`: Basics of defining classes and creating objects.
- `constructors.py`: Using `__init__` methods to initialize object state.
- `encapsulation.py`: Hiding internal state and requiring all interaction to be performed through an object's methods.
- `inheritance.py`: Creating new classes from existing ones to promote code reuse.
- `polymorphism.py`: Using a single interface with different underlying forms (data types).
- `decorator.py`: Modifying the behavior of a function or class using Python decorators.

### 3. NumPy (`/numpy`)
NumPy is the foundational package for scientific computing in Python. This folder covers:
- `array_creation.py`: Creating n-dimensional arrays from scratch or existing data.
- `array_attribute.py`: Understanding shape, size, and data types of arrays.
- `array_reshaping.py`: Changing the dimensions of arrays without changing their data.
- `index_slicing.py`: Accessing and modifying specific elements or sub-arrays.
- `math_statistics.py`: Applying mathematical functions and statistical operations on arrays.
- `linear_algebra.py`: Matrix multiplication, dot products, and other linear algebra operations.
- `random_module.py`: Generating random numbers, simulating distributions, and shuffling data.

### 4. Pandas (`/pandas`)
Pandas provides high-performance, easy-to-use data structures and data analysis tools. This folder utilizes Jupyter Notebooks for interactive learning:
- `01_pandas_data_structured.ipynb`: Introduction to Pandas Series and DataFrames.
- `02_data_inspection.ipynb`: Viewing and summarizing data (head, tail, info, describe).
- `03_indexing_selection.ipynb`: Selecting data using `.loc`, `.iloc`, and boolean indexing.
- `04_data_cleaning.ipynb`: Handling missing values, duplicates, and data type conversions.
- `05_data_transformation.ipynb`: Applying functions, mapping, and replacing values.
- `06_grouping_aggregation.ipynb`: Using `groupby` to aggregate and summarize data subsets.

---

## 🛠 Prerequisites & Setup

To run the code and notebooks in this repository, you need to have Python installed on your system. It is highly recommended to use a virtual environment.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ganzawajendra/learn-ml.git
   cd machine-learning
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - On **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the required dependencies:**
   This project includes a `requirements.txt` file that lists all the necessary packages (like `numpy`, `pandas`, `jupyter`, etc.).
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Use This Repository

- **For Python Scripts (`.py` files)**: Navigate to the respective directory and run the scripts directly from your terminal to see the output.
  ```bash
  python numpy/array_creation.py
  ```
- **For Jupyter Notebooks (`.ipynb` files)**: Navigate to the `pandas` folder (or the root directory) and start the Jupyter environment.
  ```bash
  jupyter notebook
  # OR
  jupyter lab
  ```
  This will open a browser window where you can open and execute the notebooks cell by cell.

---

## 🤝 Contributing
If you find any issues, typos, or have suggestions for new topics, feel free to open an issue or submit a pull request! Happy Learning! 🚀
