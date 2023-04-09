from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')

vms = [v for v in compute_client.virtual_machines.list_all()]
v0 = vms[0]

print(v0.storage_profile.os_disk.os_type)