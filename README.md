# Platform-NXPS32K

PlatformIO platform for NXP S32K Automotive MCUs.

This platform provides the build system, CMSIS/device support, linker scripts, toolchain configuration and upload integration required to develop applications for the NXP S32K family using PlatformIO.

Currently supported:

- NXP S32K144
- J-Link upload
- Bare-metal framework
- EduFramework (Arduino-style educational framework)

---

# Features

- GCC ARM Embedded Toolchain
- CMSIS device support
- Startup code
- Linker scripts
- Intel HEX generation
- SEGGER J-Link upload
- PlatformIO integration
- GitHub hosted framework packages

---

# Supported Board

| Board           | MCU     | Status       |
| --------------- | ------- | ------------ |
| MaaZEDU S32K144 | S32K144 | ✅ Supported |

---

# Supported Frameworks

| Framework    | Description                                        |
| ------------ | -------------------------------------------------- |
| baremetal    | Low-level CMSIS startup, linker and device support |
| eduframework | Arduino-style educational framework for S32K144    |

---

# Installation

Create a PlatformIO project and use this platform inside `platformio.ini`.

## Bare-metal

```ini
[env:s32k144]
platform = https://github.com/QuangTM15/platform-nxps32k.git
board = s32k144
framework = baremetal
```

## EduFramework

```ini
[env:s32k144]
platform = https://github.com/QuangTM15/platform-nxps32k.git
board = s32k144
framework = eduframework
```

PlatformIO will automatically:

- Download the platform
- Download required framework packages
- Configure the ARM toolchain
- Build the application
- Generate the HEX image

---

# Build

```bash
pio run
```

---

# Upload

```bash
pio run -t upload
```

The firmware is uploaded using SEGGER J-Link over the SWD interface.

---

# Project Structure

```
platform-nxps32k/
│
├── boards/
├── builder/
│   ├── frameworks/
│   └── main.py
├── cmsis/
├── linker/
├── scripts/
├── platform.json
├── platform.py
└── README.md
```

---

# Repository

Platform:

https://github.com/QuangTM15/platform-nxps32k

EduFramework:

https://github.com/QuangTM15/s32k144-edu-framework

---

# License

MIT License
