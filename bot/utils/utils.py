from icecream import ic

def format_as_html(row):
    if len(row) < 4:
        return "Yangi javob to'liq emas."

    response = f"""Test natijangiz:
       
{row[26].split(', ')[0]} - {row[27].split(', ')[0]}
{row[26].split(', ')[1]} - {row[27].split(', ')[1]}

Bepul maslahat + chegirma olish uchun:
+998 99 600 77 07
"""

    return response
