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

I don't really know Qt6. (or any Qt all that well). Most of what I know I've learned on this project.

Having issue with it not reading `~/.config/qt6ct/qt6ct.conf` (if it is supposed to read it at all?)

Or how to have it read and apply it. I use Xfce4.

Hence the theme being applied and the font setting.

Some parts of the UI are resizable, but no changes are saved as I've not dug into that yet.

I chose Python and Qt6 because that is what ChatGPT seemed to produce the fewest mistakes on for earlier attempts.

## Requirements

Apart from the latest python3 for your system, qt6 is requrired.

```shell
$ dnf list installed 'qt6*'
Installed Packages
qt6-qtbase.x86_64                                                  6.3.1-3.el9                                                      @epel
qt6-qtbase-common.noarch                                           6.3.1-3.el9                                                      @epel
qt6-qtbase-devel.x86_64                                            6.3.1-3.el9                                                      @epel
qt6-qtbase-gui.x86_64                                              6.3.1-3.el9                                                      @epel
qt6-qtbase-static.x86_64                                           6.3.1-3.el9                                                      @epel
qt6-qtsvg.x86_64                                                   6.3.1-2.el9                                                      @epel
qt6-qttools.x86_64                                                 6.3.1-3.el9                                                      @epel
qt6-qttools-common.noarch                                          6.3.1-3.el9                                                      @epel
qt6-rpm-macros.noarch                                              6.3.1-1.el9                                                      @epel
qt6ct.x86_64                                                       0.6-0.1.git6abd586.el9                                           @epel
```

<!---
  CudaText: lexer_file=Markdown; tab_size=2; tab_spaces=No; newline=LF;
  --->
