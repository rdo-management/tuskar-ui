#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from openstack_dashboard.test.test_data import utils as test_data_utils

from ironicclient.v1 import node
from ironicclient.v1 import port
from novaclient.v1_1.contrib import baremetal


def data(TEST):

    # BareMetalNode
    TEST.baremetalclient_nodes = test_data_utils.TestDataContainer()
    bm_node_1 = baremetal.BareMetalNode(
        baremetal.BareMetalNodeManager(None),
        {'id': '1',
         'uuid': 'aa-11',
         'instance_uuid': 'aa',
         "service_host": "undercloud",
         "cpus": 1,
         "memory_mb": 4096,
         "local_gb": 20,
         'task_state': 'active',
         "pm_address": None,
         "pm_user": None,
         "interfaces": [{"address": "52:54:00:90:38:01"},
                        {"address": "52:54:00:90:38:01"}],
         })
    bm_node_2 = baremetal.BareMetalNode(
        baremetal.BareMetalNodeManager(None),
        {'id': '2',
         'uuid': 'bb-22',
         'instance_uuid': 'bb',
         "service_host": "undercloud",
         "cpus": 1,
         "memory_mb": 4096,
         "local_gb": 20,
         'task_state': 'active',
         "pm_address": None,
         "pm_user": None,
         "interfaces": [{"address": "52:54:00:90:38:01"}],
         })
    bm_node_3 = baremetal.BareMetalNode(
        baremetal.BareMetalNodeManager(None),
        {'id': '3',
         'uuid': 'cc-33',
         'instance_uuid': 'cc',
         "service_host": "undercloud",
         "cpus": 1,
         "memory_mb": 4096,
         "local_gb": 20,
         'task_state': 'reboot',
         "pm_address": None,
         "pm_user": None,
         "interfaces": [{"address": "52:54:00:90:38:01"}],
         })
    bm_node_4 = baremetal.BareMetalNode(
        baremetal.BareMetalNodeManager(None),
        {'id': '4',
         'uuid': 'cc-44',
         'instance_uuid': 'cc',
         "service_host": "undercloud",
         "cpus": 1,
         "memory_mb": 4096,
         "local_gb": 20,
         'task_state': 'active',
         "pm_address": None,
         "pm_user": None,
         "interfaces": [{"address": "52:54:00:90:38:01"}],
         })
    bm_node_5 = baremetal.BareMetalNode(
        baremetal.BareMetalNodeManager(None),
        {'id': '5',
         'uuid': 'dd-55',
         'instance_uuid': 'dd',
         "service_host": "undercloud",
         "cpus": 1,
         "memory_mb": 4096,
         "local_gb": 20,
         'task_state': 'error',
         "pm_address": None,
         "pm_user": None,
         "interfaces": [{"address": "52:54:00:90:38:01"}],
         })
    TEST.baremetalclient_nodes.add(
        bm_node_1, bm_node_2, bm_node_3, bm_node_4, bm_node_5)

    # IronicNode
    TEST.ironicclient_nodes = test_data_utils.TestDataContainer()
    node_1 = node.Node(
        node.NodeManager(None),
        {'id': '1',
         'uuid': 'aa-11',
         'instance_uuid': 'aa',
         'driver': 'pxe_ipmitool',
         'driver_info': {
             'ipmi_address': '1.1.1.1',
             'ipmi_username': 'admin',
             'ipmi_password': 'password',
             'ip_address': '1.2.2.2'
         },
         'properties': {
             'cpu': '8',
             'ram': '16',
             'local_disk': '10',
         },
         'power_state': 'on',
         })
    node_2 = node.Node(
        node.NodeManager(None),
        {'id': '2',
         'uuid': 'bb-22',
         'instance_uuid': 'bb',
         'driver': 'pxe_ipmitool',
         'driver_info': {
             'ipmi_address': '2.2.2.2',
             'ipmi_username': 'admin',
             'ipmi_password': 'password',
             'ip_address': '1.2.2.3'
         },
         'properties': {
             'cpu': '16',
             'ram': '32',
             'local_disk': '100',
         },
         'power_state': 'on',
         })
    node_3 = node.Node(
        node.NodeManager(None),
        {'id': '3',
         'uuid': 'cc-33',
         'instance_uuid': 'cc',
         'driver': 'pxe_ipmitool',
         'driver_info': {
             'ipmi_address': '3.3.3.3',
             'ipmi_username': 'admin',
             'ipmi_password': 'password',
             'ip_address': '1.2.2.4'
         },
         'properties': {
             'cpu': '32',
             'ram': '64',
             'local_disk': '1',
         },
         'power_state': 'rebooting',
         })
    node_4 = node.Node(
        node.NodeManager(None),
        {'id': '4',
         'uuid': 'cc-44',
         'instance_uuid': 'cc',
         'driver': 'pxe_ipmitool',
         'driver_info': {
             'ipmi_address': '4.4.4.4',
             'ipmi_username': 'admin',
             'ipmi_password': 'password',
             'ip_address': '1.2.2.5'
         },
         'properties': {
             'cpu': '8',
             'ram': '16',
             'local_disk': '10',
         },
         'power_state': 'on',
         })
    node_5 = node.Node(
        node.NodeManager(None),
        {'id': '5',
         'uuid': 'dd-55',
         'instance_uuid': 'dd',
         'driver': 'pxe_ipmitool',
         'driver_info': {
             'ipmi_address': '5.5.5.5',
             'ipmi_username': 'admin',
             'ipmi_password': 'password',
             'ip_address': '1.2.2.6'
         },
         'properties': {
             'cpu': '8',
             'ram': '16',
             'local_disk': '10',
         },
         'power_state': 'error',
         })
    TEST.ironicclient_nodes.add(node_1, node_2, node_3, node_4, node_5)

    # Ports
    TEST.ironicclient_ports = test_data_utils.TestDataContainer()
    port_1 = port.Port(
        port.PortManager(None),
        {'id': '1-port-id',
         'type': 'port',
         'address': 'aa:aa:aa:aa:aa:aa'})
    port_2 = port.Port(
        port.PortManager(None),
        {'id': '2-port-id',
         'type': 'port',
         'address': 'bb:bb:bb:bb:bb:bb'})
    port_3 = port.Port(
        port.PortManager(None),
        {'id': '3-port-id',
         'type': 'port',
         'address': 'cc:cc:cc:cc:cc:cc'})
    port_4 = port.Port(
        port.PortManager(None),
        {'id': '4-port-id',
         'type': 'port',
         'address': 'dd:dd:dd:dd:dd:dd'})
    TEST.ironicclient_ports.add(port_1, port_2, port_3, port_4)