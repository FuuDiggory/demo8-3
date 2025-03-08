from docx import Document

def read_questions_answers(file_path):
    doc = Document(file_path)
    questions_answers = []
    current_question = None

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            if text[0].isdigit() and '.' in text:  # Dòng câu hỏi
                if current_question:
                    questions_answers.append(current_question)
                current_question = {'question': text, 'options': []}
            elif text[0] in 'ABCD':  # Dòng đáp án
                if current_question:
                    current_question['options'].append(text)
    
    if current_question:  # Đưa câu cuối vào danh sách
        questions_answers.append(current_question)
    
    return questions_answers

file_path = "/mnt/data/Trắc nghiệm giữa kì lớp 11.docx"  # Đường dẫn đến file của bạn
questions_answers = read_questions_answers(file_path)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Thay đường dẫn đến ChromeDriver của bạn
driver.get("URL của trang web Shub")  # URL của bài kiểm tra trên Shub

# Đăng nhập (nếu cần thiết)
username = driver.find_element(By.ID, "username")  # Tìm đúng trường ID trên trang web
password = driver.find_element(By.ID, "password")
username.send_keys("your_username")
password.send_keys("your_password")
password.submit()

time.sleep(2)  # Chờ trang tải

# Duyệt qua từng câu hỏi và điền đáp án
delay = 180 / len(questions_answers)  # Điều chỉnh thời gian cho 3 phút
for qa in questions_answers:
    question_text = qa['question']
    options = qa['options']
    
    # Xác định câu hỏi và đáp án đúng (giả sử bạn biết đáp án đúng là 'B')
    correct_option = next((opt for opt in options if "đúng" in opt.lower()), options[0])  # Lọc dựa trên file
    
    # Tìm và chọn câu trả lời trên Shub
    question_element = driver.find_element(By.XPATH, f"//p[contains(text(), '{question_text[:30]}')]")  # Điều chỉnh XPATH nếu cần
    correct_option_element = question_element.find_element(By.XPATH, f"//label[contains(text(), '{correct_option[0]}')]")
    correct_option_element.click()

    time.sleep(delay)

# Nộp bài
submit_button = driver.find_element(By.ID, "submit_button_id")  # Điều chỉnh ID của nút "Nộp bài"
submit_button.click()

# Đóng trình duyệt sau khi hoàn thành
time.sleep(5)
driver.quit()


