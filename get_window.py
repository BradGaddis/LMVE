import subprocess

class get_windows:
    def __init__(self):
        self.open_windows = self.find_all_windows_string()

    def get_windows_by_title(self, title):
        output = []
        for item in self.get_all_window_titles_and_ids(self.open_windows):
            if title.lower() in item["title"].lower():
                win_class = window(title=item["title"], id=item["id"])
                output.append(win_class)
        return output

    def find_all_windows_string(self) -> list:
        
        """
        returns a list of the full string of each window that is open, unparsed
        """
        
        output = subprocess.check_output(['wmctrl', '-l'])
        windows = output.decode().strip().split('\n')
        return windows

    def get_all_window_titles_and_ids(self, windows) -> list:
        
        """
        returns a list of dicts of all open window titles and ids
        """

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

class window:
    def __init__(self, title, id):
        self.title = title
        self.id = id

    def __repr__(self):
        return self.title

    def activate(self) -> None:
        """
        brings this window to the foreground
        """
        try:
            subprocess.run(['wmctrl', '-i', '-a', self.id], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    def close(self) -> None:
        try:
            subprocess.run(['wmctrl', '-i', '-c', self.id], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

