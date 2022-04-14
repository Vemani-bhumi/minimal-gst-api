from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(prefix="/taxdue",tags=["TaxDue"])

@router.get("/")
def get_tax_due(db : Session = Depends(get_db)):
    tax_due = db.query(models.TaxDue).all()

    return tax_due

@router.get("/{id}")
def get_tax_due(id : int,db : Session = Depends(get_db)):
    tax_due = db.query(models.TaxDue).filter(models.TaxDue.user_id == id).first()

    if not tax_due:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"user with id: {id} was not  found")

    return tax_due

@router.post("/")
def create_tax_due(tax_due : schemas.TaxDueCreate, db : Session = Depends(get_db)):

    new_tax_due = models.TaxDue(**tax_due.dict())
    db.add(new_tax_due)
    db.commit()
    db.refresh(new_tax_due)
    return new_tax_due
    

@router.patch("/{id}",response_model=schemas.TaxDue)
def update_tax_due_status(id:int, updated_tax_due : schemas.TaxDue,db : Session = Depends(get_db)):
    tax_due_query = db.query(models.TaxDue).filter(models.TaxDue.user_id == id)
    tax_due = tax_due_query.first()

    if tax_due == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id {id} does not exist')
    tax_due_query.update(updated_tax_due.dict(exclude_unset=True),synchronize_session=False)
    db.commit()

    return tax_due_query.first()
    



