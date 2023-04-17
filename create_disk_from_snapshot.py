from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential

subscription_id = 'd92e7f13-b7ac-4ace-af5a-562f364d6c45'
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential,subscription_id)

resource_group_name = 'StartShip'
snapshot_name = 'test_snap'
disk_name = 'disk_snap'
location = 'uksouth'

creation_data = {
    'create_option': 'Copy',
    'source_uri': f'/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/snapshots/{snapshot_name}'
}

print("Creating disk from snapshot")
poller = compute_client.disks.begin_create_or_update(
    resource_group_name,
    disk_name,
    {
        'creation_data': creation_data,
        'location': location,
        'zones': ['1']
    }
)
print("Waiting for disk creation to complete..")
try:
    poller.wait()
    print(poller.status())
except Exception as e:
    print("Exception while creating disk : " + str(e))
