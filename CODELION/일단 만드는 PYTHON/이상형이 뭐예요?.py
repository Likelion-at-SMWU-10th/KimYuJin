total_list = []

while True:
    question = input("������ �Է����ּ��� : ")
    if question == "q":
        break
    else:
        total_list.append({"����" : question, "�亯" : ""})

for i in total_list:
    print(i["����"])
    answer = input("�亯�� �Է����ּ��� : ")
    i["�亯"] = answer

print(total_list)