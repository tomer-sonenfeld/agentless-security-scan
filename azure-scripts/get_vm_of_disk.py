from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')
disks = [d for d in compute_client.disks.list()]
disk = disks[2]
vm_name = disk.managed_by.split('/')[-1]

print("This disk belongs to vm = "+vm_name)

vms = compute_client.virtual_machines.list_all()
vms_list=[v for v in vms]

for vm in vms_list:
    if vm.name == vm_name:
        print("VM details = "+str(vm))