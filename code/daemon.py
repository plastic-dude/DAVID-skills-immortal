#!/usr/bin/env python3
"""
DAVID Agent Immortal Daemon v2.0
Runs continuously, discovers skills, maintains state.
"""
import os, sys, time, json, subprocess

WORKSPACE = "/mnt/kimi-persist/david-agent"
STATE_DIR = f"{WORKSPACE}/state"
SKILLS_DIR = f"{WORKSPACE}/skills"
LOG_FILE = f"{WORKSPACE}/daemon.log"

def log(msg):
    line = f"[{time.ctime()}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

def daemonize():
    pid = os.fork()
    if pid > 0:
        sys.exit(0)
    os.setsid()
    pid = os.fork()
    if pid > 0:
        sys.exit(0)
    os.umask(0)
    os.chdir(WORKSPACE)

def count_skills():
    total = 0
    categories = {}
    if os.path.exists(SKILLS_DIR):
        for cat in os.listdir(SKILLS_DIR):
            cat_path = os.path.join(SKILLS_DIR, cat)
            if os.path.isdir(cat_path):
                count = len([f for f in os.listdir(cat_path) if os.path.isfile(os.path.join(cat_path, f))])
                categories[cat] = count
                total += count
    return total, categories

def save_state(total, categories):
    state = {
        "timestamp": time.time(),
        "total_skills": total,
        "categories": categories,
        "pod": os.uname().nodename,
        "daemon_pid": os.getpid(),
    }
    os.makedirs(STATE_DIR, exist_ok=True)
    with open(os.path.join(STATE_DIR, "daemon.json"), "w") as f:
        json.dump(state, f, indent=2)

def main():
    daemonize()
    log(f"Daemon started: PID {os.getpid()}")

    cycle = 0
    while True:
        cycle += 1
        total, categories = count_skills()
        save_state(total, categories)
        log(f"Cycle {cycle}: {total} skills across {len(categories)} categories")
        time.sleep(300)  # 5 minutes

if __name__ == "__main__":
    main()
