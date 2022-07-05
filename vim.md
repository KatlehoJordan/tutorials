Watched a setup tutorial for within VS Code here:
https://www.youtube.com/watch?v=h-epcklOC_g&ab_channel=SuboptimalEngineer

Created keyboard shortcut `ctrl` + `shift` + `/` to toggle vim mode in case get stuck somewhere or unable to use default VS code shortcuts (such as `ctrl` + `n` for opening new file)

Mapped escape to normal mode as instructed in that first video to the key combos `j` + `k` and `k` + `j`

To get the vim 'redo' and 'virtual blocks' functionality, had to add custom keyboard shortcut to the keybindings.json (which can be launched from the command palette)
Watching neural Nine's tutorial here, but paused at around minute 20, before he started talking about 'VISUAL LINES' mode:
https://www.youtube.com/watch?v=jXud3JybsG4&ab_channel=NeuralNine


Video here about some ways to be a little more effective around minute 9. Has to do with remapping caps lock to esc and speeding up key repeat, and a few minutes later a link to cheatsheet, and also advice on ~/.vimrc.
https://www.youtube.com/watch?v=_NUO4JEtkDw&ab_channel=thoughtbot

Found keyboard shortcut list here:
https://vim.rtorr.com   /

What I have learned so far:
0 - go to beginning of the line
$ - go to the end of the line
% - go to matching bracket or quotation
gg - go to beginning of file
<n>gg - go to the beginning of line number <n>
<n>G - same as <n>gg
<n> - numeric modifier for many commands to alter their behavior
G - go to end of file
w - go to next word (stop at punctuation)
W - go to next word (ignoring punctuation)
b - go to previous word (stopping at punctuation)
B - go to previous word (ignoring punctuation)
i - insert before cursor
I - insert before line
a - insert after cursor
A - insert after line
o - insert next line
O - insert previous line
j - move down
k - move up
h - move left
l - move right
j k - escape to 'NORMAL' mode
k j - escape to 'NORMAL' mode
cw - change word (delete rest of the current word and enter into 'INSERT' mode)
ciw - change word (delete the entire current word, regardless of where the cursor is, and enter into 'INSERT' mode)
c<bracket or quotation>w - change within the brackets (delete contents within the brackets and enter into 'INSERT' mode)
C - change rest of the line (delete the rest of the line and enter into 'INSERT' mode)
cc - change the whole line (delete the line and enter into 'INSERT' mode)
dw - delete rest of the current word (without entering 'INSERT' mode)
diw - delete word, regardless of where the cursor is (without entering 'INSERT' mode)
d<bracket or quotation>w - delete contents within brackets (without entering into 'INSERT' mode)
D - delete the rest of the line (without entering 'INSERT' mode) 
dd - delete the entire line (without entering 'INSERT' mode)
r - replace character at cursor
R - enter into 'REPLACE' mode
u - undo
<n>u - undo <n> actions
ctrl + r - redo (see note above --- had to adjust vs code keybindings)
<n> ctrl + r - redo <n> actions
p - paste contents 'yanked' from 'VISUAL' mode after cursor
P - paste contents 'yanked' from 'VISUAL' mode before cursorp - paste any contents "yanked" while in 'VISUAL' mode
v - toggle 'VISUAL' mode
. - repeat the last command
zz - center the view at your cursor position
> - indent right
< - indent left
= - indent selection
gg=G - indent entire file
/ - search for next string (end with enter)
n or # - jump to next search hit
N - jump to previous search hit
:s/<old word>/<new word>/gc - find and replace and confirm replacement
:s/<old word>/<new word>/gc - find and replace everywhere and confirm replacement
:set relativenumber - gives relative line numbers in the gutter


From inside 'VISUAL' mode:
use similar keys as in 'NORMAL' mode to make a selection
y - yank selection
yy - yank entire line from the cursor
Y - yank entire line
yi<bracket or quotation> - yank from inside bracket
p - paste contents 'yanked' from 'VISUAL' mode after cursor
P - paste contents 'yanked' from 'VISUAL' mode before cursor

Launch 'VISUAL LINES' mode in order to select multiple lines:
shift + v

Launch 'VISUAL BLOCKS' mode in order to select multiple columns:
ctrl + v