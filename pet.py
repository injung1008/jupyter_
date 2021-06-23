# 1. 판다스와 넘파이를 임포트하기
import numpy as np
import pandas as pd
from icecream import ic


if __name__ == '__main__':
    menu = input('0. 종료\n'
                 '1. 라이브러리 임포트\n'
                 '2. 판다스 버전 출력 \n'
                 '3. 판다스 라이브러리 버전 정보 모두 출력\n'
                 '4. 주어진 값으로 DataFrame 객체를 생성하시오\n'
                 '5. 객체내부 정보를 출력\n'
                 '6. 객체 상위 3열까지 출력\n'
                 '7. animal과 age 컬럼만 출력\n'
                 '8. 객체의 3, 4, 8번 행에 해당하는 animal과 age 값만 출력\n'
                 '9. visit 컬럼에서 3 초과하는 값 출력\n'
                 '10. age 에서 NaN 값 출력\n'
                 '11. age가 3살 미만 고양이값 출력\n'
                 '12. age가 2살이상 4살 미만인 값 출력\n'
                 '13. f 행의 나이를 1.5살로 변경\n'
                 '14. 객체에서 visit 의 합 출력\n'
                 '15. 동물별로 나이의 평균 출력\n'
                 '16. k행을 추가하여 dog , 5.5세, 방문회수 2회, 우선권없음(no) 열을 추가\n'
                 '16-1 방금 추가한 열 삭제\n'
                 '17. 객체에 있는 동물의 종류의 수 출력\n'
                 '18. age 는 내림차순, visits 는 오름차순으로 정렬\n'
                 '19. priority 의 yes를 True, no 를 False  로 맵핑 후 출력\n'
                 '20. snake 를 python 으로 값을 변경\n')


    def quiz_2():
        ic(pd.__version__)


    def quiz_3():
        ic(pd.show_versions())


    def quiz_4():
        df = pd.DataFrame({'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                           'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                           'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                           'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']},
                          index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

        ic(df)


    def quiz_5():
        ic(df.describe())

    def quiz_6():
        ic(df.iloc[:3])


    def quiz_7():
        ic(df.loc[:, ['animal', 'age']])


    def quiz_8():
        ic(df.loc[df.index[[3,4,8]], ['animal','age']])


    def quiz_9():
        ic(df[df['visits']>2])


    def quiz_10():
        ic(df[df['age'].isnull()])


    def quiz_11():
        ic(df[(df['age'] <3) & (df['animal'] =='cat')])


    def quiz_12():
        ic(df[df['age'].between(2,4)])


    def quiz_13():
        ic(df.loc['f','age'] = 1.5)


    def quiz_14():
        ic(df['visits'].sum())


    def quiz_15():
        ic(df.groupby('animal')['age'].mean())


    def quiz_16():
        ic(df.loc['k'] = ['dog',5.5,2,'no'])
        df.drop('k', inplace=True)


    def quiz_17():
        ic(df['animal'].value_counts())

    def quiz_18():
        ic(pddf.sort_values(by=['age','visits'], ascending=[False, True]))


    def quiz_19():
        df['priority'] = df['priority'].map({'yes':True, 'no':False})





    def quiz_20():
        ic(df['animal'] = df['animal'].replace('snake','python'))




    while 1:
        select = input(menu)
        if select == '0': break
        elif select == '2': quiz_2()
        elif select == '3': quiz_3()
        elif select == '4': quiz_4()
        elif select == '5': quiz_5()
        elif select == '6': quiz_6()
        elif select == '7': quiz_7()
        elif select == '8': quiz_8()
        elif select == '9': quiz_9()
        elif select == '10': quiz_10()
        elif select == '11': quiz_11()
        elif select == '12': quiz_12()
        elif select == '13': quiz_13()
        elif select == '14': quiz_14()
        elif select == '15': quiz_15()
        elif select == '16': quiz_16()
        elif select == '17': quiz_17()
        elif select == '18': quiz_18()
        elif select == '19': quiz_19()
        elif select == '20': quiz_20()






