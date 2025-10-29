# 📡 ESP8266 UART Communication (Transmit Data) — MicroPython

## 🧠 Overview
This project demonstrates **UART serial communication** using the **ESP8266** and **MicroPython**.  
The ESP8266 transmits the message `"Hello"` every 2 seconds through the UART interface at a baud rate of **115200 bps**.  
This data can be viewed on the **Thonny Shell**, **Serial Monitor**, or software like **RealTerm**, **PuTTY**, or **CoolTerm**.

---

## ⚙️ Hardware Setup

| Component | ESP8266 Pin | Description |
|------------|-------------|--------------|
| UART TX    | GPIO1 (TX)  | Serial transmit |
| UART RX    | GPIO3 (RX)  | Serial receive |
| GND        | GND         | Common ground |

🔹 The **UART0** interface on the ESP8266 uses **GPIO1 (TX)** and **GPIO3 (RX)**.  
🔹 Connect a **USB-to-UART converter** (if needed) or monitor through the built-in serial port in **Thonny IDE**.

---

## 🧩 Code

```python
from machine import UART
import utime

uart = UART(0, baudrate=115200)

while True:
    utime.sleep_ms(2000)
    uart.write('Hello\n')
