import asyncio
import subprocess
from datetime import datetime, timedelta


def round_time(round_to) -> float:
    round_to = round_to * 60  # convert seconds to minutes
    now = datetime.now()
    secs = (now.replace(tzinfo=None) - now.min).seconds
    rounding = (secs + round_to / 2) // round_to * round_to
    target = now + timedelta(0, rounding - secs, -now.microsecond)
    remaining_time = target - now
    return remaining_time.seconds


async def notify(title: str, body: str = "", icon: str = "", interval: float = 0):
    cmd = ["notify-send", title, body, "-i", f"../icons/{icon}"]
    subprocess.Popen(cmd)

    remaining_secs = round_time(interval)
    await asyncio.sleep(remaining_secs)


async def main():
    notifications = [
        ("Drink Water 🍉", "water.png", 30),
        ("Correct Your Posture 🧘", "posture.png", 45),
    ]
    while True:
        notifiers = [
            notify(title, icon=icon, interval=interval)
            for title, icon, interval in notifications
        ]
        await asyncio.gather(*notifiers)


if __name__ == "__main__":
    asyncio.run(main())
