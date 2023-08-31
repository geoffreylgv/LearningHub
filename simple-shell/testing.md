# It is very important to test your code from start
In the simple shell project, you should test every new feature you have added. Don't only test the new feature though, test also everything else that new feature could have affected.

This is important for avoiding your application becoming too large to debug memory leaks. Memory leaks are easier to spot as you progress...

## Compilation with gcc
The compilation command is provided on the intranet:
```
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 *.c -o hsh
```
Don't try to compile specific files. In this kind of projects, you can have several files, and it is too much work to always list the *.c files to compile. This means that you should keep your project folder clean all the time, and have only useful *.c files in there.

Now, the previous compilation command is the basic you need. If you want to also check for memory leaks, you can either use the ```-fsanitize=address -g``` option in your gcc command, or compile normaly and then use valgrind when you are running your program (further below).
Here is how you would compile if you want to add the AddressSanitizer
```
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 -fsanitize=address -g *.c -o hsh
```
> **Note**
> When compiled with the AddressSanitizer, you will get a lot of address outputs when you have memory leaks. I personally don't know yet how to read these. So, I instead go with valgrind. However, it is good to know that when compiled with the AddressSanitizer option, you are certain that as long as no colorful address information show up, you are good on memory...

## Running your compiled program
A normal call of your program in interactive mode would be ```./hsh```, provided you are still in your working directory in which you compiled the program.
This should open your prompt, and you can type in different commands to test your program, like ```ls```, ```/bin/ls``` ..., depending on where you are at, in your tasks of the project.

> **Important**
> Now, instead of just running your program, you can use valgrind that will do memory check for you.

This is how you use it
```
valgrind --track-origins=yes ./hsh
```
When run with the previous command, you get reports on memory leaks and any errors. This is important since the ALX checker uses valgrind to check for memory leaks in your program. You may have to exit, ```CTRL+D``` (assuming you added that handling to your code), before you see memory leaks and errors in some cases.

> **Note**
> Don't forget to also test your program in non interactive mode, i.e. whithout entering the program, you instead pipe in your command like the followings:
```
echo "            " | ./hsh

#OR

echo "ls
pwd
cd /dev" | ./hsh
```


## The test suite
Since the ALX checker is made available only a day before the first deadline, you have 14 days to work blindly, and it is difficult to test your code correctly. The rule of thumb is, when not otherwise specified in the project description, your program should behave exactly like the Bourne Shell (sh).

This includes:

* Error message syntax ```sh: 1: lkds: not found```,
* Exit status, checked after exiting the sh or ./hsh program with ```$?``` or within the program if you already have implemented Variables,
* The formatting of the output for commands that are executed correctly... i.e. not adding any extra new lines, or any extra prompt ("$ ").
* Printing is done to the appropriate stream (stderr vs. stdout)

> **Important**
> The test suite is a very important tool to be aware of. It saves you from having to deal with problems all in one day before the deadline, with a high chance to mess things up even more.

The test suite is a suite maintained by some ALX students who use the actual ALX checker test cases in a bash script, hence emulating the real checker.
Here is a [link to the test suite](https://github.com/Fuzzworth/alx_test_suite/tree/main/simple_shell_project). Scroll down on the page, and you should a README that shows you how to set it up for testing your program.

When your program gives the expected output, it shows a green ```OK```. Otherwise, it gives you what was gotten from your program (GOT), vs. what was expected by the test suite (EXPECTED). It also gives you the command that was run. So, you can always copy that command and test yourself, and very useful is that GOT vs. EXPECTED. Sometimes, it is just the exit status issue, other times it is just the stream that the output was printed to which is not the right one, .... But at least this gives you an idea where to start looking.

> **Important**
> If you have not compiled with the AddressSanitizer, you will not detect memory leaks when running the test suite ```./runchecker.bash #```, where "#" is the task you are trying to check with the test suite. Even Valgrind doesn't help you when running the test suite. So, compile you program with the AddressSanitizer before runnning the test suite, at least when you think everything works perfectly fine with your own tests, and when the test suite without AddressSanitizer gives you all green OK. This can save your life.

If you have any questions or something is unclear, feel free to create an issue on the issues tab of the repository. If you feel like something was misleading after your tests, you can create a Pull Request in which you address the issue. Read the [Contributions guideline](../CONTRIBUTING.md) for how to proceed to contribute to this learning materials repository.
