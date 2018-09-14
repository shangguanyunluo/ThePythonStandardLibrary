import os

print("-" * 20)
os.makedirs("test/multiple/levels")

fp = open("test/multiple/levels/file.txt", "w")
fp.write("hello world")
fp.close()

os.remove("test/multiple/levels/file.txt")
os.removedirs("test/multiple/levels")