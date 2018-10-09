import common
import json


def get_all(resource_group_name: str):
    common.print_info(f"Fetching resources in ResourceGroup {resource_group_name}")
    command_result = common.shell_exec(f"az resource list -g {resource_group_name}")
    resources = json.loads(command_result.stdout)
    return resources


def delete(res):
    resource_id = res['id']
    resource_name = res['name']
    common.print_info(f'Deleting Resource: {resource_name}')
    common.shell_exec(f'az resource delete --ids {resource_id}', exit_on_fail=False)
