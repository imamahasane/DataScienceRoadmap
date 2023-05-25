
# f = open("/Users/imamahasan/DataScience/1_Python/funny.txt", "w")
# f.write(" I'm from Bangladesh")
# f.close()


# f = open("/Users/imamahasan/DataScience/1_Python/funny.txt", "r")
# print(f.read())
# f.close()


# f = open("/Users/imamahasan/DataScience/1_Python/funny.txt", "r")
# for line in f:
#     tokens = line.split(" ")
#     print(str(tokens))

# f.close()


# f = open("/Users/imamahasan/DataScience/1_Python/funny.txt", "r")
# for line in f:
#     tokens = line.split(" ")
#     print(len(tokens))

# f.close() 


f = open("/Users/imamahasan/DataScience/1_Python/funny.txt", "r")
f_out = open("/Users/imamahasan/DataScience/1_Python/funny_wc.txt", "w")
for line in f:
    tokens = line.split(" ")
    f_out.write(f"WordCount: {len(tokens)}, {line}")
f.close()
f_out.close()