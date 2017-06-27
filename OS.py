import os

print(os.name)              #to show the OS name
print(os.environ)

print(os.path.abspath('.')) #to show the absolute path
print(os.path.join('C:/python/','python01')) #to show the new path

print(os.mkdir('C:/python/python01'))         #to create a folder than is named after 'python01'
print(os.rmdir('C:/python/python01'))  #to delete a folder which is named after 'python_folder'

print(os.path.split('C:/python/test.txt'))
print(os.path.splitext('C:/python/test.txt'))

print(os.rename('test.txt','test.py'))
print(os.remove('test.py'))

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])