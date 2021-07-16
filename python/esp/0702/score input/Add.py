from typing import Type


class Add:
    def __init__(self, stu_list):
        self.stu_list = stu_list

    def exe(self):
        item = []

        subjects = input('Subject:')
        for l in self.stu_list:
            if subjects in l:
                print("Subject had already been created")
                break
        else:
            while 1:
                try:
                    scores = float(input('Score:'))
                except:
                    print("Please enter scores in numbers")
                    continue
                else:
                    print("Add successfully")
                    break
            item = [subjects, scores]
            self.stu_list.append(item)
        return self.stu_list
