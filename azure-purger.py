#!/usr/bin/env python3

"""
    Atomia AzureRegionPurger
    Remove all resources created in specific region
    Maintainer: Dalibor Aleksic (dalibor.aleksic@atomia.com)
    Github: https://github.com/dalibor-aleksic-atomia
"""

import common
import init
import resource_groups


def main():

    init.parse_arguments()
    init.print_intro()
    init.check_python_version()
    init.check_azure_installation()
    init.check_azure_cli_version()
    init.check_if_logged()

    all_groups = resource_groups.get_all()
    region_groups = resource_groups.filter_by_region(all_groups, common.params['AZURE_REGION'])

    default_legacy_groups = resource_groups.filter_default_groups(region_groups)
    standard_groups = resource_groups.exclude_default_resource_groups(region_groups)

    # Delete resources created with new ResourceManager mode
    # https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-deployment-model
    resource_groups.delete_many_parallel(standard_groups)

    # Delete resources created with classic (legacy) mode
    # TODO Consider: Delete Default-Storage-Group and recreate it empty
    for group in default_legacy_groups:
        resource_groups.delete_all_resources(group)

    common.print_info("Done")
    exit(0)


if __name__ == "__main__":
    main()