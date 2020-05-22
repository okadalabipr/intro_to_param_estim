# An introduction to parameter estimation

Using Genetic Algorithm to Fit ODE Models to Data
***
![simulation_average](images/simulation_average.png)

 Points (blue diamonds, EGF; red squares, HRG) denote experimental data, solid lines denote simulations.

 ## Dependencies
> - numpy
> - scipy
> - matplotlib
> - seaborn
> - jupyter

## Description
A brief description of each file you will need to use is below:

|Name|Description|
|---|---|
|[`model/name2idx/`](model/name2idx/)|This is where you define the parameter/variable names of your model.|
|[`model/set_model.py`](model/set_model.py)|This file contains the differential equations, parameters and initial concentrations.|
|[`param_estim/observalbe.py`](param_estim/observable.py)|This is the file to define the simulations you want to run and input the experimental data that you are going to use to try and fit the parameters to.|
|[`param_estim/search_parameter.py`](param_estim/search_parameter.py)|This is where you specify the model parameters to estimate.|
|[`param_estim/fitness.py`](param_estim/fitness.py)|This is where you define an objective function to minimize, e.g. the distance between model simulation and experimental data.|

- [**runGA_*n*.ipynb (*n* ≧ 1)**](runGA_1.ipynb)<br>
    Run both input boxes and leave it. When you run the *i*<sup>th</sup> file, runGA_(*i+1*).ipynb will be generated. You can run these different parameter fittings simultaneously.

- [**runSim.ipynb**](runSim.ipynb)<br>
    This is the file that is used to actually run the simulations for your model and plot the results.

- [**figure/**](figure/)<br>
    Within this folder there are several figures that will be saved. One is the ‘param_range.pdf’ which shows the range of values for your parameters based on all the fittings. The others are results of your simulations.

## Usage
### Parameter Estimation (runGA_*n*.ipynb, *n*=1, 2, 3, · · ·)
```javascript
%%javascript
IPython.notebook.kernel.execute(
    'current_ipynb = "' + IPython.notebook.notebook_name + '"'
)
```
```python
%run -i optimize.py
""" If you want to continue from where you stopped in the last parameter search,

%run -i optimize_continue.py

"""
```
or
```bash 
$ nohup python optimize.py n &
```
- If you want to search multiple parameter sets (from *n1* to *n2*) simultaneously,
```bash
$ nohup python optimize.py n1 n2 &
```

### Visualization of Simulation Results (runSim.ipynb)
**viz_type** : str

- ```'average'```
    : The average of simulation results with parameter sets in ```fitparam/```

- ```'best'```
    : The best simulation result in ```fitparam/```, simulation with ```best_fit_param```

- ```'original'```
    : Simulation with the default parameters and initial values defined in ```model/```

- ```'n(=1,2,...)'```
    : Use the parameter set in ```fitparam/n/```

**show_all** : bool
- Whether to show all simulation results.

**stdev** : bool
- If True, the standard deviation of simulated values will be shown (only when ```viz_type == 'average'```).

```python
from param_estim import simulate_all

simulate_all(viz_type='average',show_all=False,stdev=True)
```

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
