from pathlib import Path

# Path类的cwd()方法
cwd = Path.cwd()
print(cwd)

# Path实例和一些方法

path = Path(__file__)
## Path的实例就是一个路径
print(path)

## .name属性
print(f"The name of the path: {path.name}")

## absolute()方法
print(f"The absolute path to the file: {path.absolute()}")

## is_dir方法
print(f"Is this path a folder? {path.is_dir()}")

## is_file()方法
print(f"Is this path a file? {path.is_file()}")

## exists()方法
print(f"Does this path exist? {path.exists()}")

# 利用已有的path去创建其他path
test_path = cwd / "test.py"
print(test_path)

## .stem属性(去掉拓展名)
print(f"The stem name of the path is: {test_path.stem}")

## .suffix属性(获取后缀)
print(f"The suffix of the path is: {test_path.suffix}")

## .parent属性
print(f"The parent of the path is: {test_path.parent}")

## mkdir() rmdir() touch() unlink()方法 
path1 = cwd / "new_folder"
empty_file_path = path1 / "empty_file.txt"
if not path1.exists():
    path1.mkdir()
    print(f"{path1.name} is created!")
    empty_file_path.touch()
    print(f"{empty_file_path.name} is created!")
else:
    if empty_file_path.exists():
            empty_file_path.unlink()
            print(f"{empty_file_path.name} is removed!")
    path1.rmdir()
    print(f"{path1.name} is removed!")

## rename()方法
path2 = cwd / "new_folder2"
########
if path2.exists():
     Path(path2 / 'empty_file.txt').unlink()
     path2.rmdir()
########
if path1.exists():
     path1.rename(path2)
     print(f"{path1.name} renames to {path2.name}")

## write_text() read_text()方法 (在json模块中已经使用过了)

print(cwd.resolve())
