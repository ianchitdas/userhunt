import requests
import time
import os
from pyfiglet import Figlet

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

SITES = {
    "GitHub":        "https://github.com/{}",
    "GitLab":        "https://gitlab.com/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "CodePen":       "https://codepen.io/{}",
    "Reddit":        "https://www.reddit.com/user/{}",
    "Twitter":       "https://twitter.com/{}",
    "Instagram":     "https://www.instagram.com/{}/",
    "Facebook":      "https://www.facebook.com/{}",
    "TikTok":        "https://www.tiktok.com/@{}",
    "Medium":        "https://medium.com/@{}",
    "Dev.to":        "https://dev.to/{}",
    "WordPress":     "https://{}.wordpress.com",
    "Hashnode":      "https://hashnode.com/@{}",
    "Pinterest":     "https://www.pinterest.com/{}/",
    "VK":            "https://vk.com/{}",
    "YouTube":       "https://www.youtube.com/{}",
    "Vimeo":         "https://vimeo.com/{}",
    "Behance":       "https://www.behance.net/{}",
    "Dribbble":      "https://dribbble.com/{}",
    "LinkedIn":      "https://www.linkedin.com/in/{}",
    "ProductHunt":   "https://www.producthunt.com/@{}",
    "Steam":         "https://steamcommunity.com/id/{}",
    "9GAG":          "https://9gag.com/u/{}",
    "Disqus":        "https://disqus.com/by/{}/",
    "HackerNews":    "https://news.ycombinator.com/user?id={}",
    "Quora":         "https://www.quora.com/profile/{}",
    "Replit":        "https://replit.com/@{}",
    "SoundCloud":    "https://soundcloud.com/{}",
    "Bandcamp":      "https://{}.bandcamp.com",
    "About.me":      "https://about.me/{}",
    "Keybase":       "https://keybase.io/{}",
    "Fandom":        "https://community.fandom.com/wiki/User:{}"
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_banner():
    f = Figlet(font='slant')
    print(f.renderText('UserHunt'))
    print("Author: Anchit D")

def check_username(username):
    print(f"\n🔍 Searching for username: {username}\n")
    found = []

    for site, url in SITES.items():
        full_url = url.format(username)
        try:
            res = requests.get(full_url, headers=HEADERS, timeout=10)
            if res.status_code == 200:
                print(f"✅ Found on {site:<14}: {full_url}")
                found.append((site, full_url))
            elif res.status_code == 404:
                print(f"❌ Not found on {site:<14}")
            else:
                print(f"⚠️  Unknown response from {site:<14} (status {res.status_code})")
        except Exception as e:
            print(f"❌ Error checking {site:<14}: {e}")
        time.sleep(0.5)

    print(f"\n🎯 Scan complete. Found on {len(found)} site(s).\n")

def about():
    print("""
📌 About UserHunt
-----------------------------
UserHunt is an Open Source Intelligence (OSINT) tool to scan for a given username across 30+ major websites including:
- Developer platforms (GitHub, GitLab, StackOverflow)
- Social media (Twitter, Instagram, TikTok)
- Blogging and creative platforms
- Forums and more

🛠️  Built with ❤️ for ethical research, cybersecurity, and awareness.

Author: Anchit
License: MIT
GitHub: https://github.com/ianchitdas/userhunt
""")

def main():
    clear()
    show_banner()
    print("Welcome to UserHunt 🕵️‍♂️\n")

    while True:
        print("1️⃣  Search for a username")
        print("2️⃣  About this tool")
        print("3️⃣  Exit\n")

        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            username = input("Enter the username to search: ").strip()
            clear()
            show_banner()
            check_username(username)
        elif choice == '2':
            clear()
            show_banner()
            about()
        elif choice == '3':
            print("👋 Exiting. Stay ethical.")
            break
        else:
            print("❌ Invalid input. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
