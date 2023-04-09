from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')
snapshots = [s for s in compute_client.snapshots.list()]
snap_to_delete = snapshots[0]
print("Deleting snapshot = "+snap_to_delete.name)
snap_group = snap_to_delete.id.split('/')[4]
snap_name = snap_to_delete.name
async_snapshot_delete = compute_client.snapshots.begin_delete(resource_group_name=snap_group, snapshot_name=snap_name)