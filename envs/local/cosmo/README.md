# LAMMPS with `metatomic`

## Generating Model

```
pip install --extra-index-url=https://download.pytorch.org/whl/cpu git+https://github.com/metatensor/lj-test
python PATH_TO_METATENSOR_LAMMPS/examples/PACKAGES/metatomic/create-lj-nickel.py
```

## Running LAMMPS on GPU

```
OMP_NUM_THREADS=8 spack-view/bin/lmp -k on g 1 -sf kk -in lammps.inp
```

