class Show:
    def __init__(self, stu_list):
        self.stu_list = stu_list

    def exe(self):
        print('================')
        for l in self.stu_list:
            print("{}:{}".format(l[0], l[1]))
        print('================')
        return self.stu_list
