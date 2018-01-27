# Any Alias
Any Alias, or simply `a`, is a Python 3 tool to increase productivity and lower your command typing time. Started as
 base part for `d`, Any Alias evolved into a stand-alone tool to provide basic functionality.

### Installation

**Linux**

Run `./install.sh`. You should have access to `a` right away, the installation path is usually `/home/$USER/.local/bin`.

**Mac**

Run `./install.sh`. You will be asked to input the directory to install into. Note, that your directory should be in
 your `$PATH`, i.e. in your `.bash_profile`.

**Windows**

We do not target Windows platforms, sorry. If you figure out the installation, please do not hesitate to create a pull
 request with a windows installer. Thank you in advance.

### Commands
You may define your custom commands in `alias.yml` in a folder where you need your commands. Say, you define `alias.yml`
 in `/home/foo` like so: 

```yaml
version: 1.0

commands:
  e:
    - echo Hello
    - echo World
```
Now, when you execute `a e` in `/home/foo`, Any Alias will run `echo Hello` and then `echo World`. Executing `a e` in
 `/home/bar` will give no result, unless same `alias.yml` is specified there as well.

### Commands inheritance

Any Alias will always loop over your path towards root (`/`) in attempt to merge as many `alias.yml` files in any of
 parent folders into one list, to make as many commands available.
If you specify two commands under one key, any child command will override any parent command. I.e. assume you have the
 following hierarchy:

```yaml
# /home/example/alias.yml

version: 1.0

commands:
  e: echo Hello World
  l: ls -la
  
# /home/example/project/alias.yml

version: 1.0

commands:
  e: ls -la
``` 

When you execute `a e` in `/home/example`, it will result in output of `Hello World`, but when you execute `a e` in
 `/home/example/project`, `ls -la` will be executed instead. 

### Variables in your commands

Sometimes you need to specify your own input when running custom command. Enclosing your variable between `%%` and `%%`
 will tell Any Alias you have a variable there:

```yaml
version: 1.0

commands:
  e:
    - echo %%hello%%
    - echo %%world%%
```

If you run `a e Hello World`, you will get

```
[user@localhost ~]$ a e Hello World
Hello
World
```

You should always specify all the variables defined in your commands. Otherwise an error will be thrown:

```
[user@localhost ~]$ a e
FATAL: You did not specify the variable value for your command.
```

### Named arguments and variables

Sometimes you need to specify multiple commands with a variable, which has one value. Instead of specifying the same
 amount of arguments as there are variables, you may use named variables:

```yaml
version: 1.0

commands:
  messages:
    - echo Hello %%hello%%
    - echo %%hello%%
```

Now, you may execute `a messages world world` or you could execute `a messages --hello=world`. In both cases you will
 receive:
```
[user@localhost ~]$ a messages world world
Hello world
world
[user@localhost ~]$ a messages --hello=world
Hello world
world
```

### Spaces in variable values

If you need to use a long string with spaces in your variable values, enclose it in quotes:

```yaml
version: 1.0

commands:
  e:
    - echo %%hello%%
```

If you run `a e 'Hello World'`, you will get the following:

```
[user@localhost ~]$ d e 'Hello World'
Hello World
``` 

### What is the point?

We use Any Alias for development. It help with the routine of typing long commands into short one.
Accessing one of our servers requires typing `ssh -i /home/user/.ssh/id_rsa user@server` **A LOT**.
Typing all those letters a couple times a day makes it really annoying. Any Alias helps us with allowing to simply type
 `a c`.

### Help

If you run `a`, it will list all available commands. As said above, Any Alias will iterate over towards root (`/`) and
 read all `alias.yml` files on the way to show it to you.