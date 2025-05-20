from icecream import ic

def format_as_html(row):
    if len(row) < 4:
        return "Yangi javob to'liq emas."
    
    old_response = f"""Sizga mos yo'nalishlar:
       
{row[25].split(', ')[0]} - {row[26].split(', ')[0]}
{row[25].split(', ')[1]} - {row[26].split(', ')[1]}

Bog'lanish uchun: 
+998 33 600 77 07
+998 99 600 77 07
"""

    response = f"""Test natijangiz:
       
{row[25].split(', ')[0]} - {row[26].split(', ')[0]}
{row[25].split(', ')[1]} - {row[26].split(', ')[1]}

Bepul maslahat + chegirma olish uchun:
+998 99 600 77 07
"""

    return response
