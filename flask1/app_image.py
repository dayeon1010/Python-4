from flask import Flask, render_template

app = Flask(__name__)

# 이미지 파일과 설명을 포함하는 리스트 (static 폴더 내의 상대 경로로 지정)
image_files = [
    {"path": "images_1.jpg", "description": "강얼쥐"},
    {"path": "images_2.jpg", "description": "강알쥐"},
    {"path": "images_3.jpg", "description": "강쥐"},
    {"path": "images_4.jpg", "description": "모르쥐"},
    {"path": "images_5.jpg", "description": "나누구쥐"},
    {"path": "images_6.jpg", "description": "난"}
    # 추가 이미지 파일들
]

@app.route('/')
def index():
    return render_template('index.html', image_files=image_files)

if __name__ == '__main__':
    app.run(debug=True)
