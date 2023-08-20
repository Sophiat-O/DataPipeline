import pycountry


def get_iso_alpha(country):
    if type(country) != None:
        country = pycountry.countries.get(alpha_2=country)
        iso_alpha = country.alpha_3

    return iso_alpha
