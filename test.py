import datetime
import tkinter as tk

# 한국 시간과 인도 시간을 표시할 레이블을 생성합니다.
kr_time_label = tk.Label(text="한국 시간")
in_time_label = tk.Label(text="인도 시간")

# 한국 시간과 인도 시간을 업데이트하는 함수를 생성합니다.
def update_time():
    # 현재 시간을 가져옵니다.
    now = datetime.datetime.now()

    # 한국 시간과 인도 시간을 계산합니다.
    kr_time = now.strftime("%Y-%m-%d %H:%M")
    in_time = now + datetime.timedelta(hours=5, minutes=30)
    in_time = in_time.strftime("%Y-%m-%d %H:%M")

    # 한국 시간과 인도 시간을 레이블에 표시합니다.
    kr_time_label.config(text=kr_time)
    in_time_label.config(text=in_time)

# 프로그램 시작 시 한 번만 실행할 코드를 작성합니다.
update_time()

# 프로그램 창을 생성합니다.
root = tk.Tk()

# 한국 시간과 인도 시간 레이블을 창에 추가합니다.
kr_time_label.pack()
in_time_label.pack()

# 프로그램 창을 실행합니다.
root.mainloop()