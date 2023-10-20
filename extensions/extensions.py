m = input('file type')
file_type = m.lower().strip().rsplit('.',1)
file_type_clean = file_type[1]
match file_type_clean:
    case 'gif':
        print('image/gif')
    case 'jpg':
        print('image/jpeg')
    case 'jpeg':
        print('image/jpeg')
    case 'png':
        print('image/png')
    case 'pdf':
        print('application/pdf')
    case 'txt':
        print('text/plain')
    case 'zip':
        print('application/zip')
    case "":
        print('application/octet-stream')
    case _:
        print('application/octet-stream')