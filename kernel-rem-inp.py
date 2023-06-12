import subprocess

def remove_kernel(kernel_version):
    subprocess.run(["sudo", "yum", "remove", "-y", f"kernel-{kernel_version}"])

def main():
    kernel_version = input("Enter the kernel version you want to remove: ")
    remove_kernel(kernel_version)
    print(f"Kernel version {kernel_version} has been removed.")

if __name__ == "__main__":
    main()
