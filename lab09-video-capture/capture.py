import logging
import subprocess

from datetime import datetime
from pathlib import Path


RECORDINGS = Path("recordings")
LOGS = Path("logs")

RECORDINGS.mkdir(exist_ok=True)
LOGS.mkdir(exist_ok=True)


logging.basicConfig(
    filename=LOGS / "capture.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def start_capture(stream_url):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_file = RECORDINGS / f"capture_{timestamp}.mp4"

    logging.info("Starting capture: %s", output_file)

    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel", "warning",
        "-i", stream_url,
        "-c", "copy",
        "-movflags", "+faststart",
        str(output_file)
    ]

    process = subprocess.Popen(command)

    print(f"Recording started: {output_file}")
    print("Press ENTER to stop recording.")

    input()

    logging.info("Stopping capture")

    process.terminate()
    process.wait()

    logging.info("Capture completed: %s", output_file)

    print(f"Recording saved: {output_file}")


if __name__ == "__main__":

    url = input("Enter authorized video stream URL: ").strip()

    if not url:
        print("No stream URL supplied.")
        raise SystemExit(1)

    start_capture(url)
