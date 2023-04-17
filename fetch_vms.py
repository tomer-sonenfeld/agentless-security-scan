from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
subscription_id ='d92e7f13-b7ac-4ace-af5a-562f364d6c45'
compute_client = ComputeManagementClient(credential, subscription_id)
vms = compute_client.virtual_machines.list_all()
vms_list=[v for v in vms]
print(vms_list)