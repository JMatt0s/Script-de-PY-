import phonenumbers
from phonenumbers import geocoder, carrier

def v_numero(telefono):
    try:  
        telefono = phonenumbers.parse(telefono)
        
        if not phonenumbers.is_valid_number(telefono):
            return "Invalid phone number."
        
        country = geocoder.description_for_number(telefono, "en")
        operator = carrier.name_for_number(telefono, "en")

        return {"country": country, "operator": operator}

    except phonenumbers.NumberParseException:
        return "Error parsing phone number."

number = input("ingresar numero de telefono aqui: ")
print(v_numero(number))
