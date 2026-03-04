import requests
from app.config import settings

def check_fact(message):

    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

    params = {
        "query": message,
        "key": settings.FACT_CHECK_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "claims" in data:
        claim = data["claims"][0]
        review = claim["claimReview"][0]

        return {
            "result": review["textualRating"],
            "source": review["publisher"]["name"]
        }

    return None