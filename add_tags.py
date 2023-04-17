from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential,
                                         subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')
resource_client = ResourceManagementClient(credential,
                                           subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')
vm = compute_client.virtual_machines.get(resource_group_name='StartShip',
                                         vm_name='test-auth')
vm.tags.update({'test_tag2': 'tagged'})
vm.tags.pop('test_tag1', None)
vm.tags.update({'test_tag2': 'tagged_updated'})
compute_client.virtual_machines.begin_create_or_update(resource_group_name='StartShip',
                                                       vm_name='test-auth',
                                                       parameters=vm)
