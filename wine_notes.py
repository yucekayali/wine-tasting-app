def generate_note(wine_name, appearance, aroma, taste):
    note = f"""
**Wine Name**: {wine_name}

**Appearance**: The wine shows a {appearance['color']} color with {appearance['clarity']} clarity and {appearance['legs']}.

**Aroma**: On the nose, it presents {aroma['fruit']} notes along with hints of {aroma['other']}.

**Taste**: It is {taste['sweetness']} on the palate with a {taste['body']} body and a {taste['finish']} finish.

**Overall Impression**: This wine demonstrates a balanced profile and would appeal to those who enjoy well-structured wines with clear varietal character.
"""
    return note
