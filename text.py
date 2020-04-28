import pag
import search
import add
import pag
import update
import dell

def main():
    obj = DBConnection.DBCont()

    while True:
        print("""
        1 查看学生信息
        2 录入学生信息
        3 删除学生信息
        4 修改学生信息
        5 查询学生信息
        """)
        choice = input("请选择: ").strip()
        if choice not in fun_dic: continue
        fun_dic[choice]()

fun_dic = {
    "1":pag,
    "2":add,
    "3":dell,
    "4":update,
    "5":search
}


if __name__ == '__main__':
    main()
