from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')

resource_group_name = 'StartShip'
disk_to_delete = compute_client.disks.get(resource_group_name=resource_group_name, disk_name='test_disk')
vm_of_disk_id = disk_to_delete.managed_by.split('/')[-1]
vm_of_disk = compute_client.virtual_machines.get(resource_group_name=resource_group_name, vm_name=vm_of_disk_id)

for disk in vm_of_disk.storage_profile.data_disks:
    if disk.name == disk_to_delete.name:
        disk_to_delete = disk

print("Detaching disk from VM")
vm_of_disk.storage_profile.data_disks.remove(disk_to_delete)
print("Updating VM")
poller = compute_client.virtual_machines.begin_create_or_update(resource_group_name=resource_group_name,
                                                                vm_name=vm_of_disk.name, parameters=vm_of_disk)
print("Waiting for VM update to complete..")
try:
    poller.wait()
    print(poller.status())
except Exception as e:
    print("Exception while updating VM : " + str(e))

print("Deleting disk")
poller = compute_client.disks.begin_delete(resource_group_name=resource_group_name, disk_name=disk_to_delete.name)
print("Waiting for disk deletion to complete..")
try:
    poller.wait()
    print(poller.status())
except Exception as e:
    print("Exception while deleting disk : " + str(e))
