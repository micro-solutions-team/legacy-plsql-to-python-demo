from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .db import SessionLocal, engine, Base
from .models import Customer
from .service import evaluate_eligibility


Base.metadata.create_all(bind=engine)



app = FastAPI(title="Legacy Rules Modernization Demo")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/seed")
def seed_data(db: Session = Depends(get_db)):
    customer = Customer(
        id=1,
        customer_type="STANDARD",
        monthly_usage=720,
        debt_amount=1200
    )
    db.merge(customer)
    db.commit()
    return {"status": "seeded"}

@app.get("/evaluate/{customer_id}")
def evaluate(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    result = evaluate_eligibility(customer)

    return {
        "customer_id": customer.id,
        **result
    }
