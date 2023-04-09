from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')
snapshots = [s for s in compute_client.snapshots.list()]
print("snpshots= "+str([s.name for s in snapshots]))
print("hello world")