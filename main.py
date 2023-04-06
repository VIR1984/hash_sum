import hashlib

input_hash_num =  int (input ("Enter a number to get the hash function: "))
convert_to_byte = bytes (input_hash_num)

hash_sum = convert_to_byte

hash_object = hashlib.sha256(hash_sum)
hex_dig = hash_object.hexdigest()

print("Hash sum of your number: " + hex_dig)


