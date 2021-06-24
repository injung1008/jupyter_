#%%

import pandas as pd
import numpy as np
from pandas import DataFrame
from icecream import ic
import pandas.core.series

'''
 - (1) pivot(), pd.pivot_table()

 - (2) stack(), unstack()

 - (3) melt()

 - (4) wide_to_long()

 - (5) pd.crosstab()


'''

#%%

# 30 다음 객체를 customer_id 를 인덱스로하고 product_code 를 컬럼으로, purchare_amount 를 값으로, 재구성하시오
df = pd.DataFrame({"customer_id":['kim','lee','park','song','yoon','kang','tak','ryu','jang'],
               "product_code":['com','phone','tv','com','phone','tv','com','phone','tv'],
               "grade":['A','A','A','A','A','A','B','B','B'],
               "purchase_amount":[30,10,0,40,15,30,0,0,10]})

ic(df)

df = df.pivot(index='customer_id', columns='product_code', values='purchase_amount')

ic(df)

#%%

#31. 다음 객체를 customer_id, grade 를 인덱스로하고 product_code 를 컬럼으로, purchare_amount 를 값으로, 재구성하시오
df = pd.DataFrame({"customer_id":['kim','lee','park','song','yoon','kang','tak','ryu','jang'],
               "product_code":['com','phone','tv','com','phone','tv','com','phone','tv'],
               "grade":['A','A','A','A','A','A','B','B','B'],
               "purchase_amount":[30,10,0,40,15,30,0,0,10]})
#print(df)
df = df.pivot(index=["customer_id","grade"], columns='product_code',values='purchase_amount')
ic(df)

#%%

#stack이 (위에서 아래로 길게, 높게)쌓는 것이면,
#unstack은 쌓이는 것을 앞으로 늘어놓는것(왼쪽에서 오른쪽으로 넓게 라고 연상이 될 수 있습니다
#(tuples는 복수형이기 때문에 리스트 구조로 묶어줘야한다 [()] -> 튜플 형태를 리스트로 묶어줫어 2차원 형태가 된다)

# 32
df = pd.DataFrame(np.arange(16).reshape(4,4),
                index = pd.MultiIndex.from_tuples([('kim','2019'),('kim','2020'),('lee','2019'),('lee','2020')]),
                columns = ['com','phone','tv','notebook'])
ic(df)
# ic(type(df.stack())) pandas.core.series.Series
# 칼럼의 level은 1개 밖에 없으므로 stack(level=-1) 을 별도로 명기하지 않아도 됩니다.
df = df.stack(level=-1, dropna=True)
ic(df)
df = df.unstack(level=0)
ic(df.unstack())
'''
결측값이 있는 데이터셋을 stack() 할 때 결측값을 제거할지(dropna=True),
아니면 결측값을 NaN으로 유지할지(dropna=False) 설정
unstack(level=-1), unstack(level=0), unstack(level=1) 별로
어떤 level이 칼럼으로 이동해서 unstack() 되는지 체크
'''
df = df.reset_index()
df.rename(columns={'level_0':'customer_id','level_1':'year'}, inplace=True)
ic(df)

#%%

'''
melt() 는 ID 변수를 기준으로 원래 데이터셋에 있던 여러개의 칼럼 이름을
'variable' 칼럼에 위에서 아래로 길게 쌓아놓고,
'value' 칼럼에 ID와 variable에 해당하는 값을
넣어주는 식으로 데이터를 재구조화
'''
df = pd.DataFrame({"customer_id":['kim','kim','lee','lee'],
               "product_code":['com','phone','tv','tab'],
               "purchase_count":[1,2,3,4],
               "purchase_amount":[100,200,300,400]})
ic(df)

# (1) df.melt(data, id_vars=['id1', 'id2', ...]) 를 사용한 데이터 재구조화
#df = df.melt(id_vars="customer_id", value_vars= "product_code")
#ic(df)
df = df.melt(id_vars=["customer_id","product_code"], value_vars="purchase_amount")
ic(df)
# (2) pd.melt() 의 variable 이름, value 이름 부여하기 : var_name, value_name


#%%

np.random.seed(10)
df = pd.DataFrame({"Class_1":{0:"A",1:"B",2:"C"},
                  "Class_2":{0:"D",1:"E",2:"F"},
                  "Score_1":{0:"2.5",1:"1.2",2:"0.7"},
                  "Score_2":{0:"3.2",1:"1.3",2:"0.1"},
                   "value": dict(zip(range(3),np.random.randn(3)))})
df["seq"] = df.index
ic(df)
'''
pd.wide_to_long() 함수를 써서 데이터를 재구조화
wide_to_long()은 pivot() 이나 stack() 과는 다르게
"칼럼 이름의 앞부분"과 나머지 "칼럼 이름의 뒷부분"을 구분해서,
칼럼 이름의 앞부분을 칼럼 이름으로,
칼럼 이름의 나머지 뒷부분을 행(row)의 원소로 해서
세로로 길게(long~) 쌓아 줍니다.
pd.widt_to_long() 함수를 한번 사용해서
가로로 넓은 데이터(wide~)를 세로로 길게(long~) 재구조화 하시오.
pd.wide_to_long(data, ["col_prefix_1", "col_prefix_2"], i="idx_1", j="idx_2")
'''
#df = df.melt(id_vars=['seq'], value_vars=["Class 1","Class 2","Score"])
#ic(df)


df = pd.wide_to_long(df, ["Class_","Score_"], i="seq" , j="value")
df
#wide_to_long(데이터프레임, stubnames = {}
# stub 는 그루터기로 전체값의 일부분의 값을 의미한다, class1,class2,class3에서
#반복되는 class어ㅣ store라는 값만 취한
#df, ["Class-1","Class-2"]
#i는 df의 인덱스로 정한 값을 입력한다
#j는 stubname 에서 컬럼명으로 정의한 나머지 부분은 코딩하는 사람이 임의로 정한다
#sep 은 구분자로 stubname과 임의의 칼럼명 사이를 구분하는 패턴이다
#sep에서 ''이면, 구분자가 없는 상태가 되고, 예제처럼 띄어쓰기로 하려면
#'' 반드시 스페이스바를 한번 클릭해야한다
ic(df)

#%%

'''
pd.crosstab()
범주형 변수로 되어있는 요인(factors)별로 교차분석(cross tabulations) 해서,
행, 열 요인 기준 별로 빈도를 세어서 도수분포표(frequency table),
교차표(contingency table) 를 생성한다

# 범주형 변수란 고유한 값이나 범주 수가 제한된 변수(예: 성별 또는 종교)이다.
# 교차분석(cross-tabulation analysis)은 '범주형'으로 구성된 자료들 간의 연관관계를 확인하기 위해
   교차표를 만들어 관계를 확인하는 분석 방법이다.
'''
df = pd.DataFrame({"학생ID" :["kim","kim","kim","lee","lee","park"],
                   "일학기학점":["A","A","A","B","B","B"],
                   "이학기학점":["D","D","D","C","C","D"]})
ic(df)

# (1) 교차표(contingency table, frequency table) 만들기 : pd.crosstab(index, columns)
#df = pd.crosstab(index=[df.일학기학점] ,columns= df.학생ID)
#ic(df)
# (2) Multi-index, Multi-level로 교차표 만들기 : pd.crosstab([id1, id2], [col1, col2])
#df = pd.crosstab(index=[df.일학기학점,df.이학기학점] ,columns= df.학생ID)
#ic(df)
# (3) 교차표의 행 이름, 열 이름 부여 : pd.crosstab(rownames=['xx'], colnames=['aa'])
#df = pd.crosstab(index=[df.일학기학점,df.이학기학점] ,columns= df.학생ID, rownames=['first','second'],colnames=['id'])
#ic(df)
# (4) 교차표의 행 합, 열 합 추가하기 : pd.crosstab(margins=True)
#df = pd.crosstab(index=[df.일학기학점,df.이학기학점] ,columns= df.학생ID,margins=True)
#ic(df)
# (5) 구성비율로 교차표 만들기 : pd.crosstab(normalize=True)
df = pd.crosstab(index=[df.일학기학점,df.이학기학점] ,columns= df.학생ID,normalize=True)
ic(df)
