import importlib
import pkgutil
from pathlib import Path

def create_dict_tools():
    TOOLS = dict()

    package_dir = Path(__file__).parent

    for finder, name, ispkg in pkgutil.iter_modules([str(package_dir)]):
        if ispkg:
            module_path = f"{__name__}.{name}"
            package = importlib.import_module(module_path)

            subpackage_dir = Path(package.__file__).parent
            for _, sub_name, _ in pkgutil.iter_modules([str(subpackage_dir)]):
                full_module_name = f"{module_path}.{sub_name}"
                module = importlib.import_module(full_module_name)

                obj = getattr(module, sub_name)
                TOOLS[sub_name] = obj

    return TOOLS

TOOLS = create_dict_tools()

whois = TOOLS["whois_tool"]
shodan = TOOLS["shodan_tool"]
webcopy = TOOLS["webcopy_tool"]
ping = TOOLS["ping_tool"]
traceroute = TOOLS["traceroute_tool"]

toolSetReconnaissance = [
    ("Whois", whois),
    ("Shodan", shodan),
    ("Web copy", webcopy),
    ("Leave", lambda: None)
]

toolSetScanning = [
    ("Ping", ping),
    ("Traceroute", traceroute),
    ("Leave", lambda: None)
]

toolSetEnumeration = [
    ("Leave", lambda: None)
]

toolSetVulnerability = [
    ("Leave", lambda: None)
]

toolSetAccess = [
    ("Leave", lambda: None)
]
