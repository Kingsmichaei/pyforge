from .system import get_system_info

def main():
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()