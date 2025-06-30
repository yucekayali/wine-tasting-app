def generate_note(wine_name, appearance, aroma, taste):
    prompt = f"A realistic illustration of a wine glass filled with {appearance['color'].lower()} wine, with {appearance['clarity'].lower()} clarity, and {appearance['legs'].lower()} on the glass."

    # Appearance descriptions
    appearance_desc = {
        "Pale": "delicate and subtle in color, suggesting a youthful or lightly extracted wine",
        "Medium": "balanced in appearance, indicating a classic style",
        "Deep": "intensely pigmented, possibly from extended maceration or oak aging",
        "Garnet": "slightly aged red wine, with tertiary development",
        "Amber": "oxidative aging, often seen in sherries or aged whites",
        "Purple": "indicative of youth, especially in bold red wines"
    }.get(appearance["color"], "visually characteristic")

    clarity_desc = {
        "Brilliant": "extremely polished and bright",
        "Clear": "well-made with no faults",
        "Slightly hazy": "natural or unfiltered style",
        "Dull": "potential issues or minimal intervention winemaking"
    }.get(appearance["clarity"], "visually typical")

    legs_desc = {
        "No legs": "low alcohol or dry style",
        "Some legs": "moderate alcohol level",
        "Pronounced legs": "indicative of higher alcohol or sugar",
        "Tears linger": "rich texture and full body expected"
    }.get(appearance["legs"], "standard viscosity")

    fruit_profile = {
        "Citrus": "zesty and vibrant notes of lemon or grapefruit",
        "Red berries": "fresh strawberries, raspberries or red cherries",
        "Black fruit": "bold aromas like blackberry and blackcurrant",
        "Stone fruit": "ripe peach, apricot or nectarine tones",
        "Tropical": "lively hints of pineapple, mango or banana",
        "Dried fruit": "fig, raisin or prune suggesting some age",
        "No fruit": "austerity or mineral-driven character"
    }.get(aroma["fruit"], "balanced fruit aroma")

    other_note = {
        "Floral": "floral lift of rose, violet or orange blossom",
        "Spicy": "black pepper, clove or cinnamon notes",
        "Herbal": "green herbs, eucalyptus or mint",
        "Earthy": "forest floor, mushroom or truffle notes",
        "Oak": "hints of vanilla, toast or cedar from barrel aging",
        "Mineral": "chalk, flint or wet stone",
        "Petrol": "classic aged Riesling character",
        "None": "clean and focused aroma profile"
    }.get(aroma["other"], "complementary secondary aroma")

    sweetness_note = {
        "Bone dry": "no perceptible sweetness, clean and crisp",
        "Dry": "balanced with just a hint of dryness",
        "Off-dry": "a touch of sweetness softening the acidity",
        "Medium sweet": "noticeable sugar, often dessert-style",
        "Sweet": "lush and rich, perfect for after meals"
    }.get(taste["sweetness"], "moderately sweet")

    acidity_note = {
        "Low": "soft and round, less refreshing",
        "Medium": "balanced acidity for everyday drinking",
        "High": "bright and food-friendly",
        "Zippy": "mouthwatering and sharp, excellent freshness"
    }.get(taste["acidity"], "neutral acidity")

    body_note = {
        "Light": "easy drinking with delicate structure",
        "Medium": "good balance and versatility",
        "Full": "rich, dense and mouth-filling",
        "Creamy": "smooth and round texture",
        "Structured": "firm backbone and aging potential"
    }.get(taste["body"], "standard body")

    tannin_note = {
        "None": "smooth and silky, no astringency",
        "Soft": "gentle grip, well integrated",
        "Medium": "noticeable tannin with balance",
        "Firm": "pronounced structure, good for aging",
        "Astringent": "grippy and drying, needs food pairing"
    }.get(taste["tannin"], "moderate tannin presence")

    finish_note = {
        "Short": "simple but pleasant finish",
        "Medium": "clean and lingering briefly",
        "Long": "memorable and flavor-rich finish",
        "Persistent": "leaves a strong impression",
        "Lingering": "continues to evolve on the palate"
    }.get(taste["finish"], "standard finish")

    # Wine match suggestion
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

    note = f"""
**Wine Name**: {wine_name}

**Appearance**: This wine is {appearance_desc}, with a {clarity_desc} quality and {legs_desc}.

**Aroma**: The nose reveals {fruit_profile}, supported by {other_note}. The aromatic profile is expressive and layered.

**Taste**: On the palate, it is {sweetness_note}, showing {acidity_note} acidity, a {body_note}, and {tannin_note}.

**Finish**: The finish is {finish_note}.

**Suggested Wine Match**: Based on your selections, a suitable wine match would be **{suggestion}**.

**Overall Impression**: This wine showcases personality and precision. Its combination of visual appeal, aromatic depth and textural structure makes it a well-crafted example of its kind.

**Suggested Image Prompt**: "{prompt}"
"""
    return note, prompt
