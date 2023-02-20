setup Jupyter environment to run R Scripts

## environment
`conda create -n proc_env python=3.8`
## activation
`conda activate proc_env`
## kernel installation
`conda install -c r r-irkernel jupyterlab`
## R library installation
`python3 subsetup.py`
* This calls the `Rsetup.R` script
## launch jupyter lab
`jupyter lab`
