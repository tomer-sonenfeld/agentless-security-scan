from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')
disks = [d for d in compute_client.disks.list()]
disk = disks[2]
print("This disk belongs to vm = "+disk.managed_by)