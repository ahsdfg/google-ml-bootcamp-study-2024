# [Health Insurance Cross Sell Prediction Data](https://www.kaggle.com/datasets/annantkumarsingh/health-insurance-cross-sell-prediction-data/data)

## [Data Description](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction/data)
- 차량 보험에 관심이 있는 사람과 관련된 인구통계(성별, 연령, 지역 코드 유형), 차량(차령, 손상), 정책(보험료, 소싱 채널) 등의 정보 포함 
- `381109` 개의 데이터

### Train Data
| Feature Name | Type | Description |
|----|----|----|
|id| (continuous) | 고객 식별자 |
|Age| (continuous) | 고객 나이 |
|Gender| (dichotomous) | 고객 성별(Male/Female) |
|Driving_License| (dichotomous) | 면허증 없으면 0, 있으면 1 |
|Region_Code| (nominal) | 고객 지역의 고유 코드 |
|Previous_Insured| (dichotomous) | 차량 보험이 없으면 0, 있으면 1 |
|Vehicle_Age| (nominal) | 차량 연식 |
|Vehicle_Damage| (dichotomous) | 과거 파손 이력이 없으면 No, 있으면 Yes |
|Annual_Premium| (continuous) | 연간 지불 보험료 |
|Policy_Sales_Channel| (nominal) | 고객 소통 채널의 익명 코드(예: 다른 상담원, 우편, 전화, 직접 방문 등) |
|Vintage| (continuous) | 고객, 회사 간 관계 유지 일수 |
|**Response(Dependent Feature)**| (dichotomous) | 관심 없으면 0, 있으면 1 |

### Test Data
| Feature Name | Type | Description |
|----|----|----|
|id| (continuous) | 고객 식별자 |
|Age| (continuous) | 고객 나이 |
|Gender| (dichotomous) | 고객 성별(Male/Female) |
|Driving_License| (dichotomous) | 면허증 없으면 0, 있으면 1 |
|Region_Code| (nominal) | 고객 지역의 고유 코드 |
|Previous_Insured| (dichotomous) | 차량 보험이 없으면 0, 있으면 1 |
|Vehicle_Age| (nominal) | 차량 연식 |
|Vehicle_Damage| (dichotomous) | 과거 파손 이력이 없으면 No, 있으면 Yes |
|Annual_Premium| (continuous) | 연간 지불 보험료 |
|Policy_Sales_Channel| (nominal) | 고객 소통 채널의 익명 코드(예: 다른 상담원, 우편, 전화, 직접 방문 등) |
|Vintage| (continuous) | 고객, 회사 간 관계 유지 일수 |

### Submission
| Feature Name | Type | Description |
|----|----|----|
|id| (continuous) | 고객 식별자 |
|**Response(Dependent Feature)**| (dichotomous) | 관심 없으면 0, 있으면 1 |
