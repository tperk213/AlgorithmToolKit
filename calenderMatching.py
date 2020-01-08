#Time   O(n+m)
#Space  O(n+m)

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # add start and finish times to calandars
        # convert calendars to integer minute format
    calendar1Complete = completeCalendar(calendar1, dailyBounds1)
    calendar2Complete = completeCalendar(calendar2, dailyBounds2)
    # merge calendars
    calendarComplete = mergeCalendars(calendar1Complete, calendar2Complete)
    # flatten calendar
    calendarComplete = flattenCalendar(calendarComplete)
    # construct availabilities
        # convert back to ["hr:min"] format
    return getAvailabilities(calendarComplete,meetingDuration) 

def completeCalendar(calendar, dailyBounds):
    cal = []
    cal.append(["0:00",dailyBounds[0]])
    cal += calendar[:]
    cal.append([dailyBounds[1], "23:59"])
    #convert to min format
    return list(map(lambda m: [timeToMin(m[0]), timeToMin(m[1])], cal))

def convertToMin(calendar):
    #only one line so added to complete calendar function
    cal = list(map(lambda m: [timeToMin(m[0]), timeToMin(m[1])], calendar))


def timeToMin(time):
    hr, minutes = time.split(":")
    hr = int(hr) * 60
    minutes = int(minutes)
    return hr+minutes


def mergeCalendars(calendar1, calendar2):
    merged = []
    i = 0
    j = 0
    while i < len(calendar1) and j < len(calendar2):
        if calendar1[i][0] < calendar2[j][0]:
            merged.append(calendar1[i])
            i += 1
        else:
            merged.append(calendar2[j])
            j += 1
    
    while i <len(calendar1):
        merged.append(calendar1[i])
        i+= 1
    while j <len(calendar2):
        merged.append(calendar2[j])
        j+= 1
    return merged
    
def flattenCalendar(calendar):
    calFlat = [calendar[0]]
    for i in range(1, len(calendar)):
        prev = calFlat[-1]
        cur = calendar[i]
        if cur[0] <= prev[1]:
            slot = []
            slot.append(prev[0])
            slot.append(max(prev[1], cur[1]))
            calFlat[-1] = slot
        else:
            calFlat.append(cur)
    return calFlat
    
def getAvailabilities(calendar, minTime):
    avails = []
    prev = calendar[0]
    for i in range(1, len(calendar)):
        cur = calendar[i]
        if cur[0] - prev[1] >= minTime:
            avails.append([prev[1], cur[0]])
        prev = cur[:]
    return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])],avails))

def minutesToTime(minutes):
    hrs = minutes // 60
    mins = minutes % 60
    mins = str(mins) if mins >= 10 else "0"+str(mins)
    return str(hrs)+":"+mins



if __name__ == "__main__":
    calendar1 = [
        ["10:00", "10:30"],
        ["10:45", "11:15"], 
        ["11:30", "13:00"],
        ["14:15", "16:00"],
        ["16:00", "18:00"]
    ]
    dailyBounds1 =["9:30","20:00"]
    calendar2 = [
        ["10:00", "11:00"],
        ["12:30","13:30"],
        ["14:30", "15:00"], 
        ["16:00", "17:00"]
    ]
    dailyBounds2 = ["09:00", "18:30"]
    meetingDuration = 15

    #expected = [
    # ["9:30", "10:00"],
    # ["11:15", "11:30"], 
    # ["13:30", "14:15"],
    # ["18:00", "18:30"]
    #]
    k = calendarMatching(calendar1,dailyBounds1,calendar2,dailyBounds2,meetingDuration)
    print(k)