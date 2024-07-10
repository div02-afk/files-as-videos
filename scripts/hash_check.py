import hashlib

def calculate_file_hash(path, hash_algo='sha256'):
    hash_func = hashlib.new(hash_algo)
    with open(path, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()




def hash_check(path1,path2):
    hash1 = calculate_file_hash(path1)
    hash2 = calculate_file_hash(path2)
    return hash1 == hash2