from googletrans import Translator
import asyncio

def translate_text(text: str, target_lang: str = "ja") -> str:
    translator = Translator()
    try:
        result = asyncio.run(translator.translate(text, dest=target_lang))
        return result.text
    except Exception as e:
        print("翻訳エラー:", e)
        return "[翻訳できませんでした]"
