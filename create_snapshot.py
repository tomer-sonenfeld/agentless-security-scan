from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute.v2021_04_01.models import DiskCreateOption

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')

resource_group_name = "StartShip"
disk_name = "test_disk"
snapshot_name = "test_snap"
location = "uksouth"

snapshot_creation_data = {
    "location": location,
    "creation_data": {
        "create_option": DiskCreateOption.copy,
        "source_uri": compute_client.disks.get(resource_group_name, disk_name).id
    }
}

print ("Creating snapshot")
poller = compute_client.snapshots.begin_create_or_update(resource_group_name, snapshot_name, snapshot_creation_data)
print("Waiting for snapshot creation to complete..")
try:
    poller.wait()
    print(poller.status())
except Exception as e:
    print("Exception while creating snapshot : " + str(e))
