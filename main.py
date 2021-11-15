from hashlib import sha256
import random

MAX_NONCE = 100000000000
k = 1
while k > 0: 
    def SHA256(text):
        return sha256(text.encode("ascii")).hexdigest()
    
    def mine(block_number, transactions, previous_hash, prefix_zeros):
        i = 0
        prefix_str = '0'*prefix_zeros
        for nonce in range(MAX_NONCE):
            text = str(block_number) + transactions + previous_hash + str(nonce)
            new_hash = SHA256(text)
            i = i + 1
            if new_hash.startswith(prefix_str):
                print(f"Yay! Successfully mined $SHIB with nonce value:{nonce}")
                return new_hash
    
        raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")
    
    if __name__=='__main__':
        transactions= "User #" + str(random.random()) + "sent" + str(random.random()) + " $SHIB to User #" + str(random.random())
        difficulty=5 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
        import time
        start = time.time()
        prev_hash = '000000000009c037e71eeee20352f8986d728dd5135738dd928ab90c'
        new_hash = mine(5,transactions,prev_hash, difficulty)
        total_time = str((time.time() - start))
        print(transactions)
        print(f"end mining. Mining took: {total_time} seconds")
        print(new_hash)
        print()
