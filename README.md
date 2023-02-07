# Simulated-Annealing

Simulated-Annealing algorithm is one of the most preferred heuristic methods for solving the optimization problems.

### Basic idea:

- Allow bad moves occasionally, depending on the “temperature” and how bad the move is.
- High temperature => more bad moves allowed, shake the system out of its local optimum.
- Gradually reduce temperature according to some schedule.

### Guaranteed to find optimal?

- If scheduler decreases T to 0 slowly enough, then will find optimum with probability 1

## ⚙️ Technologies

<img src="https://img.icons8.com/color/256/python.png" width=70px/>

<br>

## <img src="https://cdn-icons-png.flaticon.com/512/2103/2103633.png" width=35xp /> Algorithms and examples

<b>Simulated annealing</b> is an algorithim which uses randomness to garuntee optimality. It starts at a random point then decreases the temperature which in return decreases the margin of error. At the end it check whether the new or the old point is better and repeat.
<br>

<img src="extra-doc/SA-Example.png" alt="example.png"/>
<br>

As you can see in the gif below Simulated annealing is great for even non linear problems

<img src="https://upload.wikimedia.org/wikipedia/commons/1/10/Travelling_salesman_problem_solved_with_simulated_annealing.gif" alt="example gif"/>

<br>

## <img src="https://cdn-icons-png.flaticon.com/512/707/707163.png" width=20px/> N-Queens

N-queen problem is placing N queens on an NxN grid such that no two queens attack each other.

We will use the concise
formulation of forcing the N-queens on the N columns of the grid. Thus, a state can be represented by a tuple. For example for 4-
queens, s = (0,3,2,0) represents the state (note the usage of 0-indexing) of positioning the first queen in the first column at row 0,
the second queen in the second column at row 3, the third queen in the third column at row 2, and the fourth queen in the fourth
column at row 0

<img src="extra-doc/N-Queens.png"/>

## <img src="https://cdn-icons-png.flaticon.com/128/9184/9184187.png" width=17px /> Installation

1- install the newest version of <a href="https://www.python.org/">Python</a>

2- install numpy

```
pip install numpy
```

3-install seaborn

```
pip install seaborn
```

4- install metplotlib.pyplot

```
pip install matplotlib.pyplot
```

5- Run test_local_search.py

## <img src="https://cdn-icons-png.flaticon.com/128/2570/2570287.png" width=20px/> Author

[@AhmadBaaqeel](https://github.com/Ahmedbaaqeel)
