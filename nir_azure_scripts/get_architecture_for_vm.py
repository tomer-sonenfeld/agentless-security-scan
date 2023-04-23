from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential

subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45'
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)
resource_group_name = "StartShip"

vms = [v for v in compute_client.virtual_machines.list_all()]
v0 = vms[0]
disk_name = v0.storage_profile.os_disk.name
d = compute_client.disks.get(resource_group_name, disk_name)
arc = d.supported_capabilities.architecture
print("os_type from virtual machine is : "+v0.storage_profile.os_disk.os_type)
print(arc) # arm processors start with Arm__, for exg. Arm64 default is AMD


