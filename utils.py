import subprocess

class get_windows:
    def __init__(self):
        pass

    def activate(self, window_title: str) -> None:
        try:
            # Get the list of all windows
            windows = self.find_all_windows_string(window_title)

            for window in self.get_all_window_titles_and_ids(windows):
                print(window)
                
                if window_title.lower() in window["title"].lower():
                
                    print(f"found it: { window["title"]}")
                    # Activate the window
                    subprocess.run(['wmctrl', '-i', '-a', window["id"]], check=True)
                    # break

            print(f"Window '{window_title}' not found")
            
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")


    def find_all_windows_string(self, window_title: str) -> list:
        output = subprocess.check_output(['wmctrl', '-l'])
        windows = output.decode().strip().split('\n')
        return windows


    def get_all_window_titles_and_ids(self, windows) -> list:
        output = []
        proc = subprocess.run("hostname", stdout=subprocess.PIPE)
        host_name = proc.stdout.decode()

        for window in windows:
            parts = window.split(None, 4)
            parts = window.split(host_name, 4)
            for part in parts:
                id = part[0:10]
                title = part[14 + len(host_name): len(window)]
                output.append({"title" : title, "id": id})
        return output

#for testing purposes
if __name__ == "__main__":
    obj = get_windows()
    obj.activate("godot")