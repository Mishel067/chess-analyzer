import sqlite3
from math import *
import pandas as pd
conn = sqlite3.connect(':memory:')
conn.execute('''
create table chess (
    game_id INTEGER,
    date TEXT,
    color TEXT,
    opponent_rating INTEGER,
    result INTEGER
)
''')

data = [
(1,'1997-08-05','white',2553,1),
(2,'1962-09-02','black',1782,1),
(3,'2020-08-21','black',1525,0),
(4,'1957-11-17','white',2801,0),
(5,'1909-08-25','white',1084,1),
(6,'2020-12-23','white',2060,0),
(7,'1972-11-23','white',2005,0),
(8,'1908-05-16','white',1145,1),
(9,'1926-07-31','white',1959,1),
(10,'1930-06-03','black',2863,0),
(11,'1972-03-02','white',2483,0),
(12,'1948-11-23','black',1777,0),
(13,'1957-04-06','black',2435,0),
(14,'1978-03-08','white',1908,0),
(15,'1985-01-31','white',1991,1),
(16,'2023-09-12','black',2634,1),
(17,'1932-11-03','black',2780,1),
(18,'1977-03-05','black',2070,1),
(19,'1987-12-02','black',1908,0),
(20,'1994-11-26','white',1991,1),
(21,'1991-10-01','black',1529,1),
(22,'1915-10-02','black',2856,1),
(23,'1930-08-16','white',2456,1),
(24,'1955-07-08','black',1106,1),
(25,'1911-04-03','black',1020,1),
(26,'1992-04-06','white',2487,1),
(27,'1916-11-17','black',1761,1),
(28,'1910-01-15','white',2331,0),
(29,'2017-03-07','white',1344,1),
(30,'2008-12-19','white',2230,0)
]
conn.executemany('Insert into chess values(?,?,?,?,?)', data)
conn.commit()
df = pd.read_sql('select * from chess',conn)
white_wins = len(df[(df['color'] == 'white') & (df['result'] == 1)])
black_wins = len(df[(df['color'] == 'black') & (df['result'] == 1)])
print('\n Chess Stats')
print(f'Total games: {len(df)}')
print(f'Wins: {df['result'].sum()}')
print(f'Average opponent rating: {ceil(df['opponent_rating'].mean())}')
print(f'Wins with white: {white_wins}')
print(f'Wins with black: {black_wins}')
print(f'Win rate: {ceil(df['result'].sum() / len(df)*100)}%')
if black_wins < white_wins:
  print('More wins with white pieces.')
elif black_wins > white_wins:
  print('More wins with black pieces.')
else:
  print('Equal wins with white and black pieces.')
print('All games:')
print(df.to_string(index=False))