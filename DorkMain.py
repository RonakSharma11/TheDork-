import requests
import time
from googlesearch import search
import tkinter as tk
from tkinter import messagebox, scrolledtext


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

    queries = {
        "1": [
            f"{site_query_prefix}intitle: index of /concrete/Password",
            f"{site_query_prefix}intext:'userfiles'intitle:'Index Of'",
            f"{site_query_prefix}intitle:'index of'''main.yml",
            f"{site_query_prefix}inurl:ssh intitle:index of /files",
        ],
        "2": [
            f"{site_query_prefix}\"powered by phpMyAdmin\"",
            f"{site_query_prefix}\"powered by IIS\"",
            f"{site_query_prefix}\"powered by Apache\"",
            f"{site_query_prefix}\"powered by Tomcat\""
        ],
        "3": [
            f"{site_query_prefix}\"Warning: Cannot modify header information\"",
            f"{site_query_prefix}\"SQL syntax near\"",
            f"{site_query_prefix}\"Uncaught exception\""
        ],
        "4": [
            f"{site_query_prefix}\"username\" \"password\" \"login\"",
            f"{site_query_prefix}\"email\" \"password\" \"login\"",
            f"{site_query_prefix}\"userid\" \"password\" \"login\""
        ],
        "5": [
            f"{site_query_prefix}\"powered by Joomla\" inurl:com_",
            f"{site_query_prefix}\"powered by WordPress\" inurl:wp-content",
            f"{site_query_prefix}\"powered by Drupal\" inurl:modules"
        ],
        "6": [
            f"{site_query_prefix}\"site:{target_site}\"",
            f"{site_query_prefix}\"inurl:{target_site}\"",
            f"{site_query_prefix}\"intitle:{target_site}\"",
            f"{site_query_prefix}\"cache:{target_site}\""
        ]
    }

    result_text.delete(1.0, tk.END)  # Clear previous results
    loading_screen()  # Show loading screen

    for query in queries[category]:
        result_text.insert(tk.END, query + "\n")
        urls = search_dorks(query)
        for url in urls:
            result_text.insert(tk.END, url + "\n")

    loading_window.destroy()  # Close loading screen


def loading_screen():
    global loading_window
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading...")
    loading_window.geometry("300x100")
    loading_window.configure(bg='black')

    label_loading = tk.Label(loading_window, text="Searching...", bg='black', fg='gold', font=("Helvetica", 16))
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
              "Sensitive Information", "Vulnerable Web Applications", "Miscellaneous"]
for index, category in enumerate(categories, start=1):
    rb = tk.Radiobutton(frame, text=category, variable=category_var, value=str(index), bg='black', fg='gold',
                        selectcolor='black')
    rb.pack(anchor=tk.W)

search_button = tk.Button(frame, text="Search", command=perform_search, bg='gold', fg='black')
search_button.pack(pady=5)

result_text = scrolledtext.ScrolledText(root, width=80, height=20, bg='black', fg='gold')
result_text.pack(padx=10, pady=10)

root.mainloop()