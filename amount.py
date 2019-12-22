import time

s = []
sum1 = 0
x = 0
num = 0
# input name
def name():
    while True:
        ans = input("ニックネームを入力してください: ")
        if ans:
            print("あなたの名前は{}ですね".format(ans))
            break
        else:
            print("入力してください")

# input num
def add(x):
    x += int(num)

def loop():
    while True:
        num = input('数字を入力してください: ')
        if num == 'q':
            break
        else:
            try:
                s.append(int(num))
                add(x)
            except ValueError:
                print("")

if __name__ == '__main__':
    name()
    loop()

# amount
print("入力値:" + str(s))
while s:
    sum1 += s.pop()
print("合計:" + str(sum1))
# time
print("処理速度:" + str(time.time()) + "ms")
