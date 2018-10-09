# azure-region-purger

Removes all associated resources from Azure region.

## Pre requirements
- Python 3
- You need to install **azure-cli**. [More info](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).
- You need to login to your Azure account in azure-cli using `az login` command. [More info](https://docs.microsoft.com/cli/azure/reference-index#az-login).

## Usage
### Purge region
`# python3 azure-purger.py region-name` 

where *region-name* is *westeurope* for example

### Purge region and verbose output
`# python3 azure-purger.py --verbose region-name`

### Show help
`# python3 azure-purger.py --help`
