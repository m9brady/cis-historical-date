from cis import calc_historical_date

EXAMPLE_CHART_DATES = [
    '20150302',
    '19780713',
    '20120301',
    '19951231'
]

if __name__ == '__main__':
    for example in EXAMPLE_CHART_DATES:
        print('chart_date: %s --> hist_date: %s' % (
            example, calc_historical_date(example)
        ))
