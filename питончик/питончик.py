num1 = float(input("����� 1: "))
num2 = float(input("����� 2: "))
operation = input('''
�������� ��������:
+ ��������
- ���������
* ���������
/ �������
''')

if operation == '+':
    print("���������", num1 + num2)
elif operation == '-':
    print("���������", num1 - num2)
elif operation == '*':
    print("���������", num1 * num2)
elif operation == '/':
    if num2 == 0:
        print("������� �� ���� ���������")
    else:
        print("���������", num1 / num2)
else:
    print('������� ����������� ��������')