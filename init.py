import common
import sys
import argparse


def get_intro_message():
    return f"  Atomia AzureRegionPurger v{common.params['VERSION']}"


def print_intro():
    print()
    print(f"===== {get_intro_message()} =====")
    print()


def check_python_version():
    common.print_info("Checking python version")
    if sys.version_info[0] < 3:
        common.print_error("This is Python 3 script. Please run it using 'python3'")
        exit(1)


def check_if_logged():
    common.print_info("Checking if user is logged")
    common.shell_exec("az account show")


def check_azure_installation():
    common.print_info("Checking if azure-cli is installed")
    result = common.shell_exec("az --help")
    if result.returncode != 0:
        common.print_error("azure-cli is not installed")
        exit(1)


def check_azure_cli_version():
    common.print_info("Checking azure-cli version")
    # TODO Warn user that this script may not work on newer version than 2.x.x. Built on 2.0.46
    pass
#     command_result = common.shell_exec("az --version")
#     version_line = command_result.stdout.decode("utf-8").splitlines()[0]
#     version_full = re.search("\d(?!\()+.\d+(.\d*)(?=\))",version_line).group(0)
#     version_main = re.search("\d+(?=.)", version_full).group(0)
#     version_minor = re.search("\d+(?!.)(?=.)", version_full).group(0)
#     print(version_full, version_main)
#     exit()


def parse_arguments():
    parser = argparse.ArgumentParser(description=get_intro_message())
    parser.add_argument("region", help="Azure region to purge (ex. WestEurope)")
    parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true")
    args = parser.parse_args()
    common.params['VERBOSE'] = args.verbose
    common.params['AZURE_REGION'] = str(args.region).lower()