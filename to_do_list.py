import os
import json
from datetime import datetime

to_do_list = []
# 說明
def show_menu():
    print("\n代辦事項清單應用程式")
    print("1. 查看待辦事項")
    print("2. 新增待辦事項")
    print("3. 刪除待辦事項")
    print("4. 修改待辦事項")
    print("5. 退出程式")

# 查詢
def view_tasks():
    if not to_do_list:
        print("目前沒有待辦事項。")
    else:
        for idx, task in enumerate(to_do_list, start=1):
            deadline = task.get("deadline", "無")
            print(f"{idx}. {task['name']} (截止日期: {deadline})")

# 新增
def add_task():
    task_name = input("請輸入新的待辦事項:")
    deadline_input = input("請輸入截止日期 (格式:YYYY-MM-DD，或按 Enter 跳過): ")
    deadline = None
    if deadline_input:
        try:
            deadline = datetime.strptime(deadline_input, "%Y-%m-%d").date().isoformat()
        except ValueError:
            print("無效的日期格式，將不設置截止日期。")
    
    task = {"name": task_name, "deadline": deadline}

    to_do_list.append(task)
    print(f"待辦事項「{task_name}」已新增")
    write_to_file() # 新增後保存

# 刪除
def delete_task():
    view_tasks()
    if to_do_list:
        try:
            task_num = int(input("請輸入要刪除的待辦事項編號: "))
            if 1 <= task_num <= len(to_do_list):
                removed_task = to_do_list.pop(task_num-1)
                print(f"待辦事項「{removed_task}」已刪除")
                write_to_file() # 刪除後保存
            else:
                print("無效的編號")
        except ValueError:
            print("請輸入有效的數字")

# 讀取數據
def read_from_file():
    if os.path.exists("to_do_list.json"):
        with open("to_do_list.json", "r") as file:
            global to_do_list
            to_do_list = json.load(file)

# 保存數據
def write_to_file():
    with open("to_do_list.json", "w") as file:
        json.dump(to_do_list, file, indent=4)#設置 indent=4 表示每一層嵌套會使用 4 個空格進行縮排。容易閱讀

# 修改數據
def modify_task():
    view_tasks()
    if to_do_list:
        try:
            task_num = int(input("請輸入要修改的代辦事項編號:"))
            if 1 <= task_num <= len(to_do_list):
                new_name = input(f"請輸入新的名稱(原來的名稱: {to_do_list[task_num-1]['name']}) : ")
                new_deadline_input = input("請輸入新的截止日期(格式:YYYY-MM-DD，或按 Enter 跳過) : ")
                new_deadline = None
                if new_deadline_input:
                    try:
                        new_deadline = datetime.strptime(new_deadline_input, "%Y-%m-%d").date().isoformat()
                    except ValueError:
                        print("無效的日期格式，將保留原來的截止日期")

                to_do_list[task_num-1]['name'] = new_name or to_do_list[task_num-1]['name']
                if new_deadline_input:
                    to_do_list[task_num-1]['deadline'] = new_deadline
                
                print(f"代辦事項「{to_do_list[task_num-1]['name']}」已修改")
                write_to_file()
            else:
                print("無效的編號")
        except ValueError:
            print("請輸入有效的數字")

# 主程式
def main():
    read_from_file()    # 程式啟動時讀取數據
    while True:
        show_menu()
        choice = input("請操作(1-5) : ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            modify_task()
        elif choice == '5':
            print("再見")
            break
        else:
            print("無效的選擇，請重新輸入")

if __name__ == "__main__":
    main()