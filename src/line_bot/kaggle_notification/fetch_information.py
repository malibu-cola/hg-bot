from kaggle.api.kaggle_api_extended import KaggleApi
from line_bot.util.translate import translate_text
from textwrap import dedent

api = KaggleApi()
api.authenticate()


def fetch_competitions() -> str | None:
    ret = "【Kaggleの最新コンペ】\n"
    competitions = api.competitions_list(sort_by="latestDeadline")
    if not competitions:
        return None
    for comp in competitions:
        if comp:
            text = comp.description.strip()
            ret += dedent(f"""
            コンペ: {comp.title}
            締め切り: {comp.deadline}
            URL: {comp.ref}
            {translate_text(text, "ja")[:100]}...
            ---""")
    return ret
