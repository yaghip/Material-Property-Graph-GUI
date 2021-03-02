select
    "Date",   
    round(avg(UTS), 3) as UTS_average, 
    round(avg(YS), 3) as YS_Average, 
    round(avg(El), 3) as El_Average,
    round(stDev(UTS), 3) as UTS_StDev, 
    round(stDev(YS), 3) as YS_StDev, 
    round(stDev(El), 3) as El_StDev,
    round(stDev("Date"), 3) as Date_StDev
from
    TensileData

where 
    "Composition" = ? and 
    "Heat treatment" = ? and
    "Paint Bake" = ? and 
    "Thickness" = ? and
    defective = No

group by
    Composition, 
    "Paint Bake", 
    "Date", 
    "Heat Treatment", 
    Thickness

