# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libmetatomic(CMakePackage):
    """C++ bindings to metatomic"""

    homepage = "https://docs.metatensor.org/metatomic"
    git = "https://github.com/metatensor/metatomic.git"

    maintainers("Luthaf", "RMeli")
    license("BSD-3-Clause", checked_by="RMeli")

    root_cmakelists_dir = "metatomic-core"

    version("metatomic-core", branch="metatomic-core")

    # metatomic-torch/CMakeLists.txt
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.22:", type="build")
    depends_on("libmetatensor@0.2.4:")
