import subprocess

def list_kernels():
    uname_process = subprocess.run(["uname", "-r"], capture_output=True, text=True)
    current_kernel_version = uname_process.stdout.strip()

    dpkg_process = subprocess.run(["dpkg", "-l", "linux-image-*"], capture_output=True, text=True)
    installed_kernels = dpkg_process.stdout.splitlines()[5:]

    print("Current kernel version:")
    print(current_kernel_version)
    print("\nInstalled kernels:")
    for kernel in installed_kernels:
        kernel_info = kernel.split()
        kernel_version = kernel_info[2]
        if kernel_version != current_kernel_version:
            print(kernel_version)

def remove_kernel(kernel_version):
    subprocess.run(["sudo", "apt", "remove", "-y", f"linux-image-{kernel_version}"])

def main():
    print("List of available kernels:")
    list_kernels()

    while True:
        user_input = input("\nEnter the kernel version you want to remove (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break

        remove_kernel(user_input)
        print(f"Kernel version {user_input} has been removed.")

if __name__ == "__main__":
    main()
