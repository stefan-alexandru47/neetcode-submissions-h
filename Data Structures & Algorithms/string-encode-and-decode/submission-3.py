class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_res = ""

        for s in strs:
            encode_res += str(len(s)) + '#' + s
        print ("Encode result: " + encode_res)
        return encode_res

    def decode(self, s: str) -> List[str]:
        decode_res = []
        i = 0
        num = 0 # number that tells us how long each string is

        while True:
            if i >= len(s):
                break

            print("While Loop Started")
            current_string = ""

            num_str = ""
            while i < len(s): # loops twice because length is 2 
                print("Num builder: " + str(i))
                if s[i] == '#':
                    print ('Num created: ' + str(num))
                    i += 1
                    break
                num_str += s[i]
                i += 1
            
            num = int(num_str)

            for j in range(num): # doesn't add anything, each string remains empty
                current_string += s[i]
                print("Character added")
                i += 1
                

            print ("String appended")
            decode_res.append(current_string)

            # It should loop once and others should not show up 
                
            num = 0 # reset code to 0 for next code

            print("While Loop Finished")

            if i >= len(s):
                break

        return decode_res