class Delete:
    def __init__(self, stu_list):
        self.stu_list = stu_list

    def exe(self):
        print(self.stu_list)
        subject = input('Please select Subject:')
        for l in self.stu_list:
            if subject in l:
                self.stu_list.remove(l)
                print("Delete successfully")
                break
        else:
            print("Subject not found")
        return self.stu_list
