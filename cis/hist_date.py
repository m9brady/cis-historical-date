from datetime import datetime

# CIS "Historical Dates" for matching with chart-issuance dates
HIST_DATES = [
    '0101', '0108', '0115', '0122', '0129', '0205', '0212', '0219',
    '0226', '0305', '0312', '0319', '0326', '0402', '0409', '0416',
    '0423', '0430', '0507', '0514', '0521', '0528', '0604', '0611',
    '0618', '0625', '0702', '0709', '0716', '0723', '0730', '0806',
    '0813', '0820', '0827', '0903', '0910', '0917', '0924', '1001',
    '1008', '1015', '1022', '1029', '1105', '1112', '1119', '1126',
    '1204', '1211', '1218', '1225'
]

# this could be trivialized with python-dateutil but want to stay with built-in modules
POSSIBLE_DATE_FMTS = [
    '%Y%m%d', '%Y-%m-%d', '%Y/%m/%d', '%m/%d/%Y'
]

def parse_date(date_str: str) -> datetime:
    for fmt in POSSIBLE_DATE_FMTS:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    raise ValueError(f'Could not parse chart date {date_str!r} with any expected date format')

def calc_historical_date(chart_date: str) -> str:
    '''
    Given a chart date (expected as YYYYMMDD string), return the CIS "historical chart" value
    
    Most chart dates should be +/- 3 days from the correct HIST_DATE
    
    Caveats:
        1126 is +4/-3
        0226 is +4/-3 on leap years
    '''
    chart_dt = parse_date(chart_date)
    # CIS treats Feb 29 as Feb 28 as per sea_ice_area_table_format_description.txt line 1222
    if chart_dt.month == 2 and chart_dt.day == 29:
        chart_dt = datetime(chart_dt.year, 2, 28)
    # compile the list of possible hist_date matches for the given year
    hist_dates = [
        datetime(chart_dt.year, int(d[:2]), int(d[2:]))
        for d in HIST_DATES
    ]
    # extra timestep at end to account for late December
    hist_dates.append(datetime(chart_dt.year + 1, 1, 1))
    # find the index of the matching nearest hist_date (i.e. smallest tdiff)
    tdiffs = [abs(hist_date - chart_dt) for hist_date in hist_dates]
    match_idx = tdiffs.index(min(tdiffs))
    # if the match is in the following year (e.g. for chart_date of Dec 31), we return the 101 hist_date
    match_idx = 0 if match_idx == 52 else match_idx
    return HIST_DATES[match_idx]
