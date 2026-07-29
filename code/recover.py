#!/usr/bin/env python3
"""
DAVID Agent Auto-Recovery
Run at start of every session to restore state.
"""
import os, sys, json, time

STATE_DIR = "/mnt/kimi-persist/david-agent/state"
SKILLS_DIR = "/mnt/kimi-persist/david-agent/skills"

def recover():
    print("=" * 60)
    print("DAVID AGENT AUTO-RECOVERY")
    print("=" * 60)

    # Load session state
    session_path = os.path.join(STATE_DIR, "session.json")
    if os.path.exists(session_path):
        with open(session_path) as f:
            state = json.load(f)
        print(f"\n[✓] Session state recovered")
        print(f"    Last active: {time.ctime(state.get('_timestamp', 0))}")
        print(f"    Last pod: {state.get('_pod', 'unknown')}")
    else:
        print(f"\n[!] No previous session state found")

    # Count skills
    total = 0
    if os.path.exists(SKILLS_DIR):
        for root, dirs, files in os.walk(SKILLS_DIR):
            total += len([f for f in files if f.endswith('.md')])
    print(f"\n[✓] Skills available: {total}")

    # Check daemon
    daemon_running = False
    try:
        import psutil
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if proc.info['cmdline'] and 'immortal_daemon' in str(proc.info['cmdline']):
                daemon_running = True
                print(f"\n[✓] Daemon running: PID {proc.info['pid']}")
                break
    except:
        pass

    if not daemon_running:
        print(f"\n[!] Daemon not running. Start with:")
        print(f"    python3 /mnt/kimi-persist/david-agent/code/daemon.py")

    print(f"\n{'='*60}")
    print("RECOVERY COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    recover()
