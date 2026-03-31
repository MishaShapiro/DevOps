import os
import sys
import json
import subprocess

BASE_DIR = "/var/lib/mycontainer"
BASE_ROOTFS = os.path.join(BASE_DIR, "base")


def load_config(path):
    with open(path) as f:
        return json.load(f)


def create_dirs(container_id):
    root = os.path.join(BASE_DIR, container_id)

    os.makedirs(os.path.join(root, "upper"), exist_ok=True)
    os.makedirs(os.path.join(root, "work"), exist_ok=True)
    os.makedirs(os.path.join(root, "merged"), exist_ok=True)

    return root


def mount_overlay(container_root):
    merged = os.path.join(container_root, "merged")

    cmd = [
        "mount", "-t", "overlay", "overlay",
        "-o",
        f"lowerdir={BASE_ROOTFS},"
        f"upperdir={container_root}/upper,"
        f"workdir={container_root}/work",
        merged
    ]

    subprocess.run(cmd, check=True)


def run_container(container_root, config):
    merged = os.path.join(container_root, "merged")
    hostname = config.get("hostname", "container")
    args = config["process"]["args"]

    cmd = [
        "unshare",
        "--fork",
        "--pid",
        "--mount",
        "--uts",
        "python3",
        __file__,
        "child",
        merged,
        hostname
    ] + args

    subprocess.run(cmd, check=True)


def child_process():
    merged = sys.argv[2]
    hostname = sys.argv[3]
    cmd = sys.argv[4:]

    subprocess.run(["hostname", hostname], check=True)

    os.chroot(merged)
    os.chdir("/")

    os.makedirs("/proc", exist_ok=True)
    subprocess.run(["mount", "-t", "proc", "proc", "/proc"], check=True)

    os.execvp(cmd[0], cmd)


def main():
    if os.geteuid() != 0:
        print("Run as root")
        sys.exit(1)

    if len(sys.argv) < 3:
        print("Usage: main.py <id> <config.json>")
        sys.exit(1)

    container_id = sys.argv[1]
    config_path = sys.argv[2]

    config = load_config(config_path)

    container_root = create_dirs(container_id)
    mount_overlay(container_root)
    run_container(container_root, config)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "child":
        child_process()
    else:
        main()
