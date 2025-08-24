"""
@date: 2025/8/24
@author: tangle
"""
import uuid
import hashlib
import platform
# import os


def get_unique_device_id():
    # Get machine-specific information
    system_info = platform.platform()
    node_info = platform.node()
    processor_info = platform.processor()
    mac = uuid.getnode()  # Get MAC address (may change if using virtual machine)
    print(f'sys {system_info}\n'
          f'node {node_info}\n'
          f'process {processor_info}\n'
          f'mac {mac}'
          )

    # Combine the collected information into one string
    raw_string = f"{system_info}-{node_info}-{processor_info}-{mac}"

    # Hash the combined string to generate a fixed-length ID
    device_id = hashlib.sha256(raw_string.encode()).hexdigest()

    return device_id


if __name__ == "__main__":
    print("Unique Device ID:", get_unique_device_id())
