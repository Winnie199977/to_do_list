to_do_list = []

def show_menu():
    print("\n代辦事項清單應用程式")
    print("1. 查看待辦事項")
    print("2. 新增待辦事項")
    print("3. 刪除待辦事項")
    print("4. 退出程式")

def view_tasks():
    if not to_do_list:
        print("目前沒有待辦事項。")
    else:
        for idx, task in enumerate(to_do_list, start=1):
            print(f"{idx}. {task}")


def add_task():
    task = input("請輸入新的待辦事項:")
    to_do_list.append(task)
    print(f"待辦事項「{task}」已新增")

def delete_task():
    view_tasks()
    if to_do_list:
        try:
            task_num = int(input("請輸入要刪除的待辦事項編號: "))
            if 1 <= task_num <= len(to_do_list):
                removed_task = to_do_list.pop(task_num-1)
                print(f"待辦事項「{removed_task}」已刪除")
            else:
                print("無效的編號")
        except ValueError:
            print("請輸入有效的數字")

def main():
    while True:
        show_menu()
        choice = input("請操作(1-4) : ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("再見")
            break
        else:
            print("無效的選擇，請重新輸入")

if __name__ == "__main__":
    main()