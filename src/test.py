import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and print its output."""
    print(f"\n>>> Running: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("STDOUT:")
        print(result.stdout)
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        return result
    except Exception as e:
        print(f"Error running command: {e}")
        return None

def diagnose_dvc_pipeline():
    # Check DVC version
    run_command("dvc --version")
    
    # Check git status
    run_command("git status")
    
    # Check DVC status
    run_command("dvc status")
    
    # Try reproducing the entire pipeline
    print("\nAttempting to reproduce entire pipeline:")
    run_command("dvc repro -v")

if __name__ == "__main__":
    diagnose_dvc_pipeline()