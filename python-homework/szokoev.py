def escape_year(year):
    is_esc_year = False
    if (year % 4) == 0:
        is_esc_year = True
        if (year % 100) == 0:
            is_esc_year = False
            if (year % 400) == 0:
                is_esc_year = True
    return is_esc_year


year_to_check = int(input('Kérem adjon meg egy évszámot, hogy szökőév-e? = '))
if escape_year(year_to_check):
    print(year_to_check, 'Szökőév.')
else:
    print(year_to_check, 'Nem szökőév.')