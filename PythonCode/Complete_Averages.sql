select
    "Date",
    round(avg(UTS), 3) as UTS_average, 
    round(avg(YS), 3) as YS_Average, 
    round(avg(El), 3) as El_Average
from
    TensileData

where 
    "Composition" = ? and 
    "Heat treatment" = ? and
    "Paint Bake" = ? and 
    defective = No

group by
    Composition, 
    "Paint Bake", 
    "Date", 
    "Heat Treatment"

