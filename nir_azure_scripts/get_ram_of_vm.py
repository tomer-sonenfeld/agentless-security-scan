import re
from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential

subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45'
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)
location = "uksouth"
vs_sizes = [s for s in compute_client.virtual_machine_sizes.list(location)]

vms = [v for v in compute_client.virtual_machines.list_all()]
v0 = vms[0]
vm_size_name = v0.hardware_profile.vm_size
for vs_size in vs_sizes:
    if vs_size.name == vm_size_name:
        vm_size = vs_size
        break
