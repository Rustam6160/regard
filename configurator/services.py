from .models import *



def check_cpu_motherboard_compatibility(cpu, motherboard):
    return cpu.socket == motherboard.socket

def check_ram_motherboard_compatibility(ram, motherboard):
    return ram.memory_type == motherboard.ram_type

def check_gpu_motherboard_compatibility(gpu, motherboard):
    return gpu.interface == motherboard.pcie_version

def check_psu_gpu_compatibility(psu, gpu):
    return psu.pcie_connectors >= 1 and gpu.additional_power_needed

def check_case_gpu_compatibility(case, gpu):
    return gpu.dimensions_mm <= case.max_gpu_length_mm

def check_case_motherboard_compatibility(case, motherboard):
    supported_sizes = case.form_factor_support.split(', ')
    return motherboard.form_factor in supported_sizes

def check_storage_motherboard_compatibility(storage, motherboard):
    if storage.storage_type == "NVMe":
        return "M.2" in motherboard.form_factor_support
    else:
        return "SATA-III" in motherboard.sata_ports
