try:
    from googlesearch import search
except ImportError:
    print("No module named google found")

def google(querry):
    for j in search(querry, tld="co.in", num=1, stop=1, pause=2):
        return j




