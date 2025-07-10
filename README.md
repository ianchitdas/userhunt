# UserHunt 🔍

UserHunt is a lightweight, open-source OSINT (Open Source Intelligence) CLI tool that allows you to check if a username exists on 30+ popular websites. It's designed for ethical research, cybersecurity investigations, and digital footprint awareness.

## Features
- 🔎 Search for a username across 30+ major platforms (social, developer, creative, forums, etc.)
- ⚡ Fast and simple command-line interface
- 📝 Clear output showing where the username is found
- 🛠️ Built with Python, no browser automation required

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourname/userhunt.git
   cd userhunt
   ```
2. **Install dependencies and the CLI tool:**
   ```bash
   pip install -e .
   ```
   This will install all required Python packages and make the `userhunt` command available globally.

## Usage

### Run from anywhere:
```bash
userhunt
```

### Or, run directly with Python (if not installed as CLI):
```bash
python -m userhunt
```

You will see an interactive menu:

```
 __  __               __  __            __
/ / / /_______  _____/ / / /_  ______  / /_
/ / / / ___/ _ \/ ___/ /_/ / / / / __ \/ __/
/ /_/ (__  )  __/ /  / __  / /_/ / / / / /_
\____/____/\___/_/  /_/ /_/\__,_/_/ /_/\__/

Welcome to UserHunt 🕵️‍♂️

1️⃣  Search for a username
2️⃣  About this tool
3️⃣  Exit
```

Follow the prompts to search for a username or learn more about the tool.

## Example
```
$ userhunt

Welcome to UserHunt 🕵️‍♂️

1️⃣  Search for a username
2️⃣  About this tool
3️⃣  Exit

Choose an option (1-3): 1
Enter the username to search: johndoe

🔍 Searching for username: johndoe
✅ Found on GitHub        : https://github.com/johndoe
❌ Not found on Twitter   
... (output continues)

🎯 Scan complete. Found on X site(s).
```

## Requirements
- Python 3.6+
- `requests` and `pyfiglet` (installed automatically with pip)

## License
MIT

## Author
Anchit D
