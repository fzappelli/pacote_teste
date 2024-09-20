def to_upper(s):
    return s.upper()

def capitalize_first_letter(s):

    return s.title()

def strip_spaces(s):
    """
    Usa o método strip() para remover espaços no início e no final da string.
    """
    return s.strip()

def is_palindrome(s):
    """
    Remove caracteres não alfanuméricos e transforma a string em minúsculas antes de verificar se é um palíndromo (lê-se da mesma forma de trás para frente).
    """
    cleaned = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned == cleaned[::-1]

def count_occurrences(s, substring):
    """
    Usa o método count() para contar quantas vezes a substring aparece na string principal.
    """
    return s.count(substring)

def replace_substring(s, old, new):
    """
    Usa o método replace() para substituir todas as ocorrências de old por new
    """
    return s.replace(old, new)

def reverse_string(s):
    """
    Usa a notação de slicing para inverter a string.
    """
    return s[::-1]