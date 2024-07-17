# [Binary Classification of Insurance Cross Selling](https://www.kaggle.com/competitions/playground-series-s4e7)

## EDA
- Data Preprocessing
  - null 처리 
  - outliers 이상치 처리 (boxplot, distplot 활용)
  - 무한 값(inf) 치환
- Feature 시각화
	- distplot
	- boxplot 
	- scatterplot
	- catplot
- Feature 카테고리화
	- Age → youngAge, middleAge, oldAge 분류 
	- Region_Code → Region_A, Region_B, Region_C 분류
	- policy_sales_channel
	- vehicle_damage
	- annual_premium 
- Numerical Features 와 Non Numerical Features 분리 
	- Non Numerical Features → Numeric 값으로 인코딩
- Target Variable (Response) 시각화
	- countplot, counts 등
- Features 와 Target Variable 간 상관관계 파악
	- 중요한 영향을 주는 Feature 순위 파악 

## Feature Selection

- 참고) Kendall's rank correlation 

## Model Fitting

- Decision tree Classifier
- AdaBoost
- LightGBM
- BaggingRegressor
- NaiveBayes 
- Logistic regression

## Reference
- https://github.com/ankit986/HEALTH-INSURANCE-CROSS-SELL-PREDICTION?tab=readme-ov-file#project-outline
