import requests
import random
import time
from googlesearch import search


def search_dorks(query, num_results=10):
    urls = []
    for url in search(query, num_results=num_results):
        urls.append(url)
        # Add a delay of 5 seconds between requests to avoid hitting rate limits
        time.sleep(5)
    return urls

def main():
    print("Google Dork Queries for Penetration Testing")
    print("-------------------------------------------")

    # Ask the user for the website to search
    target_site = input("Enter the website you want to search (e.g., example.com): ")

    print("\nSelect a category of Google dorks to perform:")
    print("1. Sensitive Files and Directories")
    print("2. Vulnerable Servers")
    print("3. Error Messages")
    print("4. Sensitive Information")
    print("5. Vulnerable Web Applications")
    print("6. Miscellaneous")

    category = input("Enter the number (1-6) of the category: ")

    # Prefix to be added before each query
    site_query_prefix = f"site:{target_site} "

    if category == "1":
        print("\n## Sensitive Files and Directories")
        sensitive_queries = [
            f"{site_query_prefix}intitle: index of /concrete/Password",
            f"{site_query_prefix}intext:'userfiles'intitle:'Index Of'",
            f"{site_query_prefix}intitle:'index of'''main.yml",
            f"{site_query_prefix}inurl:ssh intitle:index of /files",
        ]
        for query in sensitive_queries:
            print(f"\n{query}")
            urls = search_dorks(query)
            for url in urls:
                print(url)

    elif category == "2":
        print("\n## Vulnerable Servers")
        vuln_server_queries = [
            f"{site_query_prefix}\"powered by phpMyAdmin\"",
            f"{site_query_prefix}\"powered by IIS\"",
            f"{site_query_prefix}\"powered by Apache\"",
            f"{site_query_prefix}\"powered by Tomcat\""
        ]
        for query in vuln_server_queries:
            print(f"\n{query}")
            urls = search_dorks(query)
            for url in urls:
                print(url)

    elif category == "3":
        print("\n## Error Messages")
        error_queries = [
            f"{site_query_prefix}\"Warning: Cannot modify header information\"",
            f"{site_query_prefix}\"SQL syntax near\"",
            f"{site_query_prefix}\"Uncaught exception\""
        ]
        for query in error_queries:
            print(f"\n{query}")
            urls = search_dorks(query)
            for url in urls:
                print(url)

    elif category == "4":
        print("\n## Sensitive Information")
        sensitive_info_queries = [
            f"{site_query_prefix}\"username\" \"password\" \"login\"",
            f"{site_query_prefix}\"email\" \"password\" \"login\"",
            f"{site_query_prefix}\"userid\" \"password\" \"login\""
        ]
        for query in sensitive_info_queries:
            print(f"\n{query}")
            urls = search_dorks(query)
            for url in urls:
                print(url)

    elif category == "5":
        print("\n## Vulnerable Web Applications")
        vuln_app_queries = [
            f"{site_query_prefix}\"powered by Joomla\" inurl:com_",
            f"{site_query_prefix}\"powered by WordPress\" inurl:wp-content",
            f"{site_query_prefix}\"powered by Drupal\" inurl:modules"
        ]
        for query in vuln_app_queries:
            print(f"\n{query}")
            urls = search_dorks(query)
            for url in urls:
                print(url)

    elif category == "6":
        print("\n## Miscellaneous")
        misc_queries = [
            f"{site_query_prefix}\"site:{target_site}\"",
            f"{site_query_prefix}\"inurl:{target_site}\"",
            f"{site_query_prefix}\"intitle:{target_site}\"",
            f"{site_query_prefix}\"cache:{target_site}\""
        ]
        for query in misc_queries:
            print(f"\n{query}")
            urls = search_dorks(query)
            for url in urls:
                print(url)

    else:
        print("Invalid category number. Please try again.")

if __name__ == "__main__":
    main()