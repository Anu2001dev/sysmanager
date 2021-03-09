import asyncio
import os
import subprocess
from datetime import datetime, timedelta

# cd to project root or set app dir env var
PROJECT_ROOT = os.getenv("APPDIR") or os.getcwd()


def round_time(round_to) -> float:
    return ((datetime.min - datetime.now()) % timedelta(minutes=round_to)).seconds


async def notify(
    title: str, count: int, body: str = "", icon: str = "", interval: float = 0
):
    cmd = ["notify-send", title, body, "-i", f"{PROJECT_ROOT}/icons/{icon}"]
    subprocess.Popen(cmd)
    remaining_secs = interval * 60 if count > 0 else round_time(interval)
    await asyncio.sleep(remaining_secs)


async def main():
    notifications = [
        ("Drink Water 🍉", "water.png", 30),
        ("Correct Your Posture 🧘", "posture.jpg", 45),
    ]
    count = 0
    while True:
        notifiers = [
            notify(title, count, icon=icon, interval=interval)
            for title, icon, interval in notifications
        ]
        await asyncio.gather(*notifiers)
        count += 1


if __name__ == "__main__":
    asyncio.run(main())
