import re
def datedetection(inputdate):
    date=re.compile(r'((\d{2})/(\d{2})/(\d{4}))')
    inputdate=date.search(inputdate)

    month = inputdate.group(2)
    day   = inputdate.group(3)
    year  = inputdate.group(4)

    month_range_30=['04','06','09','11']
    month_range_31=['01','03','05','07','08','10','12']
    if month in month_range_31:
        if int(day)<=31:
            pass
        else:
            print('incorrect Date....')
            return False
    elif month in month_range_30:
        if int(day)<=30:
            pass
        else:
            print('incorrect Date....')
            return False
    
    else:
        print('incorrect Month .....')
        return False
    print(+inputdate.group())


