from kaggle.api.kaggle_api_extended import KaggleApi
from line_bot.util.translate import translate_text

api = KaggleApi()
api.authenticate()

def fetch_competitions() -> str:
    ret = ""
    competitions = api.competitions_list(sort_by='latestDeadline')
    for comp in competitions:
        text = comp.description.strip()
        ret += f"""
        コンペ: {comp.title}
        締め切り: {comp.deadline}
        URL: {comp.ref}
        {translate_text(text, 'ja')[:100]}...
        ---"""
    return ret