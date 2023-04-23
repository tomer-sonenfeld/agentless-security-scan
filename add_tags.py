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

# Not for use
def tag_disk(resource_group_name: str, disk_name: str, tag: str) -> None:
    disk = compute_client.disks.get(resource_group_name=resource_group_name, disk_name = disk_name)
    disk.tags.update({'rezilion-generated': tag})

# Not for use
def tag_snapshot(resource_group_name: str, snapshot_name: str, tag: str) -> None:
    snapshot = compute_client.snapshots.get(resource_group_name=resource_group_name, snapshot_name=snapshot_name)
    snapshot.tags.update({'rezilion-generated': tag})

# Not for use
def tag_vm(resource_group_name: str, vm_name: str, tag: str) -> None:
    vm = compute_client.virtual_machines.get(resource_group_name=resource_group_name, vm_name=vm_name)
    vm.tags.update({'rezilion-generated': tag})

# saar
def tag_resource_scanned(resource, value: str) -> None:
    resource.tags.update({'rezilion-scanned': value})

# saar
def tag_resource_generated(resource, value: str) -> None:
    resource.tags.update({'rezilion-generated': value})

# saar
def remove_tag_resource_scanned(resource) -> None:
    resource.tags.pop('rezilion-scanned', None)

# saar
def remove_tag_resource_generated(resource) -> None:
    resource.tags.pop('rezilion-generated', None)





"""
vm.tags.update({'test_tag2': 'tagged'})
vm.tags.pop('test_tag1', None)
vm.tags.update({'test_tag2': 'tagged_updated'})
compute_client.virtual_machines.begin_create_or_update(resource_group_name='StartShip',
                                                       vm_name='test-auth',
                                                       parameters=vm)
"""
