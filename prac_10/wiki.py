import wikipedia

def get_wikipedia_summary():
    while True:
        search_query = input("Enter a Wikipedia search term (or leave blank to exit): ")
        if not search_query:
            break

        try:
            # Attempt to get the page. Set autosuggest to False to avoid automatic suggestions.
            wiki_page = wikipedia.page(search_query, auto_suggest=False)
            print("Title:", wiki_page.title)
            print("Summary:", wiki_page.summary)
            print("URL:", wiki_page.url)
        except wikipedia.DisambiguationError as e:
            print("Disambiguation error. Please be more specific or choose one of the following options:")
            for option in e.options:
                print(option)
        except wikipedia.PageError:
            print("Page not found. Please try a different search term.")
        except Exception as e:
            print("An error occurred: {}".format(e))

# Run the script
if __name__ == "__main__":
    get_wikipedia_summary()