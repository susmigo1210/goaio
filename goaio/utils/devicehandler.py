"""
Handles the connected android devices.
"""
import subprocess
from goaio.utils.loghandler import get_logger
from dataclasses import dataclass

device_handler_logger = get_logger(file_name=__name__)


@dataclass
class Device:
    name: str
    serial: str
    build: str
    manufacturer: str
    is_amati: bool


class Devices:

    def __init__(self):
        self.devices = []
        self.dut = None

    def get_connected_devices(self) -> list:
        command = ["adb", "devices", "-l"]
        try:
            raw_output = subprocess.check_output(args=command, text=True)
            for line in raw_output.strip('\n').splitlines()[1:]:
                device = line.split(" ")[0]
                self.devices.append(device)
            return self.devices
        except subprocess.CalledProcessError as e:
            device_handler_logger.error(f'Failed to get the connected devices. '
                                        f'Reason: {str(e)} , Exit Code: {e.returncode} ')

    # def get_device_info(self, device: str):
    #     _device = Device
    #     _device.name =
    #
    #     return Device


if __name__ == "__main__":
    d = Devices()
    print(d.get_connected_devices())
    # print(d.get_device_info("lol").build)
