# 파일명은 확장자 없이 Dockerfile

# base 이미지 선택
FROM python:3.6

# 학습 코드 파일을 Docker 이미지에 포함
COPY ./pytorch_classifier.py /

# requirements 파일을 Docker 이미지에 포함
COPY ./requirements.txt /

# requirements 파일을 이용하여 학습 코드 실행에 필요한 파이썬 라이브러리 설치
RUN pip install -r requirements.txt

# 학습 코드 파일 실행 구문
ENTRYPOINT ["python","pytorch_classifier.py"]