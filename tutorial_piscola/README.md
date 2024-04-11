# PISCOLA Tutorial
___

## Requirements

It is recommended to use an environment to install PISCOLA. All the requirements for this tutorial are in the `requirements.txt` file.

```python
conda create -n tutorial pip  # environment called 'tutorial'
conda activate tutorial
pip install -r requirements.txt
```
Note that the PISCOLA version used is `2.0.0rc2`, which is a release candidate and therefore not installed simply with `pip install piscola`.

In case there is a problem with jax (happened for a few Mscs) do:

```
pip uninstall jax jaxlib
conda install -c conda-forge jaxlib
conda install -c conda-forge jax
```
