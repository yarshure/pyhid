# pyhid
pyhid use BKT-05

## Only keyboard  work

example input password
```
def doControl(c):
    c.keyboard_free()
    c.word("888888",1)
    c.keyboard(["LEFT_SHIFT","q"],1)
    c.keyboard("ENTER",1)
def doPhone(c):
    c.keyboard_free()
    c.word("888888",1)
```

## todo finish keymap
