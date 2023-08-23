import tkinter as tk
from tkinter import messagebox

def select_free_talk_winner(participants, last_free_talk_winner):
    # Free Talk 참석자 중에 지난번 당첨자를 제외한 후보들
    candidates = [p for p in participants if p != last_free_talk_winner]
    
    # TODO: 후보들 중에 다음달 당첨자 선정 로직 추가
    
    return selected_winner

def select_cake_recipients(participants, last_free_talk_winner, last_cake_recipients):
    # 롤케익 당첨자 후보들 중에 지난번 당첨자들을 제외
    candidates = [p for p in participants if p != last_free_talk_winner and p not in last_cake_recipients]
    
    # TODO: 후보들 중에 이번달 롤케익 당첨자들 선정 로직 추가
    
    return selected_recipients

def submit():
    participants = entry_participants.get().split(',')
    last_free_talk_winner = entry_last_free_talk_winner.get()
    last_cake_recipients = entry_last_cake_recipients.get().split(',')
    
    free_talk_winner = select_free_talk_winner(participants, last_free_talk_winner)
    cake_recipients = select_cake_recipients(participants, free_talk_winner, last_cake_recipients)
    
    messagebox.showinfo("Results", f"Free Talk Winner: {free_talk_winner}\nCake Recipients: {', '.join(cake_recipients)}")

# GUI 생성
root = tk.Tk()
root.title("Event Winners Selection")

label_participants = tk.Label(root, text="Participants (comma-separated):")
entry_participants = tk.Entry(root)

label_last_free_talk_winner = tk.Label(root, text="Last Free Talk Winner:")
entry_last_free_talk_winner = tk.Entry(root)

label_last_cake_recipients = tk.Label(root, text="Last Cake Recipients (comma-separated):")
entry_last_cake_recipients = tk.Entry(root)

button_submit = tk.Button(root, text="Submit", command=submit)

# 위젯 배치
label_participants.pack()
entry_participants.pack()

label_last_free_talk_winner.pack()
entry_last_free_talk_winner.pack()

label_last_cake_recipients.pack()
entry_last_cake_recipients.pack()

button_submit.pack()

# GUI 실행
root.mainloop()
