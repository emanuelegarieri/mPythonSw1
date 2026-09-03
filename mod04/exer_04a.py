zander = float(input("Enter the length of the zander in centimeters: "))
if zander >= 42:
    print("The zander meets the size limit.")
else:
    print(
        "The zander does not meet the size limit.\n" +
          "Please release the fish back into the lake.\n" +
          f"The fish was {42-zander:.1f} centimeters below the size limit."
          )
    