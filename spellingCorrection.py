
from tkinter import *
from  textblob  import TextBlob


# Function to clear both the text entry boxes
def clearAll():
    word1_field.delete(0, END)
    word2_field.delete(0, END)


# Function to get a corrected word
def correction():
    input_word = word1_field.get()

    # create a TextBlob object
    blob_obj = TextBlob(input_word)

    # get a corrected word
    corrected_word = str(blob_obj.correct())

    # insert method inserting the
    # value in the text entry box.
    word2_field.insert(10, corrected_word)


# Driver code
if __name__ == "__main__":
    # Create a GUI window
    root = Tk()
    root.configure(background='light green')
    root.geometry("400x150")
    root.title("Spell Corrector")

    # Create Welcome to Spell Corrector Application: label
    headlabel = Label(root, text='Welcome to Spell Corrector Application',
                      fg='black', bg="red")

    # Create a "Input Word": label
    label1 = Label(root, text="Input Word",
                   fg='black', bg='dark green')

    # Create a "Corrected Word": label
    label2 = Label(root, text="Corrected Word",
                   fg='black', bg='dark green')
    headlabel.grid(row=0, column=1)
    label1.grid(row=1, column=0)
    label2.grid(row=3, column=0, padx=10)


    # for filling or typing the information.
    word1_field = Entry()
    word2_field = Entry()


    word1_field.grid(row=1, column=1, padx=10, pady=10)
    word2_field.grid(row=3, column=1, padx=10, pady=10)

    # Create a Correction Button and attached
    # with correction function
    button1 = Button(root, text="Correction", bg="red", fg="black",
                     command=correction)

    button1.grid(row=2, column=1)


    button2 = Button(root, text="Clear", bg="red",
                     fg="black", command=clearAll)

    button2.grid(row=4, column=1)

    # Start the GUI
    root.mainloop()
