def get_country_codes(param):
    # Your code here. Maybe try pseudocoding this one out?
    alpha_list = []
    converted_string = ""
    for char in prices:
        if char.isalpha():
            alpha_list.append(char)
    
    for i in range(int(len(alpha_list)/2)):
        
         converted_string  += "".join(alpha_list[i*2:(i*2) + 2]) + ", "
        
    return converted_string
