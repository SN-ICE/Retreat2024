```
git clone https://github.com/cconroy20/fsps
export SPS_HOME="$PWD/fsps"
git clone https://github.com/bd-j/prospector.git
cd prospector
conda env create -f environment.yml -n prospector
conda activate prospector
python -m pip install .
```

Beware of NOT mixing PROSPECTOR and Hostphot instalation since they have incompatible numpy and astropy versio
