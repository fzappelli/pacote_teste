def remove_duplicates(lst):
    """
    Remove elementos duplicados de uma lista mantendo a ordem original.
    """
    return list(dict.fromkeys(lst))

def flatten_list(nested_list):
    """
    Achata uma lista de listas (lista aninhada) em uma única lista.
    """
    return [item for sublist in nested_list for item in sublist]

def find_max(lst):
    """
    Retorna o maior valor de uma lista.
    """
    return max(lst) if lst else None

def find_min(lst):
    """
    Retorna o menor valor de uma lista.
    """
    return min(lst) if lst else None

def chunk_list(lst, chunk_size):
    """
    Divide uma lista em sublistas de tamanho fixo.
    """
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def sort_list(lst, reverse=False):
    """
    Ordena uma lista em ordem crescente ou decrescente (se reverse=True).
    """
    return sorted(lst, reverse=reverse)

def filter_even_numbers(lst):
    """
    Retorna apenas os números pares de uma lista.
    """
    return [num for num in lst if num % 2 == 0]

def filter_odd_numbers(lst):
    """
    Retorna apenas os números ímpares de uma lista.
    """
    return [num for num in lst if num % 2 != 0]

def get_unique_elements(lst):
    """
    Retorna uma lista de elementos únicos (sem repetição).
    """
    return list(set(lst))