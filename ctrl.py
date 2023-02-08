# ch 6.4.1 ctrl.py
class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):    # calculate 메서드 추가, 내용은 추후에 작성
        pass

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate) # 버튼1 연결을 변경
        self.view.btn2.clicked.connect(self.view.clearMessage)    # 버튼 2 핸들러 함수 연결

    def sum(self, a, b):    # 덧셈 함수 추가
        return a + b