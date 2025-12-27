import os

# -----------------------------------------
# Folder containing category images
# -----------------------------------------
IMAGE_DIR = "images/categories"

# -----------------------------------------
# Output HTML file
# -----------------------------------------
OUTPUT_HTML = "homepage_tiles.html"

# -----------------------------------------
# Tile template
# -----------------------------------------
TILE_TEMPLATE = """
<div class="category-tile">
    <a href="shop/{slug}.html">
        <img src="images/categories/{filename}" alt="{label}">
        <h3>{label}</h3>
    </a>
</div>
"""

def slugify(name):
    return name.lower().replace("&", "and").replace(" ", "-")

def generate_tiles():
    print("Generating homepage tiles...\n")

    tiles = []

    for filename in sorted(os.listdir(IMAGE_DIR)):
        if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            continue

        label = os.path.splitext(filename)[0].replace("-", " ").title()
        slug = slugify(label)

        tile_html = TILE_TEMPLATE.format(
            slug=slug,
            filename=filename,
            label=label
        )

        tiles.append(tile_html)

    # Write to output file
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write("\n".join(tiles))

    print(f"✅ Tiles written to: {OUTPUT_HTML}")

if __name__ == "__main__":
    generate_tiles()
