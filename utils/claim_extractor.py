import re

def extract_claim(text):

    # remove common whatsapp forward phrases
    text = re.sub(r"forwarded.*", "", text, flags=re.IGNORECASE)

    # remove links
    text = re.sub(r"http\S+", "", text)

    # keep first sentence
    claim = text.split(".")[0]

    return claim.strip()