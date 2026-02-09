# 🖱️ Course Registration Auto-Clicker

> **Disclaimer:** Use this tool at your own risk. Please ensure that your university's registration system policies allow the use of automation tools.

### 🎯 The Mission: Survive Slow University Systems

Sometimes university course registration systems are… **not great.** Slow servers, random errors, and endless clicking can make the process a nightmare.

I built this small Python auto-clicker to handle the repetitive stress of clicking while I focus on more important things (like not losing my sanity). 

**This script repeatedly:**
* ✅ Clicks the **Confirm** button
* ⏳ Waits for the popup
* ✅ Clicks **OK**
* ✅ Handles additional warning/confirmation buttons
* 🔄 Repeats until success!

*Simple. Effective. Slightly therapeutic.*

---

## 🛠️ Requirements

- **Python 3.x**
- **pyautogui** library

**Install dependency:**
```
pip install pyautogui
```
## 🚀 How to Use
- **Setup** : Open the registration website and keep it in fullscreen.

- **Locate**: Find your button coordinates using this Python command:

import pyautogui
print(pyautogui.position())

Configure: Put the coordinates into the script:

confirm_button = (x, y)
ok_button = (x, y)
extra_button = (x, y)
Run: ```python auto-clicker.py```

*Tip: Move your mouse to the **top-left corner** anytime to trigger the emergency stop.*

## 🔐 Safety Features
pyautogui.FAILSAFE = True

If something goes wrong, moving the mouse to the extreme top-left corner of your screen instantly kills the script.

## **!IMPORTANT!**

 Coordinates depend on screen resolution and scaling.

 Keep browser size and zoom unchanged while running.

 This tool does NOT bypass authentication or system rules — it only automates manual clicking.

## 💡 Why I Built This
Because sometimes engineering is not about building massive systems, but about making annoying problems disappear.

## NOTES
- **Do not forget** update the coordinates for your page
- **Why the 13-second delay?** The university server experiences extreme latency and 503 Service Unavailable errors during peak registration hours. A shorter delay would overwhelm the struggling server, while 13 seconds provides a "buffer zone" for the system to process the request and render the next popup. It’s a deliberate strategy to stay below the server's crash threshold.

## 📄 License
MIT — Feel free to use, modify, and improve it.
