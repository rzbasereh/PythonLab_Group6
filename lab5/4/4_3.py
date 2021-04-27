with open("text.txt",mode="r+") as file:
    file_list = file.readlines()
    file_reverse = []

    for line in file_list:
        m = line.split(":")
        m_reverse = [m[1][:-2], m[0]]
        m_join = ":".join(m_reverse)
        file_reverse.append(m_join)

    file_reverse = "\n".join(file_reverse)

with open("text_reverse.txt",mode="w") as text_reverse:
    text_reverse.write(file_reverse)
