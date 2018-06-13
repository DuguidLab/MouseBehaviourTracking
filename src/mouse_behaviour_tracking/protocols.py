"""
Load and parse protocol specs
"""
import os
import yaml


def load_protocol(protocol_name, path):
    """Load behavioural protocol parameters"""
    protocol_path = os.path.join(path, os.sep, protocol_name, '.yml')
    if not os.path.exists(protocol_path):
        raise Exception("Protocol " + str(protocol_name) + " does not exist!")
    return yaml.load(protocol_path)
