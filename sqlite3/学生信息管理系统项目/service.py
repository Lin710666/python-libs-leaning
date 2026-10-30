import db

class info_sys:
    def __init__(self):
        db.init_db()

    def menu(self):
        print("*" * 30)
        print("欢迎使用学生信息管理系统")
        print("1. 添加学生信息")
        print("2. 查询学生信息")
        print("3. 修改学生信息")
        print("4. 删除学生信息")
        print("5. 查看所有学生信息")
        print("6. 退出系统")
        print("*" * 30)

    def add_stu(self, stu_id, name, age, gender, score):
        db.add_stu(stu_id, name, age, gender, score)

    def get_info(self, stu_id):
        return db.get_info(stu_id)

    def update_stu(self, stu_id, name=None, age=None, gender=None, score=None):
        db.update_stu(stu_id, name, age, gender, score)

    def del_stu(self, stu_id):
        db.del_stu(stu_id)

    def view_whole(self):
        db.view_whole()

    def run(self):
        while True:
            self.menu()
            usr_choice = input("请输入您的选择（1-6）：")
            if usr_choice == "1":
                stu_id = input("请输入学生学号：")
                name = input("请输入学生姓名：")
                age = int(input("请输入学生年龄："))
                gender = input("请输入学生性别：")
                score = int(input("请输入学生成绩："))
                self.add_stu(stu_id, name, age, gender, score)
            elif usr_choice == "2":
                stu_id = input("请输入学生学号：")
                info = self.get_info(stu_id)
                if info:
                    print(info)
                else:
                    print("未找到该学生信息")
            elif usr_choice == "3":
                stu_id = input("请输入学生学号：")
                name = input("请输入学生姓名（可选）：")
                age = input("请输入学生年龄（可选）：")
                gender = input("请输入学生性别（可选）：")
                score = input("请输入学生成绩（可选）：")
                self.update_stu(stu_id, name, age, gender, score)
            elif usr_choice == "4":
                stu_id = input("请输入学生学号：")
                self.del_stu(stu_id)
            elif usr_choice == "5":
                self.view_whole()
            elif usr_choice == "6":
                print("感谢使用学生信息管理系统！")
                break
            else:
                print("无效选择，请重新输入。")