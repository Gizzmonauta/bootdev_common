def int32_to_ip(int32):
    """
    Complete the function that takes an unsigned 32 bit number and returns a string representation 
    of its IPv4 address.

    Examples:
        2149583361 ==> "128.32.10.1"
        32         ==> "0.0.0.32"
        0          ==> "0.0.0.0"
    """
    if int32 >= 2**32 or int32 < 0:
        raise ValueError("Input must be a 32-bit unsigned integer.")
    current = int32
    octate = []
    temp_total = 0
    for i in range(31, -1, -1):
        bit, mod = divmod(current, 2**i)
        temp_total += bit * 2**(i % 8)
        if i % 8 == 0:
            octate.append(str(temp_total))
            temp_total = 0
        current = mod
    return ".".join(octate)

def int32_to_ip_solution(int32):
    # 1. Get the last number (far right)
    # The remainder of dividing by 256 gives you the last 8 bits (0-255)
    octet4 = int32 % 256
    
    # 2. Move the number over to the right by 8 bits (divide by 256)
    int32 = int32 // 256
    
    # 3. Repeat...
    octet3 = int32 % 256
    int32 = int32 // 256
    
    octet2 = int32 % 256
    int32 = int32 // 256
    
    octet1 = int32 % 256
    
    return f"{octet1}.{octet2}.{octet3}.{octet4}"

def main():
    ip_int = 3232235776
    ip_str = int32_to_ip(ip_int)
    print(f"The IP address for integer {ip_int} is {ip_str}")
    ip_int = 2149583361
    ip_str = int32_to_ip(ip_int)
    print(f"The IP address for integer {ip_int} is {ip_str}") 
    ip_int = 32
    ip_str = int32_to_ip(ip_int)
    print(f"The IP address for integer {ip_int} is {ip_str}")     
    ip_int = 0
    ip_str = int32_to_ip(ip_int)
    print(f"The IP address for integer {ip_int} is {ip_str}") 
    ip_int = 128
    ip_str = int32_to_ip(ip_int)
    print(f"The IP address for integer {ip_int} is {ip_str}") 

if __name__ == "__main__":
    main()