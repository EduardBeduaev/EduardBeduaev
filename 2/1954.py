import requests


def get_game_discount(app_id, country_code="US"):
    """
    Получает информацию о скидке на игру в Steam.

    Args:
        app_id (int): ID приложения (AppID) игры в Steam.
        country_code (str): Код страны (например, "US", "RU", "EU").

    Returns:
        dict: Словарь с информацией о скидке (если есть), или None, если произошла ошибка.
    """
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}&cc={country_code}&l=english&filters=price_overview"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на HTTP ошибки
        data = response.json()

        if data and str(app_id) in data and data[str(app_id)]["success"]:
            game_data = data[str(app_id)]["data"]
            if "price_overview" in game_data:
                price_overview = game_data["price_overview"]
                if price_overview["discount_percent"] > 0:
                    return {
                        "name": game_data["name"],
                        "discount_percent": price_overview["discount_percent"],
                        "final_formatted": price_overview["final_formatted"],
                        "currency": price_overview["currency"]
                    }
                else:
                    return None  # Скидки нет
            else:
                return None  # Нет информации о цене
        else:
            return None  # Не удалось получить данные об игре

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


# Пример использования:
app_id = 121  # Counter-Strike: Global Offensive
discount_info = get_game_discount(app_id)

if discount_info:
    print(
        f"На игру {discount_info['name']} есть скидка {discount_info['discount_percent']}%! Цена: {discount_info['final_formatted']} {discount_info['currency']}")
else:
    print(f"На игру {app_id} скидок нет.")
