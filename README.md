##  Canadian Ice Service (CIS) Historical Dates

In recent years, regional ice analysis charts produced by the CIS are generated on a regular basis and are said to be valid for Monday of a given week [[1]](#1). However, charts produced in years prior did not have this regular schedule so one way to introduce standardization is to use a fixed "Historical Date" to enable climatological (long-term) analysis. 

This Python code repository attempts to estimate the `HIST_DATE` given a chart-issuance date with zero third-party dependencies.

To learn more about the charts produced by the CIS, go to https://www.canada.ca/en/environment-climate-change/services/ice-forecasts-observations/latest-conditions/products-guides/chart-descriptions.html


## How-To

0. Ensure you have Python installed and available for use

1. Download the repository:
```
git clone https://github.com/m9brady/cis-historical-date
cd cis-historical-date
```

2. Run the examples:

```
python example.py
chart_date: 20150302 --> hist_date: 0305
chart_date: 19780713 --> hist_date: 0716
chart_date: 20120301 --> hist_date: 0226
chart_date: 19951231 --> hist_date: 0101
```

3. Use the function interactively:

```python
>>> from cis import calc_historical_date
>>> calc_historical_date('20140901')
'0903'
```


### References

<a id="1">[1]</a> https://www.canada.ca/en/environment-climate-change/services/ice-forecasts-observations/latest-conditions/products-guides/chart-descriptions.html#weekly_ice