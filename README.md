# An introduction to parameter estimation

Using Genetic Algorithm to Fit ODE Models to Data
***
![simulation_average](work/Fig/simulation_average.png)

 Points (blue diamonds, EGF; red squares, HRG) denote experimental data, solid lines denote simulations.

## Description
A brief description of each file you will need to use is below:
- [**param_estim/**](/param_estim/)<br>

    - [**model/**](/param_estim/model/)<br>

        - [**name2idx/**](/param_estim/model/name2idx/)<br>
            This is where you define the parameter/variable names of your model.

        - [**param_const.py**](/param_estim/model/param_const.py)<br>
            This file contains the parameters used in the differential equations.

        - [**differential_equation.py**](/param_estim/model/differential_equation.py)<br>
            This file contains the differential equations that instruct the model how to change concentrations of reactants over the time course of the simulation.

        - [**initial_condition.py**](/param_estim/model/initial_condition.py)<br>
            This is where you define initial concentrations.

    - [**simulation.py**](/param_estim/simulation.py)<br>
        This is where you define the simulations you want to run. In this file you can define different conditions for each simulation (for example, ligand concentration) and how you would like each variable to be simulated (i.e. do you want absolute concentration to be simulated? or percentage change over time? Etc).

    - [**experimental_data.py**](/param_estim/experimental_data.py)<br>
        This is where you input the experimental data that you are going to use to try and fit the parameters to.

    - [**search_parameter.py**](/param_estim/search_parameter.py)<br>
        This is where you specify the model parameters to estimate.

    - [**fitness.py**](/param_estim/fitness.py)<br>
        This file calculates the difference between the simulated values and the experimental values.

    - [**plot_func.py**](/param_estim/plot_func.py) & [**viz.py**](/param_estim/viz.py)<br>
        This is where you define how you would like each variable to be plotted.

- [**work/**](/work/)<br>
    - [**runGA/runGA_*n*.ipynb (*n* ≧ 1)**](/work/runGA/runGA_1.ipynb)<br>
        Run both input boxes and leave it. When you run the *i*<sup>th</sup> file, runGA_(*i+1*).ipynb will be generated in the runGA folder. You can run these different parameter fittings simultaneously.

    - [**runSim.ipynb**](/work/runSim.ipynb)<br>
        This is the file that is used to actually run the simulations for your model and plot the results.

    - [**Fig/**](/work/Fig/)<br>
        Within this folder there are several figures that will be saved. One is the ‘param_range.pdf’ which shows the range of values for your parameters based on all the fittings. The others are results of your simulations.

## Requirements
- Python3+
    - numpy
    - scipy
    - matplotlib
    - seaborn
    - jupyter

## Usage
- Parameter Estimation (work/runGA/runGA_*n*.ipynb, *n*=1, 2, 3, · · ·)
```javascript
%%javascript
IPython.notebook.kernel.execute(
    'current_ipynb = "' + IPython.notebook.notebook_name + '"'
)
```
```python
%run -i ../../run_ga.py
""" If you want to continue from where you stopeed in the last parameter search,

%run -i ../../run_ga_continue.py

"""
```
or
```bash 
$ nohup python parest.py n >> work/DVODE.log 2>&1 &
```

- Visualization of Simulation Results (work/runSim.ipynb)
```python
%run -i ../run_sim.py
%matplotlib inline
%config InlineBackend.figure_formats = {'png','retina'}

"""=============================================================
    viz_type: 'best', 'average', 'original' or int(1~n_fitparam)
    show_all: bool
    stdev: bool (Only when viz_type == 'average')
================================================================"""

viualize_result(viz_type='average',show_all=False,stdev=True)
```

## Algorithm
#### ga_v1:
Parameter values are searched by genetic algorithm with Unimodal Normal Distribution Crossover (UNDX) and Minimal Generation Gap (MGG).

#### ga_v2:
ga_v2 optimizes an objective function through the following procedure.

1. **Initialization**<br>
As an initial population, create *n*<sub>*p*</sub> individuals randomly. ga_v2 also represents individuals as *n*-dimensional real number vectors, where *n* is the dimension of the search space. To these individuals, ga_v2 tentatively assigns a single objective value which is worse than those of any of the possible candidate solutions. Set Generation to 0, and set the iteration number of converging operations *N<sub>iter</sub>* to 1.

1. **Selection for reproduction**<br>
As parents for the recombination operator, ENDX, select *m* individuals, **p**<sub>1</sub>, **p**<sub>2</sub>, · · · ,**p**<sub>*m*</sub>, without replacement from the population.

1. **Generation of offsprings**<br>
Generate *N<sub>*c*</sub>* children by applying ENDX to the selected parents. This algorithm assigns the worst objective value to the children.

1. **Local Search (NDM/MGG)**<br>
Apply the local search method to the best individual in a family consisting of the two parents, i.e., **p**<sub>1</sub> and **p**<sub>2</sub>, and their children. Note here that the children are assumed to have the worst objective value. Thus, whenever the objective values of the two parents have been actually computed in previous generations, the algorithm applies the local search to either of the parents. When all of the individuals in the family have the same objective value, on the other hand, the local search is applied to a randomly selected individual from the family.

1. **Selection for survival**<br>
Select two individuals from the family. The first selected individual should be the individual with the best objective value, and the second should be selected randomly. Then, replace the two parents (**p**<sub>1</sub> and **p**<sub>2</sub>) with the selected individuals. Note that the individual to which the local search has been applied in the previous step is always selected as the best.

1. **Application of ENDX/MGG**<br>
To achieve a good search performance, ga_v2 optimizes a function, gradually narrowing the search space. For this purpose, the converging phase slightly converges the population by repeating the following procedure *N<sub>iter</sub>* times.
    1. Select *m* individuals without replacement from the population. The selected individuals, expressed here as **p**<sub>1</sub>, **p**<sub>2</sub>, · · · , **p**<sub>*m*</sub>, are used as the parents for an extended unimodal normal distribution crossover (ENDX) applied in the next step.

    1. Generate *N<sub>*c*</sub>* children by applying ENDX to the parents selected in the previous step. To reduce the computational cost, ga_v2 forgoes any computation of the objective values of the *N<sub>*c*</sub>* individuals generated here. Instead, the algorithm assigns the newly generated children a single objective value, one which is inferior to the objective values of any of the possible candidate solutions.

    1. Select two individuals from a family containing the two parents, i.e., **p**<sub>1</sub> and **p**<sub>2</sub>, and their children. The first selected individual should be the one with the best objective value, and the second should be selected randomly. Then, replace the two parents with the selected individuals.

1. **Adaptation of *N<sub>iter</sub>***<br>
If the best individual has not improved during the last *n*<sub>*p*</sub> generations, *N<sub>iter</sub>* ← 2 × *N<sub>iter</sub>*. Otherwise, set *N<sub>iter</sub>* to 1.

1. **Termination**<br>
Stop if the halting criteria are satisfied. Otherwise, *Generation* ← *Generation* +1, and return to the step 2.

## Installation

    $ git clone https://github.com/okadalabipr/intro_to_param_estim.git

## Acknowledgements
We thank Benjamin Roberts and Iosifina Sampson (University of Leeds) for helpful comments and discussions.

## References
- Nakakuki, T. *et al.* Ligand-specific c-Fos expression emerges from the spatiotemporal control of ErbB network dynamics. *Cell* **141**, 884–896 (2010). https://doi.org/10.1016/j.cell.2010.03.054

- Kimura, S., Ono, I., Kita, H. & Kobayashi, S. An extension of UNDX based on guidelines for designing crossover operators: proposition and evaluation of ENDX. *Trans. Soc. Instrum. Control Eng.* **36**, 1162–1171 (2000). https://doi.org/10.9746/sicetr1965.36.1162

- Kimura, S. & Konagaya, A. A Genetic Algorithm with Distance Independent Diversity Control for High Dimensional Function Optimization. *J. Japanese Soc. Artif. Intell.* **18**, 193–202 (2003). https://doi.org/10.1527/tjsai.18.193

- Kimura, S., Nakakuki, T., Kirita, S. & Okada, M. AGLSDC: A Genetic Local Search Suitable for Parallel Computation. *SICE J. Control. Meas. Syst. Integr.* **4**, 105–113 (2012). https://doi.org/10.9746/jcmsi.4.105

## License
[MIT](/LICENSE)
