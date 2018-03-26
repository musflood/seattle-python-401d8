
# Sacramento Crime Data Stats - January 2006


```python
import pandas as pd
import numpy as np
from datetime import datetime
```


```python
df = pd.read_csv('./SacramentocrimeJanuary2006.csv')  # Import the csv file as a DataFrame Object
```


```python
df.head()  # prints the first few rows of the data frame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cdatetime</th>
      <th>address</th>
      <th>district</th>
      <th>beat</th>
      <th>grid</th>
      <th>crimedescr</th>
      <th>ucr_ncic_code</th>
      <th>latitude</th>
      <th>longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/06 0:00</td>
      <td>3108 OCCIDENTAL DR</td>
      <td>3</td>
      <td>3C</td>
      <td>1115</td>
      <td>10851(A)VC TAKE VEH W/O OWNER</td>
      <td>2404</td>
      <td>38.550420</td>
      <td>-121.391416</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/1/06 0:00</td>
      <td>2082 EXPEDITION WAY</td>
      <td>5</td>
      <td>5A</td>
      <td>1512</td>
      <td>459 PC  BURGLARY RESIDENCE</td>
      <td>2204</td>
      <td>38.473501</td>
      <td>-121.490186</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/1/06 0:00</td>
      <td>4 PALEN CT</td>
      <td>2</td>
      <td>2A</td>
      <td>212</td>
      <td>10851(A)VC TAKE VEH W/O OWNER</td>
      <td>2404</td>
      <td>38.657846</td>
      <td>-121.462101</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/1/06 0:00</td>
      <td>22 BECKFORD CT</td>
      <td>6</td>
      <td>6C</td>
      <td>1443</td>
      <td>476 PC PASS FICTICIOUS CHECK</td>
      <td>2501</td>
      <td>38.506774</td>
      <td>-121.426951</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/1/06 0:00</td>
      <td>3421 AUBURN BLVD</td>
      <td>2</td>
      <td>2A</td>
      <td>508</td>
      <td>459 PC  BURGLARY-UNSPECIFIED</td>
      <td>2299</td>
      <td>38.637448</td>
      <td>-121.384613</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.describe()  # Provide some built-in statistics on the data... Sometimes useful, not so much in this case.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>district</th>
      <th>grid</th>
      <th>ucr_ncic_code</th>
      <th>latitude</th>
      <th>longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>7584.000000</td>
      <td>7584.000000</td>
      <td>7584.000000</td>
      <td>7584.000000</td>
      <td>7584.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.574631</td>
      <td>916.250791</td>
      <td>4275.068829</td>
      <td>38.559809</td>
      <td>-121.463832</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.642512</td>
      <td>407.436310</td>
      <td>2171.593193</td>
      <td>0.056101</td>
      <td>0.034621</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>102.000000</td>
      <td>909.000000</td>
      <td>38.437999</td>
      <td>-121.555832</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.000000</td>
      <td>567.000000</td>
      <td>2309.000000</td>
      <td>38.518476</td>
      <td>-121.489543</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3.000000</td>
      <td>899.000000</td>
      <td>3532.000000</td>
      <td>38.559523</td>
      <td>-121.465459</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5.000000</td>
      <td>1264.000000</td>
      <td>7000.000000</td>
      <td>38.610361</td>
      <td>-121.435947</td>
    </tr>
    <tr>
      <th>max</th>
      <td>6.000000</td>
      <td>1661.000000</td>
      <td>8102.000000</td>
      <td>38.683789</td>
      <td>-121.365238</td>
    </tr>
  </tbody>
</table>
</div>



## Clean up the datetime date


```python
df['cdatetime'].tail()
# See how ugly and unusable these dates are? We need consistency here to aggregate further down the line...
```




    7579    1/31/06 23:36
    7580    1/31/06 23:40
    7581    1/31/06 23:41
    7582    1/31/06 23:45
    7583    1/31/06 23:50
    Name: cdatetime, dtype: object




```python
# First we're going to parse through and get just the dates => 01/31/06
df['cdatetime'] = df['cdatetime'].map(lambda date: date.split(' ')[0])
# Next we're going to create a datetime object using that parsed date
df['cdatetime'] = df['cdatetime'].map(lambda date: str(datetime.strptime(date, '%m/%d/%y')))
```

## Number of occurences by District


```python
dist_count = df['district'].value_counts().sort_index()
dist_count
```




    1     868
    2    1462
    3    1575
    4    1161
    5    1159
    6    1359
    Name: district, dtype: int64




```python
dist_count.index = dist_count.index.map(lambda idx: 'District {}'.format(idx))
dist_count
```




    District 1     868
    District 2    1462
    District 3    1575
    District 4    1161
    District 5    1159
    District 6    1359
    Name: district, dtype: int64



## Count of incidents per day - Ordered by Date


```python
date_count = df['cdatetime'].value_counts()
date_count.sort_index()
```




    2006-01-01 00:00:00    250
    2006-01-02 00:00:00    145
    2006-01-03 00:00:00    256
    2006-01-04 00:00:00    257
    2006-01-05 00:00:00    268
    2006-01-06 00:00:00    233
    2006-01-07 00:00:00    242
    2006-01-08 00:00:00    182
    2006-01-09 00:00:00    261
    2006-01-10 00:00:00    244
    2006-01-11 00:00:00    311
    2006-01-12 00:00:00    265
    2006-01-13 00:00:00    272
    2006-01-14 00:00:00    207
    2006-01-15 00:00:00    214
    2006-01-16 00:00:00    199
    2006-01-17 00:00:00    282
    2006-01-18 00:00:00    295
    2006-01-19 00:00:00    266
    2006-01-20 00:00:00    274
    2006-01-21 00:00:00    213
    2006-01-22 00:00:00    204
    2006-01-23 00:00:00    241
    2006-01-24 00:00:00    277
    2006-01-25 00:00:00    249
    2006-01-26 00:00:00    254
    2006-01-27 00:00:00    279
    2006-01-28 00:00:00    251
    2006-01-29 00:00:00    182
    2006-01-30 00:00:00    266
    2006-01-31 00:00:00    245
    Name: cdatetime, dtype: int64




```python
date_count.sum()
```




    7584



## Turn a Series into a DataFrame


```python
date_df = date_count.to_frame()
date_df.columns = ['Incidents']
date_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Incidents</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2006-01-11 00:00:00</th>
      <td>311</td>
    </tr>
    <tr>
      <th>2006-01-18 00:00:00</th>
      <td>295</td>
    </tr>
    <tr>
      <th>2006-01-17 00:00:00</th>
      <td>282</td>
    </tr>
    <tr>
      <th>2006-01-27 00:00:00</th>
      <td>279</td>
    </tr>
    <tr>
      <th>2006-01-24 00:00:00</th>
      <td>277</td>
    </tr>
  </tbody>
</table>
</div>


