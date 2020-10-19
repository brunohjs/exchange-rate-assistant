_numbers = {
    "zero": 0,
    "um": 1,
    "dois": 2,
    "três": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6,
    "meia": 6,
    "sete": 7,
    "oito": 8,
    "nove": 9,
    "dez": 10,
    "onze": 11,
    "doze": 12,
    "treze": 13,
    "quatorze": 14,
    "quinze": 15,
    "dezesseis": 16,
    "dezessete": 17,
    "dezoito": 18,
    "dezenove": 19,
    "vinte": 20,
    "trinta": 30,
    "quarenta": 40,
    "cinquenta": 50,
    "sessenta": 60,
    "setenta": 70,
    "oitenta": 80,
    "noventa": 90,
    "cem": 100,
    "cento": 100,
    "duzentos": 200,
    "trezentos": 300,
    "quatrocentos": 400,
    "quinhentos": 500,
    "seiscentos": 600,
    "setescentos": 700,
    "oitocentos": 800,
    "novecentos": 900,
    "mil": 1000,
    "milhão": 10**6,
    "bilhão": 10**9,
    "trilhão": 10**12
}

def convertCardinal(cardinal):
    try:
        cardinal = float(cardinal.replace(',', '.'))
    except ValueError:
        pass
    finally:
        if isinstance(cardinal, str):
            total = 0
            cardinal = cardinal.split()
            for num in cardinal:
                if num in _numbers:
                    total += _numbers[num]
            return total
        else:
            return cardinal
