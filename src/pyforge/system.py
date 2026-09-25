import sys
import platform
from pathlib import Path

def get_system_info():

    system_info = {
        "python_version": sys.version,
        "platform": platform.platform(),
        "architecture": platform.architecture()[0],
        "python_executable": sys.executable,
        "working_directory": str(Path.cwd())
    }

    return system_info