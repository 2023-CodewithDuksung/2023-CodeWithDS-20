from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from konlpy.tag import Okt

# Okt 형태소 분석기 인스턴스 생성
okt = Okt()

# 불용어 리스트
stopwords = ["의", "는", "을", "를", "이", "가", "은", "와", "과", "도", "로", "에", "저", "그", "입니다", "하다"]

# 토큰화 및 불용어 제거
def preprocessing(text):
    tokens = okt.morphs(text)
    tokens = [word for word in tokens if word not in stopwords]
    return " ".join(tokens)

# 모든 강의 데이터
all_lecture_descriptions = [
    preprocessing("예술은 인간의 삶을 아름답게 만듭니다."),
    preprocessing("디자인은 좋은 예술의 핵심 요소입니다."),
    preprocessing("컴퓨터 과학에 대한 기본 개념 소개"),
    # ... 추가적인 강의 설명 ...
]

# TF-IDF 벡터라이저 생성 및 모든 강의 설명에 적용
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(all_lecture_descriptions)

# K-Means 클러스터링
num_clusters = 3  # 예시로 3개의 클러스터 사용
km = KMeans(n_clusters=num_clusters)
km.fit(tfidf_matrix)
clusters = km.labels_.tolist()

# 사용자가 들은 강의
user_lectures = [
    preprocessing("예술에 대한 깊은 탐구"),
    # ... 사용자가 들은 추가 강의 ...
]

# 사용자 강의의 클러스터 파악
user_tfidf = tfidf_vectorizer.transform(user_lectures)
user_clusters = km.predict(user_tfidf)

# 사용자가 듣지 않은 클러스터의 강의 추천
recommendations = []

for i, cluster in enumerate(clusters):
    if cluster not in user_clusters:
        recommendations.append(all_lecture_descriptions[i])

print("추천 강의:")
for rec in recommendations:
    print(rec)
