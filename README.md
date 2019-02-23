# ODEParamEstim

**Parameter Estimation:** Using Genetic Algorithm to Fit ODE Models to Data
***
![cfos](https://user-images.githubusercontent.com/31299606/50464653-81b02700-09d5-11e9-910a-e3e2dcbd4fdd.png)

 Points (blue diamonds, EGF; red squares, HRG) denote experimental data, solid lines denote simulations.

## Algorithm
ga_v2 optimizes an objective function through the following procedure.

1. **Initialization**<br>
As an initial population, create *n*<sub>*p*</sub> individuals randomly. ga_v2 also represents individuals as n-dimensional real number vectors, where n is the dimension of the search space. To these individuals, ga_v2 tentatively assigns a single objective value which is worse than those of any of the possible candidate solutions. Set Generation to 0, and set the iteration number of converging operations *N<sub>iter</sub>* to 1.

1. **Selection for reproduction**<br>
As parents for the recombination operator, ENDX, select *m* individuals, **p**<sub>1</sub>, **p**<sub>2</sub>, · · · ,**p**<sub>*m*</sub>, without replacement from the population.

1. **Generation of offsprings**<br>
Generate *N<sub>*c*</sub>* children by applying ENDX to the selected parents. This algorithm assigns the worst objective value to the children.

1. **Local Search (NDM/MGG)**<br>
Apply the local search method to the best individual in a family consisting of the two parents, i.e., **p**<sub>1</sub> and **p**<sub>2</sub>, and their children. Note here that the children are assumed to have the worst objective value. Thus, whenever the objective values of the two parents have been actually computed in previous generations, the algorithm applies the local search to either of the parents. When all of the individuals in the family have the same objective value, on the other hand, the local search is applied to a randomly selected individual from the family.

1. **Selection for survival**<br>
Select two individuals from the family. The first selected individual should be the individual with the best objective value, and the second should be selected randomly. Then, replace the two parents (**p**<sub>1</sub> and **p**<sub>2</sub>) with the selected individuals. Note that the individual to which the local search has been applied in the previous step is always selected as the best.

1. **Application of ENDX/MGG**<br>
To achieve a good search performance, ga_v2 optimizes a function, gradually narrowing the search space. For this purpose, the converging phase slightly converges the population by repeating the following procedure *Niter* times.
    1. Select *m* individuals without replacement from the population. The selected individuals, expressed here as **p**<sub>1</sub>, **p**<sub>2</sub>, · · · , **p**<sub>*m*</sub>, are used as the parents for an extended unimodal normal distribution crossover (ENDX) applied in the next step.

    1. Generate *N<sub>*c*</sub>* children by applying ENDX to the parents selected in the previous step. To reduce the computational cost, ga_v2 forgoes any computation of the objective values of the *N<sub>*c*</sub>* individuals generated here. Instead, the algorithm assigns the newly generated children a single objective value, one which is inferior to the objective values of any of the possible candidate solutions.

    1. Select two individuals from a family containing the two parents, i.e., **p**<sub>1</sub> and **p**<sub>2</sub>, and their children. The first selected individual should be the one with the best objective value, and the second should be selected randomly. Then, replace the two parents with the selected individuals.

1. **Adaptation of *N<sub>iter</sub>***<br>
If the best individual has not improved during the last *n*<sub>*p*</sub> generations, *N<sub>iter</sub>* ← 2 × *N<sub>iter</sub>* . Otherwise, set *Niter* to 1.

1. **Termination**<br>
Stop if the halting criteria are satisfied. Otherwise, *Generation* ← *Generation* +1, and return to the step 2.

## Model

- [Nakakuki, T. et al. Ligand-specific c-Fos expression emerges from the spatiotemporal control of ErbB network dynamics. Cell 141, 884–896 (2010).](https://www.cell.com/cell/fulltext/S0092-8674(10)00373-9)

## Requirement

- [Anaconda3](https://www.anaconda.com/)

## Installation

    $ git clone https://github.com/u360665a/ODEParamEstim
