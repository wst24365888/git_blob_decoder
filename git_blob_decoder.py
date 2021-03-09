import zlib

f = open('D:\\Dropbox\\Python\\git_blob_decoder\\a_blob_object', 'rb')
decompressed_data = zlib.decompress(f.read())

print(decompressed_data.decode('utf-8'))