# Spack Configuration Files

Spack has many [configuration files](https://spack.readthedocs.io/en/latest/configuration.html#).

## Shared `$HOME`

In systems with a shared `$HOME` folder it is not possible to use a single user [configuration scope](https://spack.readthedocs.io/en/latest/configuration.html#configuration-scopes). `SPACK_USER_CONFIG_PATH` allows to set a different configuration path for different systems.
