from modules.imports import *

def print_warning(old_ram_flag, new_ram_flag, needed_vram, detected_vram):
    print(f"WARNING: CUDA was chosen, but the VRAM available is less than {old_ram_flag}. You have {detected_vram:.2f} MB available, and {needed_vram - detected_vram:.2f} MB additional overhead is needed. Setting ram flag to avoid out of memory errors. New Flag: {new_ram_flag}")
    print(
        "Remember that the system will use VRAM for other processes, so you may need to lower the ram flag even more to avoid out of memory errors."
    )

print("Warnings Module Loaded")