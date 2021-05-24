#!/bin/python3

# CORTX Python common library.
# Copyright (c) 2020 Seagate Technology LLC and/or its Affiliates
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# For any questions about this software or licensing,
# please email opensource@seagate.com or cortx-questions@seagate.com.

import errno

from cortx.utils.discovery.error import DiscoveryError


class DiscoverySystem:
    """ A common interface of discovery system """

    def __init__(self, **kargs):
        pass

    @staticmethod
    def get_node_health(rpath=None, label=None, cached=True):
        """ This method provides node resource map and health information.

        param:
            rpath - Resource path in resource map to fetch its health.
                If rpath is None, it will fetch whole Cortx Node data health and display.
                Examples:
                "no-cluster>site_001>rack_001>cortx_node_1>sm_001>hw>disks>disk_001"
                "no-cluster>site_001>rack_001>cortx_node_1>sm_001"
                "no-cluster>site_001>rack_001>cortx_node_1>rss_5u84_001>hw>psus"
            label - Unique label will be tagged on resource map & health being
                generated. This can be used in future to fetch it back.
            cached - Fetch cached resorce map and health. If 'False' or no cache exists,
                afresh resource map and health will be fetched.
        return:
            A dictionary of node resource map.
        """
        pass

    @staticmethod
    def list_node_health_labels():
        """ Returns dictionary of persisted node health labels along with timestamp """
        pass

    @staticmethod
    def delete_labelled_node_health(label):
        """ Deletes cached node health label.

        return:
            Dictionary with deletion status (Success or Failure)
        """
        pass

    @staticmethod
    def compare_labelled_node_health(label1, label2, rpath=None):
        """ Compares two lables for a given resource path.

        param:
            label1, label2 - Node health lables.
            rpath - Resource path
        return:
            Difference of the given two label values in a dictionary.
            (label2-lable1)
        """
        pass

    @staticmethod
    def get_node_health_gen_status():
        """ Get status of last node health generation request.

        return:
            "processing" if last health generation request is being processed.
            "success" if health generation request is completed.
        """
        pass
