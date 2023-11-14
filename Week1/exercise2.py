dc_location = input("\nEnter data center location: ")
#insert white space after entering location and pressing Enter
print("\nStrip off whitespace:")
print(f"Before: {repr(dc_location)}")
print("\nUpper case:")
print(dc_location.upper())


print(f"After:  {repr(dc_location.strip())}")

print("\nMethod chaining:")
print(repr(dc_location.upper().strip()))