from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')
disks = [d for d in compute_client.disks.list()]
disk_to_delete = disks[3]
print("Deleting snapshot = "+snap_to_delete.name)
disk_group = disk_to_delete.id.split('/')[4]
disk_name = disk_to_delete.name
disk_vm = disk_to_delete.managed_by.split('/')[-1]
vm = compute_client.virtual_machines.get(disk_group,disk_vm)
compute_client_disks_begin_delete = compute_client.disks.begin_delete(resource_group_name=disk_group, disk_name=disk_name, delete_option=DiskDeleteOptionTypes.delete)