import os
import pprint
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, scrolledtext

def get_file_metadata(filepath):
    """
    This function takes a file path as input and returns a dictionary
    containing the file's metadata,
    extracted using the OS module
    """
    if not os.path.exists(filepath):
        return {"error": f"File '{filepath}' does not exist."}
    
    stat_info = os.stat(filepath)

    metadata = { 
                "File Name": os.path.basename(filepath),
                "File Path": os.path.abspath(filepath),
                "File Extension": os.path.splitext(filepath)[1],
                "File Size (bytes)": stat_info.st_size,
                "Creation Time": datetime.fromtimestamp(stat_info.st_ctime).strftime("%Y-%m-%d %H:%M:%S"),
                "Last Modified Time": datetime.fromtimestamp(stat_info.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                "Last Accessed Time": datetime.fromtimestamp(stat_info.st_atime).strftime("%Y-%m-%d %H:%M:%S"),
                "Is Directory": os.path.isdir(filepath),
                "Is File": os.path.isfile(filepath),
                "Permissions (octal)": oct(stat_info.st_mode)[-3],
               }
    return metadata

def get_metadata_for_multiple_files(filepaths):
    """This function extracts metadata for a list of files, keyed by filename"""
    all_metadata = {}
    for path in filepaths:
        all_metadata[os.path.basename(path)] = get_file_metadata(path)
    return all_metadata

class ForensicsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Forensics - Metadata Extractor")
        self.root.geometry("700x500")

        select_btn = tk.Button(root, text="Select File(s)", command=self.select_files)
        select_btn.pack(pady=10)

        self.output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
        self.output_box.pack(padx=10, pady=10)

    def select_files(self):
        filepaths = filedialog.askopenfilenames(title="Select one or more files")
        if not filepaths:
            return

        all_metadata = get_metadata_for_multiple_files(filepaths)

        self.output_box.delete("1.0", tk.END)
        for filename, metadata in all_metadata.items():
            self.output_box.insert(tk.END, f"--- {filename} ---\n")
            self.output_box.insert(tk.END, pprint.pformat(metadata))
            self.output_box.insert(tk.END, "\n\n")

def main():
    root = tk.Tk()
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    app = ForensicsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    