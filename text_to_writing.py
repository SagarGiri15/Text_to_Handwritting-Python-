import pywhatkit as pw



txt = input("Enter the text")



pw.text_to_handwriting(txt,"converted.png",[0,0,100])



print("Successfully Converted")