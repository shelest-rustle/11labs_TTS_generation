import re


def number_to_words_spanish(number):
    """Convert a number to Spanish words."""
    
    # Словари для конвертации
    units = {
        0: '', 1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco',
        6: 'seis', 7: 'siete', 8: 'ocho', 9: 'nueve', 10: 'diez',
        11: 'once', 12: 'doce', 13: 'trece', 14: 'catorce', 15: 'quince',
        16: 'dieciséis', 17: 'diecisiete', 18: 'dieciocho', 19: 'diecinueve',
        20: 'veinte', 21: 'veintiuno', 22: 'veintidós', 23: 'veintitrés',
        24: 'veinticuatro', 25: 'veinticinco', 26: 'veintiséis',
        27: 'veintisiete', 28: 'veintiocho', 29: 'veintinueve'
    }
    
    tens = {
        3: 'treinta', 4: 'cuarenta', 5: 'cincuenta',
        6: 'sesenta', 7: 'setenta', 8: 'ochenta', 9: 'noventa'
    }
    
    hundreds = {
        1: 'ciento', 2: 'doscientos', 3: 'trescientos', 4: 'cuatrocientos',
        5: 'quinientos', 6: 'seiscientos', 7: 'setecientos',
        8: 'ochocientos', 9: 'novecientos'
    }

    if number == 0:
        return 'cero'
    elif number == 100:
        return 'cien'
    elif number == 1000:
        return 'mil'
    elif number in units:
        return units[number]
    
    # Для чисел от 1000 до 9999
    if 1000 <= number <= 9999:
        thousands = number // 1000
        rest = number % 1000
        
        # Особый случай для 1000
        if thousands == 1:
            thousand_str = 'mil'
        else:
            thousand_str = f"{units[thousands]} mil"
            
        if rest == 0:
            return thousand_str
        elif rest < 100:
            return f"{thousand_str} {number_to_words_spanish(rest)}"
        else:
            return f"{thousand_str} {number_to_words_spanish(rest)}"
    
    # Для чисел от 30 до 99
    if 30 <= number <= 99:
        ten = number // 10
        unit = number % 10
        if unit == 0:
            return tens[ten]
        return f"{tens[ten]} y {units[unit]}"
    
    # Для чисел от 100 до 999
    if 100 <= number <= 999:
        hundred = number // 100
        rest = number % 100
        if rest == 0:
            return hundreds[hundred]
        return f"{hundreds[hundred]} {number_to_words_spanish(rest)}"
    
    return str(number)

def convert_numbers_to_words(text):
    """
    Заменяет все числа в испанском тексте на их словесное представление.
    
    Args:
        text (str): Входной текст на испанском языке
        
    Returns:
        str: Текст с замененными числами на их словесное представление
    """
    def replace_number(match):
        number = int(match.group())
        return number_to_words_spanish(number)
    
    # Используем регулярное выражение для поиска чисел
    pattern = r'\b\d+\b'
    return re.sub(pattern, replace_number, text)

# Примеры использования
if __name__ == "__main__":
    test_cases = [
        "Gracias! He grabado su promesa de pago por la cantidad de 100 euros para el día de hoy",
        "La población de la ciudad es de 8500 habitantes",
        "Necesito 1000 euros para el alquiler",
        "El precio es 2345 euros",
        "Tengo 5432 razones para sonreír"
    ]
    
    for test in test_cases:
        result = convert_numbers_to_words(test)
        print(f"Исходный текст: {test}")
        print(f"Результат: {result}")
        print("-" * 50)
