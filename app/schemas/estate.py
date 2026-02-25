from pydantic import BaseModel
from typing import Optional, List

class EstateListing(BaseModel):
    category: str         
    status: str         
    city: str            
    district: str         
    neighborhood: str    
    area: str              
    price: str           
    detail_url: str