# Environments

[Spack] [environments] are used to group together a set of specs for building, re-building, and deploying in a coherent fashion.

## Usage

### Concretize

```bash
spack -e PATH/TO/my-spack/envs/ENVIRONMENT concretize -f
```

### Install Dependencies

```bash
spack -e PATH/TO/my-spack/envs/ENVIRONMENT install --only=Dependencies
```

### Interactive Shell

```bash
spack -e PATH/TO/my-spack/envs/ENVIRONMENT build-env SPEC -- bash
```

## ALPS User Environments

The local [Spack] instance can re-use packages from [Spack Stacks] built with [Stackinator]:

```bash
export SPACK_SYSTEM_CONFIG_PATH=/user-environment/config
```

[Spack]: https://spack.readthedocs.io/en/latest/index.html
[environments]: https://spack.readthedocs.io/en/latest/environments.html
[Spack Stacks]: https://github.com/eth-cscs/alps-spack-stacks
[Stackinator]: https://github.com/eth-cscs/stackinator
