from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute.v2020_06_01.models import DiskCreateOption, StorageAccountTypes


credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')

resource_group_name = 'StartShip'