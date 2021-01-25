import math
def calculateStats(numbers):
    StatsDict = {}
    if len(numbers) <=0:
        StatsDict = dict.fromkeys(["avg", "max", "min"], math.nan)
    else:
        StatsDict["max"] = max(numbers)
        StatsDict["avg"] = sum(numbers) / len(numbers)       
        StatsDict["min"] = min(numbers)
        
    return StatsDict
