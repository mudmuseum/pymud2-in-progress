# pymud2-in-progress
A simple Python multiplayer MUD.

## Features

1. Threaded socket server, UTF-8 encoding
2. Loading / Saving / Lookup help files (JSON)
3. Player loading / saving (JSON)
4. World management and loading (JSON)
5. Greeting screen via help file
6. Commands:
  * quit
  * save
  * version
  * login
  * commands

## Start up

```bash
./start.sh
Loading game...
Game loaded, loading help...
Help loaded, loading world...
World loaded, loading zones...
Zones loaded, setting up socket server...
Socket Server setup, running in thread Thread-1
Game is ready to rock on 127.0.0.1:9000
5 seconds have elapsed...
```

## Greeting

```bash
nc -c localhost 9000

                     _,,--.._
                    /. ` ` .  `.
                    )|       `  `.
       .           / |         `  `
        `.        / /            ` `
         `.`.    / /              ` `
           `.`.'' /                ' :
            <','/'`                . ;
           ,-'.-    `             , /
       _.-',-^`       `      _.-----
 /`==::.,-'     `       ` ,-'
/ /               `     .;
| |..               ` .,' `.
| ':`....---.       ,'`'.   `.
 .`:.:.:.:.:-..    /     `.   `.
  .`ccoccoccoc'``./        `.   `.
   `.`CQCCQCCCQCC/           `.   `.
     `.`8O8O8O8O8(             `.   `.
       `.`_-_@-@_-;              `. .'"'.
            '""'                   :,' ,--'
                                    `.` _,--
             A                        `.  _,',.
            (@)                         `. .-' `_
                                          `. ,-^.`.
               A                            `. - _.-.
              (@)                             `.', ,'-
                                                `. _,-`__
                                                  `. _-,`|
                                                    |,_-`|
   Zot                                              '----'

Welcome to PyMud2! What is your traveler's name?
```
