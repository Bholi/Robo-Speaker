import os
if __name__ == '__main__':
    print("Welcome To Robo Speaker")
    while True:
        text = input("Enter any text or press q to exit the program : ")
        if text == 'q':
            os.system("say bye bye friend")
            break
        command = f"say {text}"
        os.system(command)
