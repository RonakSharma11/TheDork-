from re import search
import requests
import time
import googlesearch
import tkinter as tk
from tkinter import messagebox, scrolledtext
import json


def load_queries(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def search_dorks(query, num_results=10):
    urls = []
    for url in search(query, num_results=num_results):
        urls.append(url)
        time.sleep(5)  # Delay to avoid hitting rate limits
    return urls


def perform_search():
    target_site = entry_target.get()
    category = category_var.get()

    if not target_site or not category:
        messagebox.showerror("Input Error", "Please enter a website and select a category.")
        return

    site_query_prefix = f"site:{target_site} "

    # Load queries from the JSON file
    queries = load_queries("queries.json")

    result_text.delete(1.0, tk.END)  # Clear previous results
    loading_window()  # Show loading screen

    for query in queries[category]:
        formatted_query = query.replace("{target_site}", target_site)
        result_text.insert(tk.END, formatted_query + "\n")

        urls = search_dorks(formatted_query)

        for url in urls:
            result_text.insert(tk.END, url + "\n")

    loading_window.destroy()  # Close loading screen


def loading_window():
    global load_win
    load_win = tk.Toplevel(root)
    load_win.title("Loading...")
    load_win.geometry("300x100")
    load_win.configure(bg='black')

    label_loading = tk.Label(load_win, text="Searching...", bg='black', fg='gold', font=("Helvetica", 16))
    label_loading.pack(expand=True)


# GUI Setup
root = tk.Tk()
root.title("Google Dork Search Tool")
root.configure(bg='black')

frame = tk.Frame(root, bg='black')
frame.pack(padx=10, pady=10)

label_target = tk.Label(frame, text="Enter the website (e.g., example.com):", bg='black', fg='gold')
label_target.pack()

entry_target = tk.Entry(frame, width=50)
entry_target.pack()

label_category = tk.Label(frame, text="Select a category:", bg='black', fg='gold')
label_category.pack()

category_var = tk.StringVar(value="")
categories = ["Sensitive Files and Directories", "Vulnerable Servers", "Error Messages",
              "Sensitive Information", "Network or Vulnerability Data", "Miscellaneous"]
for index, category in enumerate(categories, start=1):
    rb = tk.Radiobutton(frame, text=category, variable=category_var, value=str(index), bg='black', fg='gold',
                        selectcolor='black')
    rb.pack(anchor=tk.W)

search_button = tk.Button(frame, text="Search", command=perform_search, bg='gold', fg='black')
search_button.pack(pady=5)

result_text = scrolledtext.ScrolledText(root, width=80, height=20, bg='black', fg='gold')
result_text.pack(padx=10, pady=10)

root.mainloop()