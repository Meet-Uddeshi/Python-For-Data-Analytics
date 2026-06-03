import sys
import os
import subprocess

if __name__ == "__main__":
    # The actual app.py is located in the projects directory
    actual_app_path = os.path.join(os.path.dirname(__file__), "projects", "Instagram.analysis", "src", "app.py")
    
    if os.path.exists(actual_app_path):
        print(f"Running {actual_app_path}...")
        # Run the actual script
        subprocess.run([sys.executable, actual_app_path])
    else:
        print(f"Could not find the script at: {actual_app_path}")

