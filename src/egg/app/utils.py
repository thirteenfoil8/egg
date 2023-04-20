import os
from datetime import datetime

from dotenv import dotenv_values

from config import Config


def get_asset_content():
    """Returns the paths of the user specific assets

    Returns
    -------
    dict
        dictionnary containing paths (strings)
    """
    content = dict()
    asset = Config().ASSET
    content['head_title'] = f"{asset}".upper()
    content['colors'] = f"static/users/{asset}/colors/colors.css"

    content['provider'] = dotenv_values()["PROVIDER"]
    
    for image in ["logo_small", "logo_big"]:
        path = os.path.join(os.getcwd(), 'plateforme_analytique',
                            'app', 'static', 'users', asset, image)
        file = os.listdir(path)[0]
        content[image] = f"static/users/{asset}/{image}/{file}"
    return content


def get_content():
    """Returns the paths of the user specific assets

    Returns
    -------
    dict
        dictionnary containing paths (strings)
    """
    content = get_asset_content()
    content["year"] = datetime.now().year
    return content


def correct_date_format(date):
    corrected_date = datetime.strptime(date, '%Y-%m-%dT%H:%M')
    corrected_date = corrected_date.strftime('%Y-%m-%d %H:%M:%S')
    return corrected_date
