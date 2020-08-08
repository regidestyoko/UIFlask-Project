from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
plt.style.use('seaborn')

app = Flask(__name__)


# read the file `googleplaystore.csv` data and save it to the dataframe object with the name playstore
# `googleplaystore.csv` 파일 데이터를 읽고 playstore라는 이름으로 데이터 프레임 객체에 저장합니다.
playstore = pd.read_csv(r'C:\Users\Regidestyoko\anaconda3\dataanalysis\capstone-UIFlask-master\data\googleplaystore.csv')

# Remove duplicate data based on the App column, while keeping the first data (hint: use subset parameters)
# 첫 번째 데이터를 유지하면서 App 열을 기반으로 중복 데이터를 제거합니다 (힌트 : 하위 집합 매개 변수 사용).
playstore.drop_duplicates(subset = 'App', keep = 'first', inplace=True) 

# This section is for deleting row 10472 because the data values ​​are not stored in the correct column
#이 섹션은 데이터 값이 올바른 열에 저장되지 않았기 때문에 행 10472를 삭제하기위한 것입니다.
playstore.drop([10472], inplace=True)

# Check the data type of the Category column. If it is still stored with the wrong data type format, change it to the appropriate data type
# 카테고리 열의 데이터 유형을 확인하십시오. 여전히 잘못된 데이터 유형 형식으로 저장되어있는 경우 적절한 데이터 유형으로 변경하십시오.
playstore.Category = playstore.Category.astype('category')

# In the Installs column, remove the comma (,) and the plus sign (+) then change the data type to an integer
# 설치 열에서 쉼표 (,) 및 더하기 기호 (+)를 제거한 다음 데이터 유형을 정수로 변경합니다.
playstore.Installs = playstore.Installs.apply(lambda x: x.replace('+',''))
playstore.Installs = playstore.Installs.apply(lambda x: x.replace(',',''))
# part to change the data type of Installs
# 설치의 데이터 유형을 변경하는 부분
playstore.Installs=playstore.Installs.astype('int64')

# This section is to tidy up the Size column, you don't need to change anything in this section
#이 섹션은 크기 열을 정리하기위한 것이므로이 섹션에서 아무것도 변경할 필요가 없습니다.
playstore['Size'].replace('Varies with device', np.nan, inplace = True ) 
playstore.Size = (playstore.Size.replace(r'[kM]+$', '', regex=True).astype(float) * \
             playstore.Size.str.extract(r'[\d\.]+([KM]+)', expand=False)
            .fillna(1)
            .replace(['k','M'], [10**3, 10**6]).astype(int))
playstore['Size'].fillna(playstore.groupby('Category')['Size'].transform('mean'),inplace = True)

# In the Price column, remove the $ character from the Price value then change the data type to float
# Price 열에서 Price 값에서 $ 문자를 제거한 다음 데이터 유형을 float로 변경하십시오.
playstore.Price = playstore.Price.apply(lambda x: x.replace('$',''))
playstore.Price = playstore.Price.astype('float64')

# Change the data type Reviews, Size, Installs into an integer data type
# 데이터 유형 Reviews, 크기, 설치를 정수 데이터 유형으로 변경
playstore[['Reviews','Size']]=playstore[['Reviews','Size']].astype('int64')

@app.route("/")
# This fuction for rendering the table
# 테이블 렌더링을위한이 기능
def index():
    df2 = playstore.copy()

    # Statistics
    # Dataframe top_category is created to store application frequency for each Category.
    # Dataframe top_category는 각 Category에 대한 적용 빈도를 저장하기 위해 생성됩니다.
    # Use crosstab to calculate the frequency of applications in each category then use 'Amount'
    # 교차 분석을 사용하여 각 범주의 응용 프로그램 빈도를 계산 한 다음 '금액'을 사용합니다.
    # as the column name and sort the frequency values ​​from the greatest number. Finally, reset the index of the dataframe top_category
    # 열 이름으로 가장 큰 숫자부터 빈도 값을 정렬합니다. 마지막으로 데이터 프레임 top_category의 인덱스를 재설정합니다.
    # top_category = pd.crosstab(
    #         index = df2['Category'],
    #         columns = 'Jumlah').sort_values('Jumlah',ascending=False).reset_index()
    # Dictionary stats are used to store some data that is used to display values ​​in value boxes and tables
    # 사전 통계는 값 상자 및 테이블에 값을 표시하는 데 사용되는 일부 데이터를 저장하는 데 사용됩니다.
    stats = {
        # This is a section to complete the value box content
        # 밸류 박스 내용을 완성하는 섹션입니다.
        # most category takes the most category name refers to the dataframe top_category
        # 대부분의 카테고리는 카테고리의 이름을 취합니다. 가장 데이터 프레임을 참조합니다. top_category
        # total takes the most category frequency / number refers to the dataframe top_category
        # total은 top_category 데이터 프레임을 참조하여 가장 많은 빈도 / 카테고리 수를 취합니다.
        'most_categories' : 'Family',
        'total': 1832,
        # rev_table is a table containing the 10 most reviewed applications by users.
        # rev_table은 사용자가 가장 많이 검토 한 애플리케이션 10 개를 포함하는 테이블입니다.
        # Please do a proper data aggregation using groupby to display 10 applications sorted by
        # groupby를 사용하여 올바른 데이터 집계를 수행하여 정렬 된 10 개의 애플리케이션을 표시하십시오.
        # Number of user reviews. The table displayed consists of 4 columns, namely Category name, App name, Total Reviews, and Average Rating.
        # 사용자 리뷰 수. 표시되는 테이블은 범주 이름, 앱 이름, 총 리뷰 및 평균 등급의 4 개 열로 구성됩니다.
        # Your aggregation is judged correct if the result is the same as the table attached to this file
        # 결과가이 파일에 첨부 된 표와 동일한 경우 집계가 올바른 것으로 판단됩니다.
        'rev_table' : df2.groupby(['Category','App']).agg({'Reviews':'sum','Rating':'mean'}).sort_values('Reviews',ascending=False).reset_index().head(10).to_html(classes=['table thead-light table-striped table-bordered table-hover table-sm'])
    }

    ## Bar Plot
    ## Lengkapi tahap agregasi untuk membuat dataframe yang mengelompokkan aplikasi berdasarkan Category
    ## 집계 단계를 완료하여 범주별로 애플리케이션을 그룹화하는 데이터 프레임을 만듭니다.
    ## Buatlah bar plot dimana axis x adalah nama Category dan axis y adalah jumlah aplikasi pada setiap kategori, kemudian urutkan dari jumlah terbanyak
    ## x 축이 범주 이름이고 y 축이 각 범주의 응용 프로그램 수인 막대 플롯을 만든 다음 가장 큰 숫자로 정렬합니다.
    cat_order = df2.groupby('Category').agg({'App': 'count'}).reset_index().rename({'App':'Total'}, axis=1).sort_values('Total',ascending=False).head()
    X = cat_order.Category
    Y = cat_order.Total
    my_colors = 'rgbkymc'
    # bagian ini digunakan untuk membuat kanvas/figure
    #이 부분은 캔버스 / 그림을 만드는 데 사용됩니다.
    fig = plt.figure(figsize=(8,3),dpi=300)
    fig.add_subplot()
    # bagian ini digunakan untuk membuat bar plot
    #이 섹션은 플롯 바를 만드는 데 사용됩니다.
    # isi variabel x dan y yang telah di definisikan di atas
    # 위에서 정의한 변수 x와 y를 채 웁니다.
    plt.barh(X,Y, color=my_colors)
    # This section is used to save the plot in image.png format
    #이 섹션은 플롯을 image.png 형식으로 저장하는 데 사용됩니다.
    plt.savefig('cat_order.png',bbox_inches="tight") 

    # This section is used to convert matplotlib png to base64 so that it can be displayed in html templates
    #이 섹션은 html 템플릿에 표시 될 수 있도록 matplotlib png를 base64로 변환하는 데 사용됩니다.
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    # result variable will be inserted into the parameter in the render_template () function so that it can be displayed on the html page
    # 결과 변수는 render_template () 함수의 매개 변수에 삽입되어 html 페이지에 표시 될 수 있습니다.
    result = str(figdata_png)[2:-1]
    
    ## Scatter Plot
    # Make a scatter plot to show the relationship and the distribution of the application as seen from Review vs Rating.
    # Review vs Rating에서 본 애플리케이션의 관계와 분포를 보여주는 산점도를 만듭니다.
    # The scatter size describes how many users have installed the application
    # 분산 크기는 애플리케이션을 설치 한 사용자 수를 나타냅니다.
    X = df2['Reviews'].values # axis x  axis x
    Y = df2['Rating'].values # axis y   axis y   
    area = playstore['Installs'].values/10000000 #산점도 원의 크기, 산점도의 크기
    fig = plt.figure(figsize=(5,5))
    fig.add_subplot()
    # Fill in the method name for scatter plot, variable x, and variable y
    # 산점도, 변수 x 및 변수 y에 대한 메서드 이름을 입력합니다.
    plt.scatter(x=X,y=Y,s=area, alpha=0.3)
    plt.xlabel('Reviews')
    plt.ylabel('Rating')
    plt.savefig('rev_rat.png',bbox_inches="tight")

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result2 = str(figdata_png)[2:-1]

    ## Histogram Size Distribution
    # Create a histogram describing the size distribution of the application in Mb (Megabytes)
    # 응용 프로그램의 크기 분포를 Mb (메가 바이트) 단위로 설명하는 히스토그램을 만듭니다.
    # The formed histogram is divided into 100 bins
    # 형성된 히스토그램은 100 개의 빈으로 나뉩니다.
    X=(df2.Size/1000000).values
    fig = plt.figure(figsize=(5,5))
    fig.add_subplot()
    plt.hist(X,bins=100, density=True,  alpha=0.75)
    plt.xlabel('Size')
    plt.ylabel('Frequency')
    plt.savefig('hist_size.png',bbox_inches="tight")

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result3 = str(figdata_png)[2:-1]

    ## Create a plot that displays insight into the data
    ## 데이터에 대한 통찰력을 표시하는 플롯 만들기
    top5 = df2.groupby(['Genres']).agg({'App':'count'}).reset_index().sort_values('App',ascending=False).head(5).Genres.to_list()
    baru = df2.copy()
    baru.Genres = pd.Categorical(baru.Genres,categories=top5,ordered=True)
    com = pd.pivot_table(
        data = baru,
        index=['Genres','Type'],
        values='App',
        aggfunc='count'
        ).reset_index()
    com.Genres = com.Genres.str.cat(com.Type,sep = ', ')
    fig = plt.figure(figsize=(5,13))
    fig.add_subplot()
    plt.ylabel('Count')
    plt.xlabel('GenresType')
    plt.xticks(rotation=65)
    plt.bar(x=com.Genres, height=com.App,color=['blue','red','blue','red','blue','red','blue','red','blue','red'])
    plt.savefig('bar_com.png',bbox_inches="tight")

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result4 = str(figdata_png)[2:-1]

    # Add result plot result to render_template () function
   # render_template () 함수에 결과 플롯 결과 추가
    return render_template('index.html', stats=stats, result=result, result2=result2, result3=result3,result4=result4)

if __name__ == "__main__": 
    app.run(debug=True)
