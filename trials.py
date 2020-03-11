Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> message = "crap bag"
>>> print(message)
crap bag
>>> name = "ada lovelace"
>>> print(name.title())
Ada Lovelace
>>> name = "harold ochieng"
>>> print(name.subtitle())
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(name.subtitle())
AttributeError: 'str' object has no attribute 'subtitle'
>>> name = "sex education season 2 is lit"
>>> print(name.upper())
SEX EDUCATION SEASON 2 IS LIT
>>> print(name.lower())
sex education season 2 is lit
>>> first_name = "harold"
>>> last_name = "ochieng"
>>> full_name = f"{first_name}{last_name}"
>>> print(full_name)
haroldochieng
>>> print(full_name.title())
Haroldochieng
>>> print(full_name.upper())
HAROLDOCHIENG
>>> first_name = "harold"
>>> last_name = "ochieng"
>>> full_name = f"{first_name} {last_name}"
>>> print(full_name)
harold ochieng
>>> print(full_name.upper())
HAROLD OCHIENG
>>> message = "Harold"
print ("\tmessage")


