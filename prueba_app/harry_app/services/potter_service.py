import requests
from ..models import Personaje

API_URL = "https://potterapi-fedeperin.vercel.app/es/characters"


def load_characters():
    Personaje.objects.all().delete()

    try:
        response = requests.get(API_URL)
        characters_list = response.json()

        for item in characters_list:
            Personaje.objects.create(
                nombre=item.get("fullName", "Desconocido"),
                apodo=item.get("nickname", ""),
                casa=item.get("hogwartsHouse", "Ninguna"),
                actor=item.get("interpretedBy", "Desconocido"),
                imagen=item.get("image", ""),
            )

        return f"Se cargaron {len(characters_list)} personajes con sus nombres reales."

    except Exception as e:
        return f"Hubo un error: {str(e)}"
