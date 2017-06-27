from io import BytesIO
f=BytesIO()
f.write('python 工程师'.encode('utf-8'))
print(f.getvalue())