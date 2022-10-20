import hashlib

def compute_file_hash(fileName: str) -> str:
    with open(fileName, 'rb') as obj:
        data = bytearray(obj.read())
        return hashlib.md5(data).hexdigest()

