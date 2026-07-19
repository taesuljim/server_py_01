from lib import ui

def main():
    # ui.py에서 정의한 창 생성 함수 호출
    window = ui.create_main_window()
    
    # 메인 루프 실행
    window.mainloop()

if __name__ == "__main__":
    main()
