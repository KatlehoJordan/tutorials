# Vim introduction

Vim is a powerful text editor. I will be trying to use a Vim emulator in VS Code.

## Customizations I made for VS Code neovim extension

Downloaded the `.zip` file for neovim put it in program files. Added a line of code to the `settings.json` file to point to the path and had to use extra backslashes to escape the backslashes in the path.

Specifically:
```
    "vscode-neovim.neovimExecutablePaths.win32": "C:\\Program Files\\nvim-win64\\bin\\nvim.exe",
```

I also modified the behavior of `ctrl` + `h` and `ctrl` + `w` in the VS Code keyboard shortcuts.

## Customizations I made for VS Code Emulation of Vim

I followed the setup tutorial for within VS Code - https://www.youtube.com/watch?v=h-epcklOC_g&ab_channel=SuboptimalEngineer  

Note that using the VS Code Emulation of Vim, instead of VS Code Neovim Extension, results in needing to make many more customizations, and the end result is still that some key combinations conflict between the Vim emulator and how you would expect things to behave in VS Code; thus, I recommend sticking to the neovim implementation.

Mapped `j` + `k` and `k` + `j` to `<Esc>` in 'NORMAL' and 'VISUAL' modes since `<Esc>` has other uses in VS Code.

```
    "vim.useCtrlKeys": true,
    "vim.insertModeKeyBindings": [
        {
            "before": [
                "k",
                "j"
            ],
            "after": [
                "<Esc>"
            ]
        },
        {
            "before": [
                "j",
                "k"
            ],
            "after": [
                "<Esc>"
            ]
        }
    ],
    "vim.visualModeKeyBindings": [
        {
            "before": [
                "k",
                "j"
            ],
            "after": [
                "<Esc>"
            ]
        },
        {
            "before": [
                "j",
                "k"
            ],
            "after": [
                "<Esc>"
            ]
        }
    ]    
    "vim.normalModeKeyBindingsNonRecursive": [
        {
            "before": [
                "u"
            ],
            "commands": [
                "undo"
            ]
        },
        {
            "before": [
                "<C-r>"
            ],
            "commands": [
                "redo"
            ]
        }
    ],
```

I created keyboard shortcut `ctrl` + `shift` + `/` to toggle vim mode in case get stuck somewhere or unable to use default VS code shortcuts (such as `ctrl` + `n` for opening new file).

To get the vim 'redo' functionality, had to add custom keyboard shortcut to the keybindings.json (which can be launched from the command palette).

```
    {
        "key": "ctrl+shift+oem_2",
        "command": "toggleVim"
    },
    {
        "key": "capslock",
        "command": "extension.vim_escape",
        "when": "editorTextFocus && vim.active && !inDebugRepl"
    },
    {
        "key": "escape",
        "command": "-extension.vim_escape",
        "when": "editorTextFocus && vim.active && !inDebugRepl"
    },
    {
        "key": "ctrl+v",
        "command": "extension.vim_ctrl+v",
        "when": "textInputFocus && vim.mode != 'Insert'"
    },
    {
        "key": "ctrl+r",
        "command": "extension.vim_ctrl+r",
        "when": "textInputFocus && vim.mode != 'Insert'"
    },
```

## Launching Vim

For the first time, it is best to run `vimtutor`. If you cannot run that from terminal, then you first need to install vim on your machine.

## Exiting Vim

To exit Vim, you will use a command. [More on commands later](#commands).

The command to exit Vim is `:q!`. The `:` initiates a command string. The `q` means quit. The `!` means accept that you are quitting without saving changes to the file you are in.

## 'NORMAL' mode

If you ever want to get back to 'NORMAL' mode, from within vim you would press 'Esc' key. However, depending on if you set up a keymap switch with caps lock (see software for that below) and if you are using the Vim emulator or neovim, you will get back to 'NORMAL' mode in different ways.

If you did not swap the keymappings for `Esc` and `CapsLock` but are using neovim: press `Esc`.
If you swapped the keymappings for `Esc` and `CapsLock` and are using neovim: press `CapsLock`.
If you did not swap the keymappings for `Esc` and `CapsLock` and are using the vim emulator, then if you followed the instructions above in this document for setting vs code keybindings, press in rapid succession either `j` then `k` or `k` then `j`.

## Operators and motions

### Operators do something.

Operators include:
`x` - delete character under the cursor
`r` - replace character at cursor  
`R` - enter into 'REPLACE' mode  
`d` - delete something without going into 'INSERT' mode, and store the deleted item in the 'Vim register'
`D` - delete the rest of the line without going into 'INSERT' mode, and store the deleted item in the 'Vim register'
`dd`- delete the whole line without going into 'INSERT' mode, and store the deleted item in the 'Vim register'
`c` - change (remove) something and go into 'INSERT' mode
`C` - change (remove) the rest of the line and go into 'INSERT' mode
`cc` - change (remove) the whole line and go into 'INSERT' mode

### Motions indicate to where to do that thing.

Motions include:
`j` - move down  
`k` - move up  
`h` - move left  
`l` - move right  
`0` - go to beginning of the line  
`$` - go to the end of the line  
`gg` - go to beginning of file  
`G` - go to end of file  
`w` - go to next word, respecting punctuation as word delimiters  
`W` - go to next word, ignoring punctuation  
`b` - go to previous word, respecting punctuation as word delimiters  
`B` - go to previous word, ignoring punctuation  
`e` - to the end of the current word, respecting punctuation as word delimiters
`E` - to the end of the current word, ignoring punctuation
`(` or `{` - to the beginning of the parenthesis or code block
`)` or `}` - to the end of the parenthesis or code block
`%` - go to matching bracket `(` `)` `[` `]` `{` `}`
`i` - inside of (for example the word, paranthesis, or code block)

#### Motion modifiers

Using numbers, motions can be modified. For example:

`<n>gg` - go to the beginning of line number <n>  
`<n>G` - same as <n>gg  
`ctrl` + `g` - give information about file and location in file - behaves differently in VS Code vs Vim

### Going into 'INSERT' mode

`i` - insert before cursor  
`I` - insert before line  
`a` - insert after cursor  
`A` - insert after line  
`o` - insert next line  
`O` - insert previous line  
`<n>o` - insert <n> new lines after current line
`<n>O` - insert <n> new lines before current line

#### Indentation

`>` - indent right  
`<` - indent left  
`=` - indent selection  

#### Combining indentation and motions

`gg=G` - indent entire file  

#### Combining operators and motions

`dw` - delete rest of the current word (without entering 'INSERT' mode), and store the deleted item in the 'Vim register'
`diw` - delete word, regardless of where the cursor is (without entering 'INSERT' mode), and store the deleted item in the 'Vim register'
`di<bracket or quotation>` - delete contents within brackets (without entering into 'INSERT' mode), and store the deleted item in the 'Vim register'
`D` - delete from cursor through the end of the line, and store the deleted item in the 'Vim register'
`d$` - same as `D`
`d0` - delete from cursor through the beginning of the line, and store the deleted item in the 'Vim register'
`de` - delete from cursor through the end of the current word, and store the deleted item in the 'Vim register'
`cw` - change word
`ciw` - change inside word
`ci<bracket or quotation>` - change inside brackets
`C` - change from cursor through the end of the line
`c$` - same as `C`
`c0` - chage from cursor through the end of the line
`ce` - change from cursor through the end of the current word
`cc` - change the entire line
`yw` - 'yank' up to the next word
`yiw` - 'yank' the word the cursor is inside of
`yi<bracket or quotation>` - 'yank' contents within brackets
`Y` - 'yank' from cursor through the end of the line
`y$` - same as `Y`
`y0` - 'yank' from cursor through the start of the line
`ye` - 'yank' from cursor through the end of the current word
`yy` - 'yank' the entire line

## Other functionality

`zz` - center the view at your cursor position  
`.` - repeat the last command
`u` - undo  
`<n>u` - undo <n> actions  
`U` - undo whole line, note that this can be undone with `u`
`ctrl` + `r` - redo (see note above --- had to adjust vs code keybindings)  
    `<n>ctrl` + `r` - redo <n> actions  
`v` - toggle 'VISUAL' mode  
`p` - print previously deleted or 'yanked' text after the cursor
`P` - print previously deleted or 'yanked' text before the cursor
`ZZ` - exit the currently opened help window without exiting vim

## 'VISUAL' mode  

Use similar keys as in 'NORMAL' mode to make a selection, then can use the various versions of 'yanking' to move the contents to the vim register.
`shift` + `v` - launch 'VISUAL LINES' mode to select multiple lines
`ctrl` + `v` - launch 'VISUAL BLOCKS' mode to select multiple columns

## Commands

Commands end with pressing the `enter` key. They often start by using the `:`, but some are initiated with other keys.

For commands that are initiated with `:`, one can use `ctrl` + `d` in order to get auto-complete suggestions for commands. For example, `:e` followed by `ctrl` + `d` will show commands such as `earlier`, `echo`, `echoconsole`, etc. Furthermore, `tab` can then be used to provide tab-completion. Note that this works in Vim, but not in the Vim emulator in VS Code.

Also note that not all of these commands have been tested using the neovim implementation in VS Code, so it may be just as easy to use the VS Code functions (by putting yourself in insert mode then using VS Code keyboard shortcuts) if the following commands do not work as well.

`:w` - save changes to the open file
`:wq` - save changes to the open file and quit Vim
`:w <FILENAME>` - save the current file with the given `FILENAME` - does not work from VS Code, since will only save the current file without saving with a new name. This can be used to save partial selections of text by first highlighting text you want to save in another file with 'VISUAL' mode; then use `:` to start entering a command, whereupon you should see `<,>` in the prompt; finish saving with `w <FILENAME>`; unfortunately, this also does not seem to work from the VS Code emulation of Vim, but only in Vim.
`:q!` - quit Vim without saving changes to the open file
`:e <FILENAME>` - open a `<FILENAME>` for editing
`/<string>` - search for next <string>, searching document from top to bottom
`/<string>\c` - search for the next <string>, searching document from bottom to top, and ignoring case
`?<string>` - search for previous <string>, searching document from bottom to top
`?<string>\c` - search for the previous <string>, searching document from bottom to top, and ignoring case
`n` or `#` - jump to next search hit  
`N` - jump to previous search hit
`ctrl` + `o` - move cursor to previous search return
`ctrl` + `i` - move cursor to next search return (if you used `ctrl` + `o` previously)
`:s/<old word>/<new word>` - find and replace first instance
`:s/<old word>/<new word>/g` - find and replace all instances in the line
`:<num>,<num>s/<old word>/<new word>/g` - find and replace all instances in the line range from `<num>`  to `<num>`
`:%s/<old word>/<new word>/g` - find and replace all instances in the file
`:%s/<old word>/<new word>/gc` - find and replace all instances in the file, but pause to confirm replacement at each match
`:!<shell command>` - how to run shell commands from within Vim - does not seem to work from VS Code Vim emulator, but does work from Vim (try `:! ls` or `:! pwd`)
`:r` - starts 'retrieving' text to be inserted after the cursor. Can be used as in `:r <FILENAME>` or `:r !<shell command>`, etc.

## Recording a macro

Type `q` then `<any key>` to start recording a macro. You stop recording when you press `q` again. Now, if you press `@` + `<any key>` you will redo what you recorded.

## Settings 

`:set number` - gives absolute line number for the current line in the gutter
`:set relativenumber` - gives line numbers relative to the current line in the gutter
`:set ruler` - not available in VS Code, just Vim, but shows row and column number in bottom right of terminal session
`:set ic` - ignores case when searching
`:set hlsearch` - highlights matches when searching
`:set incsearch` - highlights strings you are searching for as you type the string
`:noh` - removes highlighting from the previous search
`:set cp` - puts Vim into 'compatible' mode, which is usually to be avoided since it disables most of the features added by Vim that extend the vi text editor
`:set no<setting>` - shuts off the given `<setting>`
`:set inv<setting>` - in neovim, inverts the value of the given `<setting>`

## Getting more help

The following are some help commands that can be run from Vim. These do not work from the VS Code emulation of Vim, unfortunately.

To launch Vim, from a terminal, use `vim`.

`:help` - opens help text file in a new pane
`ctrl` + `]` - from within the help menu, jumps to tagged section
`ctrl` + `t` - if you jumped to a tagged section, this will jump you back to where you were before
`ctrl` + `w` then `ctrl` + `w` again - cycles through open text file panes
`:help vimrc-intro` - get help creating your own vimrc profile
`:help user-manual` - opens the Vim user manual, which is extensive
A book dedicated to vim - http://iccf-holland.org/click5.html
For remapping the keyboard in Windows 10, use Sharpkeys although, if you use the Vim emulator (and not neovim and the neovim extension), you will still need to map the jk/kj to escape in the VS Code settings since the escape key has different behavior in VS code by default - https://github.com/randyrants/sharpkeys/releases
For remapping the keyboard in Mac, this site is suggested - https://pqrs.org/osx/karabiner/seil.html.en
It is recommended to modify the key repeat rate. In Windows, search "keyboard" and modify the 'repeat delay' and 'repeat rate'. In OSx, 
Vim cheatsheet - http://www.viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html
Site for vimrc files (it is recommended to version control your own vimrc and other profiles) - https://github.com/mscoutermarsh/dotfiles or https://github.com/thoughtbot/dotfiles
Another learning tool instead of vimtutor - vim-adventures.com
Also recommended to watch screencasts - http://vimcasts.org or https://upcase.com/vim
A list of keyboard shortcuts - https://pqrs.org/osx/karabiner 
https://vim.rtorr.com
Plugins for development if vim becomes your primary text editor include githumb.com/kien/ctrlp.vim ; github.com/scrooloose/nerdtree , github.com/rking/ag.vim
If you run neovim, to run vimtutor, use `:Tutor` or `:Tutor vim-01-beginner`

## Next steps

Run `:help user_toc.txt` to browse sections that could be useful or interesting. Then start using vim at home to do some of the projects shown by NeuralNine. 
Opening the help menu and following the instructions in there in terms of reading through the entire manual. After that, start using nvim at work in VS Code.