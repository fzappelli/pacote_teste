from datetime import datetime, timedelta

def get_current_date():
    """
    Retorna a data e hora atuais usando datetime.now().
    """
    return datetime.now()

def format_date(date, fmt="%Y-%m-%d"):
    """
    Formata um objeto datetime de acordo com o formato especificado (padrão: YYYY-MM-DD). O formato pode ser alterado conforme necessário (por exemplo, "%d/%m/%Y" para o formato brasileiro).
    """
    return date.strftime(fmt)

def parse_date(date_str, fmt="%Y-%m-%d"):
    """
    Converte uma string de data em um objeto datetime com base no formato especificado. Isso é útil para converter datas de arquivos ou entradas de usuários
    """
    return datetime.strptime(date_str, fmt)

def days_between(d1, d2):
    """
    Retorna a diferença em dias entre duas datas d1 e d2. A função usa a operação de subtração entre objetos datetime.
    """
    return abs((d2 - d1).days)

def add_days_to_date(date, days):
    """
    Adiciona um número de dias à data fornecida, retornando a nova data. Usa timedelta para fazer a adição.
    """
    return date + timedelta(days=days)

def is_weekend(date):
    """
    Verifica se uma data cai no fim de semana (sábado ou domingo). A função usa weekday() que retorna um número de 0 (segunda-feira) a 6 (domingo).
    """
    return date.weekday() >= 5

def is_weekday(date):
    """
    Similar à anterior, verifica se a data está entre segunda e sexta-feira.
    """
    return date.weekday() < 5

def get_first_day_of_month(date):
    """
    Retorna o primeiro dia do mês da data fornecida, usando replace(day=1) para modificar o dia da data.
    """
    return date.replace(day=1)

def get_last_day_of_month(date):
    """
    Calcula o último dia do mês de maneira segura, lidando com a variação de meses com 28, 30 ou 31 dias. Faz isso ao avançar até o próximo mês e depois voltar para o último dia do mês atual.
    """
    next_month = date.replace(day=28) + timedelta(days=4)  # Garante que estamos no mês seguinte
    return next_month - timedelta(days=next_month.day)