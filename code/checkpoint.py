#!/usr/bin/env python3
"""
DAVID Agent Checkpoint System v1.0
Auto-saves state after every action. Auto-recovers on new session.
"""
import os, sys, json, time

CHECKPOINT_DIR = "/mnt/kimi-persist/david-agent/state"
os.makedirs(CHECKPOINT_DIR, exist_ok=True)

def save_checkpoint(data, name="latest"):
    path = os.path.join(CHECKPOINT_DIR, f"{name}.json")
    data["_timestamp"] = time.time()
    data["_pod"] = os.uname().nodename
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path

def load_checkpoint(name="latest"):
    path = os.path.join(CHECKPOINT_DIR, f"{name}.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None

def get_last_session_state():
    return load_checkpoint("session")

def save_session_state(context):
    return save_checkpoint(context, "session")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        cp = load_checkpoint()
        if cp:
            print(f"Checkpoint: {cp.get('_timestamp', 'unknown')}")
            print(f"Pod: {cp.get('_pod', 'unknown')}")
        else:
            print("No checkpoint found")
