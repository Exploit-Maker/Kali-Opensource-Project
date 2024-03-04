import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()

def test_nmap():
    print("Testing Nmap...")
    output = run_command("nmap localhost")
    print(f"Nmap Output:\n{output}")

def test_metasploit():
    print("Testing Metasploit...")
    output = run_command("msfconsole -q -x 'version; exit -y'")
    print(f"Metasploit Output:\n{output}")

def test_wireless_tools():
    print("Testing Wireless Tools...")
    output = run_command("iwconfig")
    print(f"Wireless Tools Output:\n{output}")

def test_ssl_analysis():
    print("Testing SSL Analysis Tools...")
    output = run_command("sslyze --regular localhost:443")
    print(f"SSL Analysis Output:\n{output}")

def main():
    print("Starting Kali Linux ARM Testing Script...\n")
    
    # Example test cases
    test_nmap()
    test_metasploit()
    test_wireless_tools()
    test_ssl_analysis()

    print("\nTesting script completed.")

if __name__ == "__main__":
    main()
