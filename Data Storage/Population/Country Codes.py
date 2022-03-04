from pygal.maps.world import COUNTRIES

def get_country_codes(country_name):
    """Return the Pygal 2-digit country code for the given country."""

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    return None
        
print(get_country_codes('Andorra'))
print(get_country_codes('United Arab Emirates'))
print(get_country_codes('Afghanistan'))