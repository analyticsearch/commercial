import base64

blockLength = 64

with open("usr", 'rb') as binFile:
    encodedString = base64.b64encode(binFile.read())

decodedString = base64.b64decode(encodedString)

Splitter = ()

for i in range(0, len(encodedString), blockLength):
    if i < len(encodedString) and i + blockLength > len(encodedString):
        Splitter += (encodedString[i:],)
    elif i < len(encodedString):
        Splitter += (encodedString[i:i+blockLength],)
    else:
        break

result = '['
for element in Splitter:
    result += '"' + element + '"' + ','

result = result[:-1] + ']'

print len(result)

with open("result", 'w') as outputFile:
    outputFile.write(result)
