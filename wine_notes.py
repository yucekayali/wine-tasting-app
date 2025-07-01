def build_overall_impression(taste, aroma, body_note, sweetness_note):
    if taste["body"] == "Full":
        depth = "This wine delivers bold structure and depth, offering a memorable tasting experience."
    elif taste["body"] == "Light":
        depth = "Elegant in its simplicity, this wine offers a clean and refreshing profile ideal for relaxed occasions."
    elif taste["body"] == "Creamy":
        depth = "Its soft, rounded texture invites leisurely sipping, making it an indulgent and comforting choice."
    else:
        depth = "Balanced and composed, this wine sits comfortably between freshness and richness."

    if aroma["other"] == "Spicy" and taste["sweetness"] in ["Dry", "Off-dry"]:
        nuance = "The spice-driven nose combined with its dry palate gives it a lively, gastronomic personality."
    elif aroma["fruit"] == "Tropical" and taste["acidity"] in ["High", "Zippy"]:
        nuance = "Its vibrant acidity and tropical character make it a bright and exotic expression."
    elif aroma["other"] == "Earthy":
        nuance = "Earth-driven nuances suggest complexity and potential for food pairing with rustic dishes."
    elif taste["tannin"] == "Astringent":
        nuance = "Its firm tannins imply aging potential, though it currently calls for rich, hearty cuisine."
    else:
        nuance = "This wine showcases clarity and typicity, true to its varietal roots."

    close = "Overall, it is a well-executed wine that reflects thoughtful winemaking and expressive terroir."
    return f"{depth} {nuance} {close}"


def generate_note(wine_name, appearance, aroma, taste):
    prompt = f"A realistic illustration of a wine glass filled with {appearance['color'].lower()} wine, with {appearance['clarity'].lower()} clarity, and {appearance['legs'].lower()} on the glass."

    # Görsel açıklamaları
    appearance_desc = appearance["color"]
    clarity_desc = appearance["clarity"]
    legs_desc = appearance["legs"]

    fruit_profile = aroma["fruit"]
    other_note = aroma["other"]
    sweetness_note = taste["sweetness"]
    acidity_note = taste["acidity"]
    body_note = taste["body"]
    tannin_note = taste["tannin"]
    finish_note = taste["finish"]

    # Şarap eşleştirmesi
    def suggest_wine(taste, aroma):
        if taste["body"] == "Full" and aroma["fruit"] == "Black fruit":
            return "Cabernet Sauvignon"
        elif taste["body"] == "Light" and aroma["fruit"] == "Citrus":
            return "Sauvignon Blanc"
        elif taste["sweetness"] in ["Medium sweet", "Sweet"]:
            return "Riesling"
        elif taste["body"] == "Medium" and aroma["other"] == "Spicy":
            return "Syrah"
        elif aroma["other"] == "Earthy":
            return "Pinot Noir"
        elif taste["body"] == "Creamy" and aroma["fruit"] == "Stone fruit":
            return "Chardonnay"
        else:
            return "Rosé or versatile white wine"

    suggestion = suggest_wine(taste, aroma)
    overall_impression = build_overall_impression(taste, aroma, body_note, sweetness_note)

    # Tadım Notu
    note = f"""
**Wine Name**: {wine_name}

**Appearance**: This wine is {appearance_desc}, with a {clarity_desc} quality and {legs_desc}.

**Aroma**: The nose reveals {fruit_profile}, supported by {other_note}. The aromatic profile is expressive and layered.

**Taste**: On the palate, it is {sweetness_note}, showing {acidity_note} acidity, a {body_note}, and {tannin_note}.

**Finish**: The finish is {finish_note}.

**Suggested Wine Match**: Based on your selections, a suitable wine match would be **{suggestion}**.

**Overall Impression**: {overall_impression}

**Suggested Image Prompt**: "{prompt}"
"""
    return note, prompt
