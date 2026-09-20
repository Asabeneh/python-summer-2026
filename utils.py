
def change_text2words(filename):
    """Reads a text file, strips basic punctuation, and extracts all words.

    Args:
        filename (str): The path to the text file that needs to be processed.

    Returns:
        list of str: A flat list containing all the lowercased words from 
        the file in their original order.

    Examples:
        If 'sample.txt' contains: "Hello, world. Hello again."
        >>> change_text2words('sample.txt')
        ['hello', 'world', 'hello', 'again']
    """
    f = open(filename, 'r', encoding='utf-8')
    lines = f.read().splitlines()
    lst = []
    for line in lines:
        words = line.replace('.', '').replace(',', '').replace(',', '').replace('’', '').replace('"', '').replace(':', '').replace('-','').lower().split()
        lst.extend(words)
    f.close()
    return lst




def freq_table(lst, n = None):
    """Calculates the frequency of elements in a list and returns them sorted by count.

    Args:
        lst (list): A list of items (e.g., strings, numbers) to count.
        n (int, optional): The number of top frequent elements to return. 
            Defaults to None, which returns all elements.

    Returns:
        list of tuples: A list of `(item, frequency)` tuples, sorted in descending 
        order by their frequency.

    Examples:
        >>> freq_table(['apple', 'banana', 'apple', 'cherry'], n=2)
        [('apple', 2), ('banana', 1)]
    """
    dct = {}
    for word in lst:
        if word in dct:
            dct[word] = dct[word] + 1
        else:
            dct[word] = 1
    items = dct.items()
    sorted_items = sorted(items, key = lambda item:item[1], reverse=True)
    if n:
        return sorted_items[0:n]
    return sorted_items


def format_time():
    """Fetches the current local time and formats it as a readable string.

    Returns:
        str: The current date and time formatted like '20 September 2026 20:46:15'.

    Note:
        This function utilizes the country-specific platform flag format (`%#d`) 
        to strip leading zeros from the day number on Windows systems. On Linux/macOS 
        environments, this may require changing `%#d` to `%-d` to avoid a ValueError.
    """
    from datetime import datetime
    now = datetime.now()
    t = now.strftime("%#d %B %Y %H:%M:%S")
    return t

    
