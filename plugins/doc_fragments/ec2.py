# -*- coding: utf-8 -*-
# (c) 2022 Red Hat Inc.
#
# This file is part of Ansible
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from .region import ModuleDocFragment as RegionFragment

#
# The amazon.aws.ec2 docs fragment has been deprecated,
# please migrate to amazon.aws.region.modules.
#


class ModuleDocFragment:
    def __init__(self):
        self.DOCUMENTATION = RegionFragment.MODULES
