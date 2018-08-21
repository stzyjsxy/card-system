# 建立一个名片列表
card_list = []

def new_card():
    """
新建一个名片记录
    """
    print("=" * 50)
    print("新建名片会话：")
    print("")
    name_str = input("请输入姓名：")
    phono_int = input("请输入电话号码：")
    qq_int= input("请输入QQ号码：")
    print("=" * 50)
    card_dict = {"name":name_str,
                "phono":phono_int,
                "qq":qq_int}
    card_list.append(card_dict)         # 添加进名片列表中
    print("保存名片成功！")
    print("%s\t\t%s\t\t%s" % (name_str,phono_int,qq_int))

def show_all():
    """
显示所有名片
    """
    print("=" * 50)
    print("显示全部会话：")
    print("")
    if len(card_list) > 0:
        for name in ["姓名","电话","QQ"]:
            print(name,end="\t\t")
        print("")
        for card_dir in card_list:
            print("%s\t\t%s\t\t%s" % (card_dir["name"],
                                      card_dir["phono"],
                                      card_dir["qq"]))
    else:
        print("无内容！请先建立新名片！")
    print("=" * 50)

def find_person():
    """
查询名片
    """
    find_name = input("请输入姓名：")
    for card_dir in card_list:      # 遍历列表中的字典
        if card_dir["name"] == find_name:       # 判断用户输入的名字是否在列表的字典中
            print("=" * 50)
            print("查询结果：")
            for name in ["姓名","电话","QQ"]:
                print(name,end="\t\t")      # 单行输出
            print("")                       # 换行
            print("%s\t\t%s\t\t%s" % (card_dir["name"],         # 输出列表中符合的字典
                                          card_dir["phono"],
                                          card_dir["qq"]))
            print("")
            chage(card_dir)         # 修改名片
            print("=" * 50)
            break
    else:
        print("查无此人！")

def chage(card_dir):
    """
修改名片：对查找到的字典进行操作
    :param card_dir: 查找到的字典
    """
    pop = input("可执行的操作： [1].修改/[2].删除/[0].返回菜单\n")
    print("")
    if pop == "1":
        card_dir["name"] = card_info(card_dir["name"],"修改姓名：")
        card_dir["phono"] = card_info(card_dir["phono"],"电话：")
        card_dir["qq"] = card_info(card_dir["qq"],"QQ:")
        print("修改成功！")
    elif pop == "2":
        card_list.remove(card_dir)
        print("删除成功！")

def card_info(value,new):
    """
判断用户输入的内容是否为空，如果为空返回原来的值，如果不为空就添加新的值
    :param value: 用户原先的值
    :param new: 用户新输入的值
    :return:
    """
    result = input(new)
    if len(result) > 0:
        return result
    else:
        return value
