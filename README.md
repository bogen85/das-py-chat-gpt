# das-py-chat-gpt

Several parts of this Chat-GPT wrote for me and I interacted with it to get them working.

First I had it write a terminal based python chat-gpt chat app for me in multiple modules and we debugged that together.

Then I had it write a qt6 GUI skeleton where the buttons just sent the text to output window.
We debugged that together.

Then I took the two and combined them into a GUI app.

First time it is run it will create the virtual environment.
(use `make run` to run)

In the terminal it will ask for model to use and your auth token.

Those will stored in the ChatGPT.data along with chat logs and edit texts.

The primary text input has history, access via ctrl left and right arrows.
(up and down being ignored, might be something in my desktop setup)

All edit inputs are multiline.

`Ctrl-Enter` or the button sends.

Output history is saved and is restored on next run of the program.

I don't really know Qt6. (or any Qt).

Having issue with it not reading `~/.config/qt6ct/qt6ct.conf` (if it is supposed to read it at all?)

Or how to have it read and apply it. I use Xfce4.

Hence the theme being applied and the font setting.

Some parts of the UI are resizable, but no changes are saved as I've not dug into that yet.

<!---
  CudaText: lexer_file=Markdown; tab_size=2; tab_spaces=No; newline=LF;
  --->
