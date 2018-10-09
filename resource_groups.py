import common
import json
import resources


def get_all():
    common.print_info("Fetching ResourceGroups")
    command_result = common.shell_exec("az group list")
    groups = json.loads(command_result.stdout)
    return groups


def filter_by_region(groups, region: str):
    common.print_info(f"[Filter] Filtering ResourceGroups by region: {region}")
    result_list = []
    for group in groups:
        if group["location"] == region:
            result_list.append(group)
    return result_list


def exclude_region(groups, region: str):
    common.print_info(f"[Filter] Excluding ResourceGroups by region: {region}")
    result_list = []
    for group in groups:
        if group["location"] != region:
            result_list.append(group)
    return result_list


def filter_default_groups(groups):
    common.print_info("[Filter] Filtering Default ResourceGroups")
    result_list = []
    for group in groups:
        if str.startswith(group["name"], "Default"):
            result_list.append(group)
    return result_list


def exclude_default_resource_groups(groups):
    common.print_info(f"[Filter] Excluding Default ResourceGroups")
    result_list = []
    for group in groups:
        if not str.startswith(group["name"], "Default"):
            result_list.append(group)
    return result_list


def delete(group):
    name = group["name"]
    common.print_info(f'Deleting ResourceGroup: {name}. May take couple of minutes..')
    common.shell_exec(f"az group delete --name {name} --yes")


def delete_many(groups):
    for group in groups:
        delete(group)


def delete_all_resources(group):
    group_name = group["name"]
    resource_list = resources.get_all(group_name)
    common.print_info(f"Delete resources in group {group_name} started")
    for res in resource_list:
        resources.delete(res)
    common.print_info(f"Delete resources in group {group_name} finished")
    """
    TODO: Check if resource deletion failed (ex. vhds locked)
          and try to unlock it.
          1. Get-Storage-Access-Key (az storage account keys [list])
          2. Set-Storage-Access-Key (env var?)
          3. Break Lease 
          https://docs.microsoft.com/en-us/cli/azure/storage/blob/lease?view=azure-cli-latest#az-storage-blob-lease-break
    """