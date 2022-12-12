# Set the secret key to some random bytes. Keep this really secret!
def base64_encode(data):
    """
    Encodes data into base64

    Args:
        data (str): data to encode

    Returns:
        str: base64 encoded data
    """
    # Write this function without the base64 module
    converted = ""
    for i in range(0, len(data), 3):
        # Get the next 3 bytes
        block = data[i:i + 3]

        # Convert the block to a number
        num = 0
        for j in range(len(block)):
            num += ord(block[j]) << (8 * (2 - j))

        # Convert the number to 4 base64 characters
        for j in range(4):
            if i * 8 + j * 6 > len(data) * 8:
                converted += "="
            else:
                converted += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"[
                    num >> (6 * (3 - j)) & 0x3F]
    return converted
