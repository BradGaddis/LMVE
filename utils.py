import subprocess

def activate_window(window_title):
    try:
        # Get the list of all windows
        output = subprocess.check_output(['wmctrl', '-l'])
        windows = output.decode().strip().split('\n')

        for window in windows:
            parts = window.split(None, 4)
            if len(parts) == 5:
                window_id, _, _, _, title = parts
    
                if window_title.lower() in title.lower():
                    # Activate the window
                    subprocess.run(['wmctrl', '-i', '-a', window_id], check=True)
                    break

        print("Window not found")
        
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")