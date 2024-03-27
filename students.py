import numpy as np
import random


class StudentData:
    def __init__(self, num_students, subjects=list):
        self.first_names = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ', 'კლარა', 'სიმონ',
                            'ანზორ', 'სოფია', 'სოსო', 'ნელი', 'ბონდო', 'ედუარდ', 'სონია', 'არჩილ', 'მარიამ', 'სოფია',
                            'ემა', 'იზოლდა', 'ომარ', 'ტატიანა', 'ვიქტორ', 'კარინე', 'გუგული', 'კახა', 'როზა', 'რუსუდან',
                            'სიმონ', 'ნელი', 'ბადრი', 'მადონა', 'ირინე', 'მინდია', 'ნათია', 'გულნარა', 'კახა', 'ელზა',
                            'როინ', 'ნაირა', 'ლიანა', 'ნინელი', 'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა', 'გოჩა', 'მურმან']
        self.last_names = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი', 'ბუჩუკური',
                           'ტყებუჩავა', 'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა',
                           'ნაკაშიძე', 'ღურწკაია', 'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე', 'ხვიჩია',
                           'ბასილაშვილი', 'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე', 'ხარაბაძე', 'მუსაევა', 'მამულაშვილი',
                           'ელიზბარაშვილი', 'მამულაშვილი', 'ჯოჯუა', 'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე',
                           'ბერიანიძე', 'ჯოხაძე', 'სამხარაძე', 'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე',
                           'ინასარიძე', 'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა', 'რევაზიშვილი']
        self.num_students = num_students
        self.subjects = subjects
        self.num_subjects = len(self.subjects)
        self.data = self.generate_data()

    def __str__(self):
        output = ""
        for row in self.data:
            output += ", ".join(str(item) for item in row) + "\n"
        return output

    def generate_data(self):
        name = [f"{random.choice(self.first_names)} {random.choice(self.last_names)}" for _ in range(self.num_students)]
        data = np.random.randint(1, 101, size=(len(name), len(self.subjects)))
        subjects_table = np.array(self.subjects).reshape(1, len(self.subjects))
        names_table = np.array(name).reshape(len(name), 1)
        table_header = np.hstack(([["Student"]], subjects_table))
        return np.vstack((table_header, np.hstack((names_table, data))))

    def highest_avg_score(self):
        scores = self.data[1:, 1:].astype(int)
        averages = np.mean(scores, axis=1)
        max_avg = np.max(averages)
        max_avg_student = self.data[np.argmax(averages) + 1][0]
        return max_avg_student, max_avg

    def highest_and_lowest_math_scores(self):
        math_scores = self.data[1:, self.subjects.index("Mathematics") + 1].astype(int)
        max_math_score = np.max(math_scores)
        max_math_index = np.argmax(math_scores) + 1
        min_math_score = np.min(math_scores)
        min_math_index = np.argmin(math_scores) + 1
        return [self.data[max_math_index, 0], max_math_score], [self.data[min_math_index, 0], min_math_score]

    def english_above_average(self):
        english_scores = self.data[1:, self.subjects.index("English") + 1].astype(int)
        avg_english_score = np.mean(english_scores)
        above_avg_indices = np.where(english_scores > avg_english_score)[0]
        above_avg_students = [(self.data[idx + 1, 0], english_scores[idx]) for idx in above_avg_indices]
        return above_avg_students

    def avg_on_subject(self, subject_name):
        subject_index = self.subjects.index(subject_name) + 1
        scores = self.data[1:, subject_index].astype(int)
        avg_score = np.mean(scores)
        max_avg = np.max(avg_score)
        max_avg_student = self.data[np.argmax(avg_score) + 1][0]
        return max_avg_student, max_avg
