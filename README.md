# 🧠 MAC Address Changer

A simple Python tool that changes the MAC address of a network interface to enhance privacy and test network security.  
Built for learning, ethical hacking, and cybersecurity practice.

---

## 🎯 Objective
This project demonstrates how to use Python for **network interface manipulation**.  
It helps users understand how MAC addresses can be changed programmatically using system commands — a core concept in **network security** and **ethical hacking**.

---

## 🧩 Features
- View the current MAC address of any network interface  
- Change the MAC address to a new one provided by the user  
- Verify that the MAC address was successfully changed  
- Lightweight and requires **no external Python libraries**

---

## ⚙️ Requirements
- **Operating System:** Linux (tested on Kali Linux)  
- **Python:** 3.x (Python 3.10+ recommended)  
- **Tool:** `ifconfig` (from `net-tools` package)

> 🛠️ Install `net-tools` if not already installed:
> ```bash
> sudo apt update && sudo apt install net-tools
> ```

---

## 🚀 Usage

1. **Clone this repository**
   ```bash
   git clone https://github.com/alagskomahd/mac-address-changer.git
   cd mac-address-changer
   
2. **Run the script with root privileges**
   ```bash
   sudo python3 mac_changer.py -i <interface> -m <new-mac-address>
   
3. **Example**
   ```bash
   sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55

4. **Expected Output**
   ```pgsql
   Current MAC address = aa:bb:cc:dd:ee:ff
   [+] Changing MAC address for eth0 to 00:11:22:33:44:55
   [+] MAC address was successfully changed to 00:11:22:33:44:55

5. **If the MAC did not change, the script prints:**
   ```css
   [-] MAC address did not change

🧠 How It Works

Uses the subprocess module to execute system commands.

Extracts the current MAC address using a regular expression.

Brings the network interface down, changes the MAC, then brings it back up.

Re-checks to confirm the change was successful.

👤 Author

Dennis Alagskomah (alagskomahd)
🎓 BSc Information Technology, University of Cape Coast, Ghana
💻 Passionate about Cybersecurity, Network Security, and Cloud Security
📫 Email: alagskomah25@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/alagskomah/
   






   
