import subprocess

def get_current_kernel_version():
    uname_process = subprocess.run(["uname", "-r"], capture_output=True, text=True)
    current_kernel_version = uname_process.stdout.strip()
    return current_kernel_version

def list_available_kernel_versions():
    rpm_process = subprocess.run(["rpm", "-qa", "kernel*"], capture_output=True, text=True)
    installed_kernels = rpm_process.stdout.splitlines()
    available_kernels = [kernel.split("-")[1] for kernel in installed_kernels]
    return available_kernels

def remove_kernel(kernel_version):
    subprocess.run(["sudo", "yum", "remove", "-y", f"kernel-{kernel_version}"])

def main():
    current_kernel = get_current_kernel_version()
    print("Current kernel version:", current_kernel)
    
    available_kernels = list_available_kernel_versions()
    print("\nAvailable kernel versions:")
    for kernel in available_kernels:
        print(kernel)
    
    while True:
        user_input = input("\nEnter the kernel version you want to remove (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break

        if user_input == current_kernel:
            print("Cannot remove the current kernel.")
        elif user_input in available_kernels:
            remove_kernel(user_input)
            print(f"Kernel version {user_input} has been removed.")
        else:
            print("Invalid kernel version. Please try again.")

if __name__ == "__main__":
    main()
