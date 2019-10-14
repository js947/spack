# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Phylipnew(AutotoolsPackage):
    """The PHYLIPNEW programs are EMBOSS conversions of the programs in Joe
    Felsenstein's PHYLIP package, version 3.61 (August 2004)."""

    homepage = "http://emboss.sourceforge.net/apps/cvs/embassy/phylipnew/"
    url      = "ftp://emboss.open-bio.org/pub/EMBOSS/PHYLIPNEW-3.69.660.tar.gz"

    version('3.69.660', sha256='af385d01826e67e05295955f05721728abbd4feb9e11a944189414da6590bfeb')

    depends_on('emboss')
    depends_on('pcre')
