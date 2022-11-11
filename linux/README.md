# Introduction to the Linux Terminal

Familiarity with the terminal is key to being a productive developer. While it is often times not necessary, the terminal is often a faster or more idiomatic way to perform both simple and complex operations. The goal of this document (and the workshop) isn't to make you a master of using the terminal, however it will allow you to become familiar with the basics, introduce you to some key utilities, and generally make you more confident when learning more in the future.

The following document assumes that you are a complete novice and that this is your first introduction to the terminal. If this is not the case, feel free to skim the document for useful information.

Also, the following document is designed for use in bash/zsh. shells. Windows Powershell or Windows Command line is not supported. Some commands may work in the newer Windows Terminal application, but if you are on a Windows OS, try and use the WSL terminal instead if possible.

### The Filesystem

When you first open a terminal, you will be presented with an empty prompt. The prompt might look something like this:

```other
-bash-4.2$
```

What you see can be affected by a variety of different things; however, what is important is the `$`. The dollar sign (sometimes replaced with a `%` or `~` in the zsh shell), indicates where the start of every command you type begins.

While not every command operates on the filesystem, whenever a terminal is open you are able to operate directly with the filesystem. Additionally, you are given what is called a working directory. This working directory can be changed, but it provides a starting point for running commands and referencing files.

#### Viewing your Present Working Directory:

To view your present working directory, simply type the following: `pwd`. Doing so will create the following result (with the directory being different depending on your machine and user):

```shell
$ pwd
/Users/carsonwoods
```

#### Viewing Files in the Directory:

The terminal is very flexible, and can double as a file explorer window. Simply typing `ls` into the terminal will display all of the files in a directory. For example, say I was in a folder named `temp`. In order to view what was int the folder, I might use the following:

```shell
$ ls
example.txt
```

As you can see, this shows a file named `example.txt` in the directory. Thats great, but it doesn't show us the whole picture. The `ls` command will hide certain files and folders by default. Specifically, it will hide files that are prefixed with a `.`. This is because those files are frequently used as configuration directories or files on linux machines, and can quickly clutter your working directories. If you do want to see all the files, you can use the `-a` flag. Lets go back to our previous example. Lets assume we know there is a *single* hidden file and we just want to see it, so lets run the new command like so:

```shell
$ ls -a
.           ..          .hidden.txt example.txt
```

And now you can clearly see that there are now 4 files instead of 1! Wait... 4? Presumably, you're asking whats with those `.` and `..` files. Those are not files! They are directory pointers. We'll talk about that next, but first make sure to see how we now have a `.hidden.txt` file in the same directory where previously none was listed.

Now, onto the pointers. This is a key part of understanding relative files and how to navigate through directories. We'll cover moving into new directories next, but for now just know that the single period `.` corresponds to the current file you are currently in. The `..` pointer corresponds to the parent directory of your current directory. For example, if I am in the directory `/Users/carsonwoods/temp/` , then the `.` pointer would correspond with that directory, whereas the `..` pointer would correspond with `/Users/carsonwoods/`.

One thing I will add on the `ls` command is the `-l` option. This option forces the directory to be printed in a long, list format. This shows more detailed information about what type of file and permissions a specific file has. It also makes crowded and cluttered directories easier to read.

```shell
$ ls -al
total 16
drwxr-xr-x   4 carsonwoods  staff   128 Aug 30 12:01 .
drwxr-x---+ 72 carsonwoods  staff  2304 Aug 30 12:10 ..
-rw-r--r--   1 carsonwoods  staff    19 Aug 30 12:01 .hidden.txt
-rw-r--r--   1 carsonwoods  staff    12 Aug 30 11:59 example.txt
```

One final important piece of information is the `ls` command can be invoked on a folder that you are not currently *in*. This can be done by specifying the path to the file after any flags (or simply after the ls command if you wish to not use flags): `ls /Users/carsonwoods/temp` .

#### Moving into and out of Directories

To move from one directory to another is vital when using the terminal. To move from one directory to another, you use the `cd` command. This stands for "change directory" and it is extremely straightforward. You can pass into the command a full path (starting at your current directory or from `/` ) or you can use a relative path. Lets look at some examples:

```shell
$ cd temp
$ pwd
/Users/carsonwoods/temp
$ cd /Users/carsonwoods
$ pwd
/Users/carsonwoods
$ cd ./temp
$ pwd
/Users/carsonwoods/temp
$ cd ./../
$ pwd
/Users/carsonwoods
```

#### Copying, Moving, and Deleting Files

Copying, moving, and deleting files is important for filesystem manipulation. To do this, we use the `cp` ,`mv` , and `rm` commands respectively. The format for these commands is very simple and can be seen as follows:

```shell
# Copying a file from one location to another
cp /path/to/file /path/to/destination/location

# Copying a directory from one location to another
cp -r /path/to/directory/ /path/to/new/directory

# Moving a file from one location to another
mv /path/to/file /path/to/destination/location

# Renaming a file with the move command
mv /path/to/file/original-filename /path/to/file/new-filename

# Deleting a file
rm /path/to/file

# Deleting a directory
rm -r /path/to/directory

# Forcibly deleting a file
rm -f /path/to/file
```

#### Super-User Access

Some command require additional privileges. This is probably a familiar concept for those who have installed software before. You might have to temporarily authorize the computer to install programs to a privileged/secure location. This type of access is given to a so called super-user. To use command with super user access you must prefix whatever command you are running with `sudo` . Here is an example of a command (DO NOT RUN THE FOLLOWING COMMAND):

```shell
sudo rm -rf /usr/bin
```

#### Man Pages

Man pages are reference pages that exist for many different terminal commands. This is not even close to being a comprehensive introduction to the terminal. One quick way to learn more about new terminal commands is via the `man` command. See how the `man` command is used in the following example:

```shell
$ man mv

mv [-f | -i | -n] [-hv] source target
MV(1)                                                                                                                                                   General Commands Manual                                                                                                                                                   MV(1)

NAME
     mv – move files

SYNOPSIS
     mv [-f | -i | -n] [-hv] source target
     mv [-f | -i | -n] [-v] source ... directory

DESCRIPTION
     In its first form, the mv utility renames the file named by the source operand to the destination path named by the target operand.  This form is assumed when the last operand does not name an already existing directory.

     In its second form, mv moves each file named by a source operand to a destination file in the existing directory named by the directory operand.  The destination path for each operand is the pathname produced by the concatenation of the last operand, a slash, and the final pathname component of the named file.

     The following options are available:

     -f      Do not prompt for confirmation before overwriting the destination path.  (The -f option overrides any previous -i or -n options.)

     -h      If the target operand is a symbolic link to a directory, do not follow it.  This causes the mv utility to rename the file source to the destination path target rather than moving source into the directory referenced by target.

     -i      Cause mv to write a prompt to standard error before moving a file that would overwrite an existing file.  If the response from the standard input begins with the character 'y' or 'Y', the move is attempted.  (The -i option overrides any previous -f or -n options.)

     -n      Do not overwrite an existing file.  (The -n option overrides any previous -f or -i options.)

     -v      Cause mv to be verbose, showing files after they are moved.

     It is an error for the source operand to specify a directory if the target exists and is not a directory.

     If the destination path does not have a mode which permits writing, mv prompts the user for confirmation as specified for the -i option.

     As the rename(2) call does not work across file systems, mv uses cp(1) and rm(1) to accomplish the move.  The effect is equivalent to:

           rm -f destination_path && \
           cp -pRP source_file destination && \
           rm -rf source_file

EXIT STATUS
     The mv utility exits 0 on success, and >0 if an error occurs.

     The command "mv dir/afile dir" will abort with an error message.

LEGACY DIAGNOSTICS
     In legacy mode, the command "mv dir/afile dir" will fail silently, returning an exit code of 0.

     For more information about legacy mode, see compat(5).

EXAMPLES
     Rename file foo to bar, overwriting bar if it already exists:

           $ mv -f foo bar

COMPATIBILITY
     The -h, -n, and -v options are non-standard and their use in scripts is not recommended.

     The mv utility now supports HFS+ Finder and Extended Attributes and resource forks.  The mv utility will no longer strip resource forks off of HFS files.  For an alternative method, refer to cp(1).

SEE ALSO
     cp(1), rm(1), symlink(7)

STANDARDS
     The mv utility is expected to be IEEE Std 1003.2 ("POSIX.2") compatible.

HISTORY
     A mv command appeared in Version 1 AT&T UNIX.
```

