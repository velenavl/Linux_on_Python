
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)
    if result.returncode == 0 and text in result.stdout:
        return True
    else:
        return False


folderin = '/home/user/test'
folderout = '/home/user/out'
# print(checkout('cd /home/user/test; 7z a /home/user/arh1', 'Everything is Ok'))


def test_step1():
    assert checkout(f'cd {folderin}; 7z a {folderout}/arh1', 'Everything is Ok'), 'test1 FAIL'


def test_step2():
    assert checkout(f'cd {folderin}; 7z u {folderout}/arh1', 'Everything is Ok'), 'test2 FAIL'


def test_step3():
    assert checkout(f'cd {folderout}; 7z l arh1.7z', 'Method'), 'test3 FAIL'


def test_step4():
    assert checkout(f'cd {folderout}; 7z d arh1.7z', 'Everything is Ok'), 'test4 FAIL'


def test_step5():
    assert checkout(f'cd {folderout}; 7z x arh1.7z', 'Everything is Ok'), 'test5 FAIL'


def test_step6():
    hash = subprocess.run(f'cd {folderout}; crc32 arh1.7z', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    assert checkout(f'cd {folderout}; 7z h arh1.7z', hash.stdout.upper()), 'test6 FAIL'
