from database import SessionLocal
import models

def check():
    db = SessionLocal()
    try:
        products = db.query(models.Product).all()
        print(f"Total products in DB: {len(products)}")
        for p in products:
            print(f"- {p.name} ({p.category})")
    finally:
        db.close()

if __name__ == "__main__":
    check()
