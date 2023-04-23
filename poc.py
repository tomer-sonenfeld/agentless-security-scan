from datetime import datetime
from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute.models import DiskCreateOption

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')


# do we need to filter by windows/arm? or do we want to comment all machines that have/haven't been scanned?
def fetch_vms_by_resource_group(resource_group_name: str) -> list:
    vms = compute_client.virtual_machines.list(resource_group_name)
    vms_list = [v for v in vms]
    return vms_list


def fetch_disks_by_vm(resource_group_name: str, vm_name: str) -> list:
    disks = compute_client.disks.list_by_resource_group(resource_group_name)
    disks_list = [d for d in disks]
    return disks_list

#Nir/shir
def create_snapshot_of_disk(resource_group_name: str, disk_name: str, snapshot_name: str) -> None:
    # from azure.mgmt.compute.models import DiskCreateOption
    disk = compute_client.disks.get(resource_group_name, disk_name)

    snapshot_creation_data = {
        "location": disk.location,
        "creation_data": {
            "create_option": DiskCreateOption.COPY,
            "source_uri": disk.id
        }
    }
    print(f"Creating snapshot {snapshot_name} from disk {disk_name}")
    poller = compute_client.snapshots.begin_create_or_update(resource_group_name, snapshot_name, snapshot_creation_data)
    print(f"Waiting for snapshot {snapshot_name} creation to complete..")
    try:
        poller.wait()
        print(poller.status())
    except Exception as e:
        print(f"Exception {str(e)} while creating snapshot {snapshot_name}")

#Saar
def tag_disk(resource_group_name: str, disk_name: str, tag: str) -> None:
    pass

#Saar
def tag_snapshot(resource_group_name: str, snapshot_name: str, tag: str) -> None:
    pass

#nir/shir
def create_disk_from_snapshot(resource_group_name: str, snapshot_name: str, disk_name: str) -> None:
    # from azure.mgmt.compute.models import DiskCreateOption
    snapshot = compute_client.snapshots.get(resource_group_name, snapshot_name)
    resource_availability_zones = [av for av in compute_client.availability_sets.list(resource_group_name)]
    poller = compute_client.disks.begin_create_or_update(
        resource_group_name,
        disk_name,
        {
            'creation_data': {
                'create_option': DiskCreateOption.COPY,
                'source_uri': snapshot.id
            },
            'location': snapshot.location,
            'zones': resource_availability_zones
        }
    )
    print(f"Waiting for disk {disk_name} creation from {snapshot_name} to complete..")
    try:
        poller.wait()
        print(poller.status())
    except Exception as e:
        print(f"Exception {str(e)} while creating disk {disk_name} creation from {snapshot_name}")


# tomer
def attach_disk_to_vm(resource_group_name: str, vm_name: str, disk_name: str) -> None:
    pass

# tomer
def mount_disk_on_vm(resource_group_name: str, vm_name: str, disk_name: str) -> None:
    pass

# tomer
def unmount_disk_from_vm(resource_group_name: str, vm_name: str, disk_name: str) -> None:
    pass

#nir/shir
def delete_snapshot_of_disk(resource_group_name: str, snapshot_name: str) -> None:
    print(f"Deleting snapshot {snapshot_name}")
    poller = compute_client.snapshots.begin_delete(resource_group_name=resource_group_name, snapshot_name=snapshot_name)
    print(f"Waiting for snapshot {snapshot_name} deletion to complete..")
    try:
        poller.wait()
        print(poller.status())
    except Exception as e:
        print(f"Exception {str(e)} while deleting snapshot {snapshot_name}")


#nir/shir
def detach_and_delete_disk(resource_group_name: str, vm_name: str, disk_name: str) -> None:
    pass

#nir/shir
def rezilion_scan(resource_group_name: str, vm_name: str) -> None:
    # needs to check for each vm if should_scan_compute -
    # is supported architechre
    # scan window elapsed from last_scan and we should scan again
    # not our Rezilion's vm
    print("Scan Completed")

# saar
def tag_vm(resource_group_name: str, vm_name: str, tag: str) -> None:
    pass


if __name__ == '__main__':
    vms = fetch_vms_by_resource_group('StartShip')
    for vm in vms:
        disks = fetch_disks_by_vm('StartShip', vm.name)
        for disk in disks:
            snapshot_name = f"{disk.name}-snapshot"
            disk_from_snapshot_name = f"{disk.name}-from-snapshot"
            rezilion_vm_name = 'rezilion_vm'
            create_snapshot_of_disk('StartShip', disk.name, snapshot_name)
            tag_snapshot('StartShip', snapshot_name, 'rezilion-generated')
            create_disk_from_snapshot('StartShip', disk.name, disk_from_snapshot_name)
            tag_disk('StartShip', disk_from_snapshot_name, 'rezilion-generated')
            attach_disk_to_vm('StartShip', rezilion_vm_name, disk_from_snapshot_name)
            mount_disk_on_vm('StartShip', rezilion_vm_name, disk_from_snapshot_name)

            rezilion_scan('StartShip', rezilion_vm_name)

            unmount_disk_from_vm('StartShip', rezilion_vm_name, disk_from_snapshot_name)
            delete_snapshot_of_disk('StartShip', snapshot_name)
            detach_and_delete_disk('StartShip', rezilion_vm_name, disk_from_snapshot_name)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tag_vm('StartShip', vm.name, 'rezilion-scanned', timestamp)
