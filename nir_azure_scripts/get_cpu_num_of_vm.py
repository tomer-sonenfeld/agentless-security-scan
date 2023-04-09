import re
from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id='d92e7f13-b7ac-4ace-af5a-562f364d6c45')

vms = [v for v in compute_client.virtual_machines.list_all()]
v0 = vms[0]
vm_size = v0.hardware_profile.vm_size
cpu_regex = "(?<=_D)\d+"
num_cpus = re.findall(cpu_regex, vm_size)[0]
print("number of cpus for vm0 is: "+str(num_cpus))