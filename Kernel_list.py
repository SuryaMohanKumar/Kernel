import subprocess

def list_kernels():
    rpm_process = subprocess.run(["rpm", "-qa", "kernel*"], capture_output=True, text=True)
    installed_kernels = rpm_process.stdout.splitlines()
    
    print("Available kernels:")
    for kernel in installed_kernels:
        print(kernel)

def main():
    list_kernels()

if __name__ == "__main__":
    main()
