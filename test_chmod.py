from chmod import Chmod


def test_text1():
    c = Chmod('rwxrwxrwx')
    assert c.getNumeric() == '777'


def test_text2():
    c = Chmod('rwxr-xr-x')
    assert c.getNumeric() == '755'


def test_text3():
    c = Chmod('rw-r--r--')
    assert c.getNumeric() == '644'


def test_text4():
    c = Chmod('rwx------')
    assert c.getNumeric() == '700'


def test_text_same():
    c = Chmod('rwxrwxrwx')
    assert c.getText() == 'rwxrwxrwx'


def test_text_incomplete():
    c = Chmod('rwxrwx')
    assert c.getNumeric() == 'rwxrwx'


def test_text_larger():
    c = Chmod('rwxrwxrwxrwx')
    assert c.getNumeric() == 'rwxrwxrwxrwx'


def test_text_wrong_letter():
    c = Chmod('abc')
    assert c.getNumeric() == 'abc'


def test_numeric1():
    c = Chmod('777')
    assert c.getText() == 'rwxrwxrwx'


def test_numeric2():
    c = Chmod('755')
    assert c.getText() == 'rwxr-xr-x'


def test_numeric3():
    c = Chmod('644')
    assert c.getText() == 'rw-r--r--'


def test_numeric4():
    c = Chmod('700')
    assert c.getText() == 'rwx------'


def test_numeric_same():
    c = Chmod('777')
    assert c.getNumeric() == '777'


def test_numeric_incomplete():
    c = Chmod('77')
    assert c.getText() == '77'


def test_numeric_bigger():
    c = Chmod('777777777')
    assert c.getText() == '777777777'


def test_numeric_wrong():
    c = Chmod('999')
    assert c.getText() == '999'
