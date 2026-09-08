# Cn_package.py
# Wi-Fi Detector + Computer Networks Concepts Project
# Run: python3 Cn_package.py   (Linux)
# or   python Cn_package.py   (Windows)

import tkinter as tk
from tkinter import ttk
import subprocess
import platform
import socket
import threading
import time

# -----------------------------
# MAIN WINDOW
# -----------------------------
root = tk.Tk()
root.title("Wi-Fi Detector - CN Project")
root.geometry("950x650")
root.configure(bg="#0f172a")

# -----------------------------
# TITLE
# -----------------------------
title = tk.Label(
    root,
    text="📶 Wi-Fi Detector & Computer Networks Analyzer",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#0f172a"
)
title.pack(pady=15)

# -----------------------------
# OUTPUT BOX
# -----------------------------
output = tk.Text(
    root,
    height=22,
    width=110,
    bg="#111827",
    fg="lime",
    font=("Consolas", 11)
)
output.pack(pady=10)

# -----------------------------
# FUNCTIONS
# -----------------------------
def write(text):
    output.insert(tk.END, text + "\n")
    output.see(tk.END)

def clear_box():
    output.delete(1.0, tk.END)

# -----------------------------
# DETECT WIFI
# -----------------------------
def detect_wifi():
    clear_box()
    write("Scanning Wi-Fi...\n")

    try:
        # Try Windows command
        result = subprocess.check_output(
            "netsh wlan show interfaces",
            shell=True
        ).decode(errors="ignore")

        write(result)

    except:
        try:
            # Linux fallback
            result = subprocess.check_output(
                "nmcli dev wifi",
                shell=True
            ).decode(errors="ignore")

            write(result)

        except:
            write("Wi-Fi Scan Failed!")
            write("Use Windows Python for best support.")

# -----------------------------
# SHOW IP
# -----------------------------
def show_ip():
    clear_box()

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    write("🌐 IP Address Information")
    write("-----------------------------")
    write(f"Hostname   : {hostname}")
    write(f"IP Address : {ip}")

# -----------------------------
# DNS LOOKUP
# -----------------------------
def dns_lookup():
    clear_box()

    write("🌍 DNS Lookup")
    write("-----------------------------")

    sites = ["google.com", "youtube.com", "openai.com"]

    for site in sites:
        try:
            ip = socket.gethostbyname(site)
            write(f"{site}  --->  {ip}")
        except:
            write(f"{site}  ---> Failed")

# -----------------------------
# PING TEST
# -----------------------------
def ping_test():
    clear_box()
    write("📡 Pinging google.com ...\n")

    try:
        if platform.system() == "Windows":
            cmd = "ping google.com -n 4"
        else:
            cmd = "ping google.com -c 4"

        result = subprocess.check_output(
            cmd,
            shell=True
        ).decode(errors="ignore")

        write(result)

    except:
        write("Ping Failed!")

# -----------------------------
# LIVE SIGNAL
# -----------------------------
def live_signal():
    clear_box()
    write("📶 Live Signal Strength (updates every 3 sec)\n")

    def run():
        while True:
            try:
                result = subprocess.check_output(
                    "netsh wlan show interfaces",
                    shell=True
                ).decode(errors="ignore")

                for line in result.split("\n"):
                    if "Signal" in line:
                        write(line.strip())

                time.sleep(3)

            except:
                write("Live Signal not supported here.")
                break

    threading.Thread(target=run, daemon=True).start()

# -----------------------------
# TOPOLOGY WINDOW
# -----------------------------
def topology():
    top = tk.Toplevel(root)
    top.title("Network Topology")
    top.geometry("700x450")
    top.configure(bg="white")

    canvas = tk.Canvas(top, width=700, height=450, bg="white")
    canvas.pack()

    # Router
    canvas.create_rectangle(280, 30, 420, 90, fill="orange")
    canvas.create_text(350, 60, text="Router", font=("Arial", 14, "bold"))

    # PCs
    pcs = [(80, 220), (300, 220), (520, 220)]

    for x, y in pcs:
        canvas.create_rectangle(x, y, x+110, y+60, fill="lightblue")
        canvas.create_text(x+55, y+30, text="PC", font=("Arial", 12, "bold"))
        canvas.create_line(350, 90, x+55, y)

# -----------------------------
# ABOUT
# -----------------------------
def about():
    clear_box()
    write("📘 Computer Networks Concepts Used")
    write("-----------------------------------")
    write("1. Wi-Fi Detection")
    write("2. IP Addressing")
    write("3. DNS Resolution")
    write("4. Ping / ICMP")
    write("5. Signal Strength")
    write("6. Network Topology")

# -----------------------------
# BUTTONS
# -----------------------------
frame = tk.Frame(root, bg="#0f172a")
frame.pack(pady=10)

buttons = [
    ("Detect Wi-Fi", detect_wifi),
    ("Show IP", show_ip),
    ("DNS Lookup", dns_lookup),
    ("Ping Test", ping_test),
    ("Live Signal", live_signal),
    ("Topology", topology),
    ("About CN", about),
    ("Clear", clear_box)
]

row = 0
col = 0

for text, cmd in buttons:
    btn = tk.Button(
        frame,
        text=text,
        command=cmd,
        width=18,
        height=2,
        bg="#2563eb",
        fg="white",
        font=("Arial", 10, "bold")
    )
    btn.grid(row=row, column=col, padx=8, pady=8)

    col += 1
    if col == 4:
        col = 0
        row += 1

# -----------------------------
# FOOTER
# -----------------------------
footer = tk.Label(
    root,
    text="Mini Project using Python + Computer Networks",
    fg="gray",
    bg="#0f172a"
)
footer.pack(pady=10)

# -----------------------------
# RUN
# -----------------------------
root.mainloop()