from pandas import read_csv;

# get all answers
def get_answer(fileName):
    # 打开输入文件（格式需为UTF-8）并传入db变量方便后续处理
    inFile = open(fileName, 'r', encoding="utf-8")
    db = inFile.read()
    inFile.close()
    # 打开输出文件
    outFile = open("outFile.csv", 'w', encoding="utf-8")
    # 将db中的","替换为换行\n
    outFile.write(db.replace('\",\"', '\n'))
    outFile.close()


# delete the same answers
def delete_SameAnswer(fileName):
    df = read_csv(fileName)
    answerBook = df.drop_duplicates();
    outFile = open("answerBook.csv", 'w', encoding="utf-8")
    # 将db中的","替换为换行\n
    outFile.write(answerBook)
    outFile.close()

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    get_answer("allAnswers.txt")
