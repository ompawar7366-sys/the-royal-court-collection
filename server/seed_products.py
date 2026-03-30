import requests

PRODUCTS = [
    {
        "name": "Midnight Serenade Ring",
        "description": "A capture of the evening sky, featuring a deep blue sapphire surrounded by a constellation of micro-diamonds set in 18K white gold.",
        "price": 540000,
        "category": "Rings",
        "image_url": "https://images.unsplash.com/photo-1605100804763-247f67b3557e?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "name": "Oura Blossom Earrings",
        "description": "Inspired by the cherry blossoms of Kyoto, these earrings feature pink morganite petals with yellow gold stems.",
        "price": 320000,
        "category": "Earrings",
        "image_url": "https://images.unsplash.com/photo-1630019058353-53580525996b?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "name": "Imperial Gold Cuff",
        "description": "A bold statement of power and elegance. Hand-forged 24K gold with intricate relief work depicting ancient solar motifs.",
        "price": 780000,
        "category": "Bracelets",
        "image_url": "https://images.unsplash.com/photo-1515562141207-7a88fb0ce33e?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "name": "Starlight Chronograph",
        "description": "Precision engineering meets celestial beauty. Featuring a moon-phase dial and a diamond-encrusted bezel.",
        "price": 1500000,
        "category": "Watches",
        "image_url": "https://images.unsplash.com/photo-1523170335258-f5ed11844a49?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "name": "Veridian Heart Pendant",
        "description": "A rare 5-carat heart-cut emerald suspended from a delicate platinum chain, symbolizing eternal life.",
        "price": 1200000,
        "category": "Necklaces",
        "image_url": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "name": "Solaris Citrine Ring",
        "description": "Sunlight crystallized into a 10-carat citrine, set in a halo of yellow diamonds and cognac gold.",
        "price": 410000,
        "category": "Rings",
        "image_url": "https://images.unsplash.com/photo-1603561591411-071c03260639?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "name": "Lumina Pearl Drops",
        "description": "South Sea pearls of exceptional luster, cascading from a branch of diamond-studded white gold.",
        "price": 280000,
        "category": "Earrings",
        "image_url": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "name": "Gilded Ivy Bracelet",
        "description": "Nature's embrace in fine jewelry. A flexible vine of gold leaves shimmering with emerald dewdrops.",
        "price": 390000,
        "category": "Bracelets",
        "image_url": "https://images.unsplash.com/photo-1611591438381-456012659e0a?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "name": "Aurora Borealis Necklace",
        "description": "A spectrum of multi-colored fancy diamonds arranged in a fluid, waving pattern mimicking the Northern Lights.",
        "price": 2500000,
        "category": "Necklaces",
        "image_url": "https://images.unsplash.com/photo-1611085354924-49c89420088b?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "name": "Zenith Skeleton Watch",
        "description": "A masterpiece of transparency. Every moving part visible through sapphire crystal, housed in brushed titanium.",
        "price": 1800000,
        "category": "Watches",
        "image_url": "https://images.unsplash.com/photo-1542496658-e33a6d0d50f6?q=80&w=1000&auto=format&fit=crop"
    }
]

def seed():
    for product in PRODUCTS:
        try:
            response = requests.post("http://127.0.0.1:8000/products/", json=product)
            if response.status_code == 200:
                print(f"Successfully added: {product['name']}")
            else:
                print(f"Failed to add {product['name']}: {response.text}")
        except Exception as e:
            print(f"Error adding {product['name']}: {e}")

if __name__ == "__main__":
    seed()
