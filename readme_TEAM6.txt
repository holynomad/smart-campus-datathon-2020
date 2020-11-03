#================= 2020 KU 스마트 캠퍼스 데이터톤 6조 [SKUM - Safe Korea Univ. Map, "스쿰"] readme_TEAM6.txt ====================
#================= ★★ 주의 ★★ readme 목록 중 public 공개가 어려운 부분은 제외됨 

# !먼저 [00.readme_TEAM6]의 TEAM6_OUTPUT_DIR_STRUCTURE.png 파일을 보고 전체적인 산출물 스트럭처를 살펴봅니다.

# 폴더별 상세 산출물 구성은 아래와 같습니다.

	[01.실외 공기질 데이터셋 크롤링(API)]
	
		[A.기상청 동네예보조회(API)]
		
			기상청18_동네예보 조회서비스_오픈API활용가이드.docx - 기상청에서 제공한 오픈API 가이드북
			airAPI.py - 기상청 데이터 API 크롤링 소스(Python)
			air_output_sample_10000row.csv - 크롤링 결과파일(7/30 이전 3개월치)
		
		[B.한국환경공단 대기오염정보(API)]
		
			airkorea_openapi_guide-v1_7_2.docx - 한국환경공단에서 제공하는 실외대기오염 데이터 오픈API 가이드북
			weatherAPI.py - 실외대기오염 데이터 API 크롤링 소스(Python)	
	
	[02.데이터전처리 및 통합데이터셋 구축]
	
		[A.IoT 데이터셋 변환(txt2csv)]
		
			txt2csv.py - 데이터톤 집행부에서 제공해준 SK미래관 IoT센서 수집정보 Text-to-CSV 변환 소스(Python)
			그 외 Input (TXT) & Output 파일(CSV)
		
		[B.SK미래관 층별 룸별사이즈 추출 및 재실Capa라벨링]
		
			skf_area_tot.csv - SK미래관 층별 룸별 도면에서 룸별-Size정보 추출/요약한 데이터셋
			label_capaNpcnt_iot_n_airinfo_200812.R - 위 데이터셋과 [02-A]단계에서 변환된 IoT 데이터셋(CSV)을 roomid로 병합하고 가상 재실인원(personCnt) 라벨링 소스(R)
			area_pcnt_rnorm_merged_20200618_v1.1.csv 외 2건 - 해당 결과파일
			
		[C.실내(IoT)+실외(API) 통합데이터셋 구축]
		
			merge_iot_n_airinfo_200805.R - [02-B]단계에서 생성된 IoT 데이터셋과 [01]단계에서 진행한 실외대기오염 데이터셋(API) 병합 소스(R)
			iot_air_merged_20200611.csv 외 3건 - 위 소스 결과파일
			merge_all_linked_200820.R - 각 일자별 데이터셋(CSV)을 하나의 파일로 병합한 소스(R)
			iot_allmerged_0618_0702.csv - 위 소스 결과파일
			
		[D.탐색적 데이터 분석]
		
			EDA.R - 실내+실외 통합데이터셋 기반 탐색적데이터분석 실시한 소스(R)
	
	[03.가상 DR시나리오 라벨링 및 시각화]
	
		[A.SK미래관 건물 도면이미지]
		
			데이터톤 집행부에서 제공해준 SK미래관 층별(B1F~5F) 룸별 도면정보(PDF)
			SKUM_COVID위험도_UI예시.png - 위 도면이미지 분석을 바탕으로 SKUM UI 예시 이미지
			 
		[B.가상 DR 시나리오 케이스 라벨링]
		
			라벨링 기준_20200820_heatmap위한 5단계.xlsx - 가상 DR 시나리오 케이스별 라벨링 기준 자체분석표
			label_all_Y_merged_200826.R - 위 기준에 맞춰 진행한 가상 DR 시나리오별 라벨링 소스(R)
			labelled_all_merged_0618_0702_v1.0.csv - 위 소스를 바탕으로 6/18~7/2 실내(IoT)+실외(API) 통합 데이터셋 라벨링 결과파일
			
		[C.시각화(Heatmap + 2D Gaussian)]
		
			heatmap_01.py - 특정 feature별 (예: dust, temp, humid, covid_case등) 룸별(roomid) 시계열 시각화(heatmap, Python)
			Figure_1_COVID Risk TimeSeries Map_0625~0702_marked.png - heatmap_01.py 통해 COVID 감염위험도(covid_case) 룸별-시계열 heatmap 결과예시 이미지
			heatmap_02.py - SK미래관 2F 도면이미지를 오픈한 후 특정 룸별(roomid) 특정 가상 DR 시나리오 feature (예: covid_case, di_case, complx_case 등)별 2D Gaussian 시각화 적용 소스(Python)
			2F.png - SK미래관 2F 도면 이미지
			Figure_2_SKF_2F_COVID_RISK_MAP(sample).png - SK미래관 2F 특정 스터디룸의 COVID 감염위험도 시각화 샘플 이미지
			Figure_3_SKF_2F_COMPLX_RISK_MAP(sample).png - SK미래관 2F 특정 스터디룸의 COVID 밀집도 시각화 샘플 이미지
			Figure_4_SKF_2F_DI_MAP(sample).png - SK미래관 2F 특정 스터디룸의 불쾌지수(불쾌도) 시각화 샘플 이미지
			heatmap_03.py - 위 heatmap_02.py를 자동 애니메이션으로 시계열 시각화 구현하기 위한 소스(미완성, Python)
			Figure_5_COVID_Virtual labelled Dataset.png - heatmap_02.py 및 heatmap_03.py에서 2D Gaussian 시각화를 위해 사용한 샘플데이터셋 구간캡쳐 이미지
			
	[04.SKUM앱 프로토타이핑]
	
		SKUM UI Flow_v2_20200823.pptx - SKUM앱 기획시 작성한 UX 가이드라인에 맞춰 디자인한 앱 UI flow
		SKUM Prototype_v1.0.mp4 - 위 UI flow를 바탕으로 만들어 본 SKUM 앱 데모영상(약1분30초, Adobe Xd)
		SKUM LivingLab Prototype v1.0.mp4 - 디지털트윈 재난대응(DR) 리빙랩 구축을 위한 SKUM 리빙랩 앱 데모영상(약1분30초, Adobe Xd)
	
	[99.분석모델링 참조 페이퍼]
	
		공기질 분석 및 가상 DR 시나리오 (COVID 감염위험, 화재위험, 밀집도위험 등) 라벨링 위해 참고한 자료들(PDF)
	
