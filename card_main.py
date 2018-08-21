import card_tool

while True:
    # 显示菜单
    #使用列表存储一个菜单内容
    menu_bar = ["*" * 30,
                "[欢迎使用名片管理系统] V1.0","",
                "1. 新建名片",
                "2. 显示全部",
                "3. 查询名片","",
                "0. 退出系统",
                "*" * 30]
#遍历菜单列表，显示菜单内容
    for menu in menu_bar:
        print(menu)
#提示用户输入选择功能
    num = str(input("请输入要执行的功能："))
    if num not in ["1","2","3","0"]:
        print("输入有误，请重新输入！")
        input("\t\t0.返回菜单")
    elif num == "1":
        card_tool.new_card()
    elif num == "2":
        card_tool.show_all()
    elif num == "3":
        card_tool.find_person()
    elif num == "0":
        break
