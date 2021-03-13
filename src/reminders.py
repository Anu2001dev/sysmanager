import asyncio
import os
import subprocess
from datetime import datetime, timedelta

# cd to project root or set app dir env var
PROJECT_ROOT = os.getenv("APPDIR") or os.getcwd()


def round_time(round_to) -> float:
    return ((datetime.min - datetime.now()) % timedelta(minutes=round_to)).seconds


async def notify(
    title: str, body: str = "", icon: str = "", interval: float = 0
):
    count = 0
    while True:
        subprocess.Popen(["notify-send", title, body, "-i", f"{PROJECT_ROOT}/icons/{icon}"])
        remaining_secs = interval * 60 if count > 0 else round_time(interval)
        await asyncio.sleep(remaining_secs)
        count += 1


async def main():
    notifications = [
        ("Drink Water 🍉", "water.png", 30),
        ("Correct Your Posture 🧘", "posture.jpg", 45),
    ]
    notifiers = [
        notify(title, icon=icon, interval=interval)
        for title, icon, interval in notifications
    ]
    await asyncio.gather(*notifiers)        


if __name__ == "__main__":
    asyncio.run(main())
