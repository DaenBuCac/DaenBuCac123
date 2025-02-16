import pyautogui
import time

def find_fishing_spot():
    spot = pyautogui.locateOnScreen('fish_spot.png', confidence=0.8)
    if spot:
        print("Tìm thấy chỗ câu cá!")
        pyautogui.moveTo(spot.left + spot.width/2, spot.top + spot.height/2)
        pyautogui.click()

find_fishing_spot()

def cast_fishing_rod():
    pyautogui.keyDown('e')  # Giữ phím E để ném cần câu
    time.sleep(0.8)  # Chỉnh thời gian theo khoảng cách ném mong muốn
    pyautogui.keyUp('e')  # Nhả phím E

cast_fishing_rod()

def detect_fish_bite():
    while True:
        bite = pyautogui.locateOnScreen('fish_bite.png', confidence=0.8)
        if bite:
            print("Cá cắn câu!")
            pyautogui.press('e')  # Giật cần
            break
        time.sleep(0.1)  # Kiểm tra liên tục

detect_fish_bite()

def sell_fish():
    npc = pyautogui.locateOnScreen('npc_fish.png', confidence=0.8)
    if npc:
        pyautogui.moveTo(npc.left + npc.width/2, npc.top + npc.height/2)
        pyautogui.click()
        time.sleep(2)  # Đợi menu mở ra
        pyautogui.click(x=600, y=400)  # Nhấp vào nút Sell

sell_fish()

while True:
    find_fishing_spot()
    cast_fishing_rod()
    detect_fish_bite()
    sell_fish()
    time.sleep(2)  # Nghỉ 2 giây rồi tiếp tục
