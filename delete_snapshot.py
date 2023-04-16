from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')

resource_group_name = 'StartShip'
snapshots = [s for s in compute_client.snapshots.list()]
snap_to_delete = snapshots[0]
snap_name = snap_to_delete.name

print("Deleting snapshot")
poller = compute_client.snapshots.begin_delete(resource_group_name=resource_group_name, snapshot_name=snap_name)
print("Waiting for snapshot deletion to complete..")
try:
    poller.wait()
    print(poller.status())
except Exception as e:
    print("Exception while deleting snapshot : " + str(e))
