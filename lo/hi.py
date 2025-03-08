import pyautogui, pyperclip, time

string = input("Nhập một chuỗi: ")
amount = int(input("Nhập số lần gửi: "))
delay = int(input("Nhập thời gian delay: "))

print("Đặt chuột vào vị trí muốn spam gửi tin nhắn.(10s đếm ngược!)")
for i in range(5,0,-1):
    print(i,end=" ", flush=True)
    time.sleep(1)
print("Done!")

for i in range(amount):
    pyperclip.copy(string)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(delay)
pyautogui.alert("Done!")
