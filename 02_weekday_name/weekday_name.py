def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    if day_of_week == 1:
        print ("Sunday")
    if day_of_week == 2:
        print ("Monday")
    if day_of_week == 3:
        print("Tuesday")
    if day_of_week == 4:
        print("Wednesday")
    if day_of_week == 5:
        print("Thursday")
    if day_of_week == 6:
        print("Friday")
    if day_of_week == 7:
        print("Saturday")
    else: 
        return None
    
weekday_name(1)
weekday_name(2)
weekday_name(3)
weekday_name(4)
weekday_name(5)
weekday_name(6)
weekday_name(7)
weekday_name(8)