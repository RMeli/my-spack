# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.plumed.package import Plumed as BuiltinPlumed

from spack.package import *


class Plumed(BuiltinPlumed):
    """Plumed with compiler wrapper filtering for mklib support."""

    filter_compiler_wrappers(
        "config.txt",
        "compile_options.sh",
        relative_root=join_path("lib", "plumed", "src", "config"),
    )
