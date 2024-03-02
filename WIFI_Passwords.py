import subprocess

def get_wifi_profiles():
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        return profiles
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve Wi-Fi profiles.")
        return []

def get_wifi_password(profile_name):
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        password = [b.split(":")[1][1:-1] for b in result if "Key Content" in b]
        return password[0] if password else ""
    except subprocess.CalledProcessError:
        return "ENCODING ERROR"

def main():
    wifi_profiles = get_wifi_profiles()
    
    if not wifi_profiles:
        return

    print("{:<30} | {:<}".format("Wi-Fi Profile", "Password"))
    print("=" * 45)
    
    for profile in wifi_profiles:
        password = get_wifi_password(profile)
        print("{:<30} | {:<}".format(profile, password))

    input("Press Enter to exit.")

if __name__ == "__main__":
    main()
