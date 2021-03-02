select 
    Date,
    UTS,
    YS, 
    El
from 
    TensileData
where 
    "Composition" = ? and 
    "Heat treatment" = ? and
    "Paint Bake" = ? and 
    "Thickness" = ? and
    defective = No 