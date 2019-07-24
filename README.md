# winaudit-python

Executes automatically a diagnostic of the computer every monday and outputs it to a pdf file named with the actual date.

### Why I did this program?

We have a computer that monitors sensors like cameras/temperatures/etc.. and we don't have a history report of the computer's healthy.
So we needed to find a way to create this report weekly automatically. First I tryed with a software called HWINFO but I found on their forum that they don't want to make this a feature of their software so I had to keep looking for another solutions.

## The solution

Since nobody keeps using this computer (its just a monitor screen so the employee keeps analysing the sensors data), I camed with this python script that will call the winaudit.exe every monday and output the result of the diagnostic into a pdf file name by today's date.

### Note

I couldn't find a way to interact with the program without needing of moving the mouse and clicking and typing things (it takes like 5 seconds to do the whole thing) 

First of all you need to fix the settings in the winaudit program like (check the code and read the comments):
- the time you need to wait until the diag is done
- the format that is been saved ( I rater choose pdf)
- make sure that the program will be open in full screen ( or adjust the position of the pixels )


# How to install

make sure you have python 3.7+ installed 

To install all the pip librarys required
```
 pip install -r requirements.txt
```

and finally:

```
python winaudit-python.py
```
