from datetime import datetime
from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')


def fetch_vms_by_resource_group(resource_group_name: str) -> list:
    vms = compute_client.virtual_machines.list(resource_group_name)
    vms_list = [v for v in vms]
    return vms_list


def fetch_disks_by_vm(resource_group_name: str, vm_name: str) -> list:
    disks = compute_client.disks.list_by_resource_group(resource_group_name)
    disks_list = [d for d in disks]
    return disks_list


def create_snapshot_of_disk(resource_group_name: str, disk_name: str, snapshot_name: str) -> None:
    pass


def tag_disk(resource_group_name: str, disk_name: str, tag: str) -> None:
    pass


def tag_snapshot(resource_group_name: str, snapshot_name: str, tag: str) -> None:
    pass


def create_disk_from_snapshot(resource_group_name: str, snapshot_name: str, disk_name: str) -> None:
    pass


def attach_disk_to_vm(resource_group_name: str, vm_name: str, disk_name: str) -> None:
    pass


def mount_disk_on_vm(resource_group_name: str, vm_name: str, disk_name: str) -> None:
    pass


def unmount_disk_from_vm(resource_group_name: str, vm_name: str, disk_name: str) -> None:
    pass


def delete_snapshot_of_disk(resource_group_name: str, snapshot_name: str) -> None:
    pass


def detach_and_delete_disk(resource_group_name: str, vm_name: str, disk_name: str) -> None:
    pass


def rezilion_scan(resource_group_name: str, vm_name: str) -> None:
    print("Scan Completed")


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
