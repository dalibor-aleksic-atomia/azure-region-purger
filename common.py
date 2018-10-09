import subprocess
import sys
from datetime import datetime

params = {
    "VERBOSE": False,
    "AZURE_REGION": "",
    "VERSION": 0.1
}


def _print_message(message: str, msg_type: str, stderr: bool = False):
    print(f"[{datetime.utcnow()}][{msg_type.upper()}] {message}",
          file=sys.stderr if stderr else sys.stdout)


def print_info(message: str):
    _print_message(message, "info")


def print_error(message: str):
    _print_message(message, "error", stderr=True)


def print_warring(message: str):
    _print_message(message, "warning")


def print_verbose(message: str):
    if params['VERBOSE']:
        _print_message(message, "verbose")


def _format_command(command: str):
    if not str.startswith(command, "az"):
        return command
    return f"{command} --output=json"


def shell_exec(command: str, exit_on_fail: bool = True):
    try:
        formatted_command = _format_command(command)

        print_verbose(f"Executing: {formatted_command}")
        result = subprocess.run(formatted_command.split(),
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                check=True)
        print_verbose(f"Execution output: \n"
                      f"Stdout: {result.stdout.decode('utf-8')}\n"
                      f"Stderr: {result.stderr.decode('utf-8')}")
        return result
    except subprocess.CalledProcessError as error:
        print_error(f"Command '{formatted_command}' failed to execute. \n"
                    f"ReturnCode: {error.returncode} \n"
                    f"Stdout: {error.stdout.decode('utf-8')}\n"
                    f"Stderr: {error.stderr.decode('utf-8')}")
        if exit_on_fail:
            exit(error.returncode)


def process_start(command: str):
    formatted_command = _format_command(command)
    return subprocess.Popen(formatted_command,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)