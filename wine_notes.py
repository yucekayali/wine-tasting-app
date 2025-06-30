def generate_note(wine_name, appearance, aroma, taste):
    prompt = f"A realistic illustration of a wine glass filled with {appearance['color'].lower()} wine, with {appearance['clarity'].lower()} clarity, and {appearance['legs'].lower()} on the glass."

    note = f"""
**Wine Name**: {wine_name}

**Appearance**: The wine displays a {appearance['color']} hue, appearing {appearance['clarity']} in the glass with {appearance['legs']}, which suggests a notable alcohol or sugar content.

**Aroma**: On the nose, it reveals {aroma['fruit']} characteristics, complemented by {aroma['other']} undertones. The bouquet is expressive, indicating potential complexity and depth.

**Taste**: On the palate, this wine is {taste['sweetness']}, with {taste['acidity']} acidity that provides structure and freshness. It shows a {taste['body']} mouthfeel with {taste['tannin']} tannins that contribute to its framework.

**Finish**: The finish is {taste['finish']}, leaving a lasting impression and encouraging further sips.

**Overall Impression**: This wine shows typicity and elegance, likely benefiting from good vinification practices and terroir expression. Ideal for pairing with complementary dishes or enjoying on its own for contemplation.

**Suggested Image Prompt**: "{prompt}"
"""
    return note, prompt
