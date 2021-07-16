from Add import Add


class Modify:
    def __init__(self, stu_list):
        self.stu_list = stu_list

    def exe(self):
        print(self.stu_list)
        subject = input('Please select Subject:')
        for l in self.stu_list:
            if subject in l:
                scores = float(input('Score:'))
                l[1] = scores
                print("Modify successfully")
                break
        else:
            create = input("Subject not found, create a new one? (Y/N)")
            if create.lower() == "y":
                self.stu_list = Add(self.stu_list).exe()

        return self.stu_list
