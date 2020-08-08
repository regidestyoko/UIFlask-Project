# Google Play Store Analytics
<img src="https://raw.githubusercontent.com/fafilia/capstone-UIFlask/master/full_capstone.png">

## Introduction
이 프로젝트는 알고리즘 팀과의 협력입니다. 이 프로젝트의 목표는 Flask 프레임 워크를 사용하여 간단한 웹 애플리케이션 (대시 보드)을 빌드하는 것입니다. 이 프로젝트는 Flask 사용자 인터페이스의 모양에 중점을 둘 것입니다.

## Data Summary
이 프로젝트에 사용 된 데이터는 Google Playstore 앱에서 데이터를 스크랩합니다. Google Playstore 앱 데이터는 다음 세부 정보가 포함 된 여러 변수로 구성됩니다.

- `App`: 응용 프로그램 이름
- `Category`: 애플리케이션 카테고리
- `Rating`: 애플리케이션 사용자가 제공 한 전체 등급 (스크랩시)
- `Reviews`: 애플리케이션 사용자가 제공 한 리뷰 수 (스크랩 한 경우)
- `Size`: 응용 프로그램 크기 (스크랩시)
- `Installs`: 애플리케이션을 설치 / 다운로드 한 사용자 수 (스크랩시)
- `Type`: 신청 유형 (유료 / 무료)
- `Price`: 애플리케이션 가격 (스크랩시)
- `Content Rating`: 이 앱의 연령대를 타겟팅합니다-어린이 / 만 21 세 이상 / 성인
- `Genres`: 응용 장르.
- `Last Updated`: Play 스토어에서 애플리케이션이 마지막으로 업데이트 된 날짜 (스크랩 한 경우)
- `Current Ver`: Playstore에서 사용할 수있는 앱의 현재 버전 (스크랩 한 경우)
- `Android Ver`: 필요한 최소 Android 버전 (스크랩시)

## Dependencies
- Flask
- Matplotlib
- Pandas
- Numpy

이러한 모든 모듈은 다음을 통해 설치할 수 있습니다.
```
pip install -r requirements.txt
```

### 1. Preprocessed Data and Exploratory Data Analysis
이 전처리 단계에서 중복 데이터 제거, 데이터 유형 변경 및 데이터 값 수정과 같은 전처리 데이터를 완료하라는 메시지가 표시됩니다.

### 2. Data Wrangling
- 이 단계에서 데이터를 그룹화하고 집계합니다. 데이터 랭 글링은 요청 된 분석에 따라 올바른 데이터를 준비하는 데 사용됩니다. 예시로`stats` 객체에는 아래와 같이 데이터 테이블을 생성하기 위해 그룹화 및 집계를 통해 데이터를 처리하는 변수`rev_tablel`이 있습니다. :

    <img src="https://raw.githubusercontent.com/fafilia/capstone-UIFlask/master/table_rev.PNG" width=400>

### 3. Data Visualization
- Google Playstore에서 상위 5 개 카테고리를 나타내는 플롯 바를 생성하거나 복제합니다.
-리뷰, 평가 및 설치된 애플리케이션 수를 기반으로 애플리케이션 배포를 설명하는 산점도를 생성하거나 복제합니다.
-응용 프로그램 크기 분포를보기 위해 플롯 히스토그램 생성 또는 복제


### 4. Build Flask App
Flask 애플리케이션에서 이러한 플롯을 렌더링하고 html 템플릿 / 페이지에 표시하는 방법을 보여줍니다. 주목할만한 것은`app.py` 섹션입니다.
```
render_templates(__________)
```
`templates / index.html`에서 플롯 이미지를 저장할 소스 plot.png를 호출해야합니다.
```
<img src="________________________" height="450" width=500>
```

NB : Those translation was developed by google, apologize for inconvenience sentences

그 번역은 구글에서 개발했습니다. 불편한 문장에 대해 사과드립니다.
